#!/usr/bin/env python3
"""Generate IELTS Part 2 MP3 with the official MiniMax T2A v2 API.

Reads the existing Markdown scripts verbatim; only removes Markdown bold markers.
The API key and source text are never printed to the workflow log.
"""
import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "speaking/part2/minimal-memory/ZOE_PHILIPPINES_25_TOPICS.md"
OUTPUT = ROOT / "speaking/part2/audio"
HEADING = re.compile(r"^## ([PLEO]\d{2}) —", re.MULTILINE)
BODY = re.compile(
    r"### 1 — INTRO\n\n([\s\S]*?)\n\n"
    r"### 2 — WHAT\n\n([\s\S]*?)\n\n([\s\S]*?)\n\n"
    r"### 3 — WHY / HOW\n\n([\s\S]*?)\n\n([\s\S]*?)\n\n"
    r"\*\*1 分钟准备"
)


def load_topics():
    markdown = SOURCE.read_text(encoding="utf-8")
    headings = list(HEADING.finditer(markdown))
    if not headings:
        raise ValueError("No Part 2 topic headings found")

    topics = {}
    for index, heading in enumerate(headings):
        finish = headings[index + 1].start() if index + 1 < len(headings) else len(markdown)
        topic = heading.group(1)
        match = BODY.search(markdown[heading.start():finish])
        if not match:
            raise ValueError(f"Cannot parse five paragraphs for {topic}")
        paragraphs = [value.replace("**", "").strip() for value in match.groups()]
        if len(paragraphs) != 5 or not all(paragraphs):
            raise ValueError(f"Expected five non-empty paragraphs for {topic}")
        topics[topic] = paragraphs
    if len(topics) != 25:
        raise ValueError(f"Expected 25 topics, found {len(topics)}")
    return topics


def format_speech(paragraphs, sentence_pause=0.20, paragraph_pause=0.75):
    # MiniMax supports explicit <#seconds#> silence tags.
    parts = []
    for paragraph in paragraphs:
        with_pauses = re.sub(
            r"(?<=[.!?]) (?=[A-Z])",
            f" <#{sentence_pause:.2f}#> ",
            paragraph,
        )
        parts.append(with_pauses)
    return f" <#{paragraph_pause:.2f}#> ".join(parts)


def synthesize(text, api_key, base_url, voice, speed, model):
    payload = {
        "model": model,
        "text": text,
        "stream": False,
        "voice_setting": {
            "voice_id": voice,
            "speed": speed,
            "vol": 1,
            "pitch": 0,
        },
        "audio_setting": {
            "format": "mp3",
            "sample_rate": 32000,
            "bitrate": 128000,
            "channel": 1,
        },
        "language_boost": "English",
        "output_format": "hex",
    }
    request = Request(
        base_url.rstrip("/") + "/t2a_v2",
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    try:
        with urlopen(request, timeout=180) as response:
            result = json.load(response)
    except HTTPError as exc:
        # Do not print response bodies: they may contain private data.
        raise RuntimeError(
            f"MiniMax HTTP {exc.code}; check API Key, API region and balance"
        ) from None
    except URLError:
        raise RuntimeError("Cannot reach MiniMax API (network or DNS error)") from None

    status = result.get("base_resp") or {}
    code = status.get("status_code")
    if code != 0:
        raise RuntimeError(
            f"MiniMax API error code={code}: {status.get('status_msg', 'Unknown error')}"
        )
    hex_audio = (result.get("data") or {}).get("audio")
    if not isinstance(hex_audio, str) or not hex_audio:
        raise RuntimeError("MiniMax returned no audio")
    try:
        audio = bytes.fromhex(hex_audio)
    except ValueError:
        raise RuntimeError("MiniMax returned invalid hex audio") from None
    is_mp3 = audio.startswith(b"ID3") or (
        len(audio) > 2 and audio[0] == 0xFF and (audio[1] & 0xE0) == 0xE0
    )
    if not is_mp3 or len(audio) < 1024:
        raise RuntimeError("Unexpected audio format or empty MP3")
    return audio


def main():
    parser = argparse.ArgumentParser(description="MiniMax IELTS Part 2 TTS")
    parser.add_argument("--topic", default="P16", help="P16, another topic ID, or all")
    parser.add_argument("--dry-run", action="store_true", help="Validate text without API calls")
    parser.add_argument("--speed", type=float, default=0.78)
    parser.add_argument("--voice", default="English_Trustworthy_Man")
    parser.add_argument("--model", default="speech-2.8-hd")
    args = parser.parse_args()

    if not 0.5 <= args.speed <= 2.0:
        parser.error("--speed must be between 0.5 and 2.0")

    topics = load_topics()
    topic = args.topic.upper()
    selection = list(topics) if topic == "ALL" else [topic]
    if any(name not in topics for name in selection):
        parser.error(f"Unknown topic: {args.topic}")

    if not args.dry_run:
        api_key = os.environ.get("MINIMAX_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("MINIMAX_API_KEY repository secret is missing")
        base_url = os.environ.get(
            "MINIMAX_API_BASE", "https://api.minimaxi.com/v1"
        ).strip()
        if not base_url.startswith("https://"):
            raise RuntimeError("MINIMAX_API_BASE must use HTTPS")
        OUTPUT.mkdir(parents=True, exist_ok=True)

    for name in selection:
        paragraphs = topics[name]
        script = format_speech(paragraphs)
        spoken = " ".join(paragraphs)
        word_count = len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", spoken))
        print(f"{name}: {word_count} English words, {len(script)} TTS input chars")
        if args.dry_run:
            continue
        mp3 = synthesize(script, api_key, base_url, args.voice, args.speed, args.model)
        file_path = OUTPUT / f"{name}.mp3"
        partial = file_path.with_suffix(".mp3.part")
        partial.write_bytes(mp3)
        partial.replace(file_path)
        print(f"Saved {file_path.relative_to(ROOT)} ({len(mp3)} bytes)")
        if len(selection) > 1:
            time.sleep(0.5)

    print("DRY RUN PASSED" if args.dry_run else "TTS GENERATION COMPLETED")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
