#!/usr/bin/env python3
"""Read the 25 original IELTS Part 2 scripts and create Chinese-title + English MP3s.

Each topic: Chinese male voice says the title, short quiet gap, then the original
English answer with English male voice. Never log the API key or the speech body.
"""
import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "speaking/part2/minimal-memory/ZOE_PHILIPPINES_25_TOPICS.md"
OUTPUT = ROOT / "speaking/part2/audio"
HEADING = re.compile(r"^## ([PLEO]\d{2}) — (.+)$", re.MULTILINE)
BODY = re.compile(
    r"### 1 — INTRO\n\n([\s\S]*?)\n\n"
    r"### 2 — WHAT\n\n([\s\S]*?)\n\n([\s\S]*?)\n\n"
    r"### 3 — WHY / HOW\n\n([\s\S]*?)\n\n([\s\S]*?)\n\n"
    r"\*\*1 分钟准备"
)
CATEGORIES = {
    "P": "人物类",
    "E": "事件类",
    "O": "物品类",
    "L": "地点类",
}
# Spoken Chinese titles and file names follow the exact study labels.
# P16 is number 01 among people per the requested example, not number 11.
NAME_OVERRIDES = {"P16": "擅长学习语言的人"}


def load_topics():
    markdown = SOURCE.read_text(encoding="utf-8")
    headings = list(HEADING.finditer(markdown))
    if not headings:
        raise ValueError("No Part 2 topic headings found")
    topics = {}
    for index, heading in enumerate(headings):
        end = headings[index + 1].start() if index + 1 < len(headings) else len(markdown)
        topic_id, original_title = heading.group(1), heading.group(2).strip()
        match = BODY.search(markdown[heading.start():end])
        if not match:
            raise ValueError(f"Cannot parse five English paragraphs for {topic_id}")
        paragraphs = [value.replace("**", "").strip() for value in match.groups()]
        if len(paragraphs) != 5 or not all(paragraphs):
            raise ValueError(f"Expected five paragraphs for {topic_id}")
        title = NAME_OVERRIDES.get(topic_id, original_title)
        topics[topic_id] = {"title": title, "paragraphs": paragraphs}

    if len(topics) != 25:
        raise ValueError(f"Expected 25 topics, found {len(topics)}")

    # Give each category sequential numbers; put P16 first as explicitly requested.
    for letter, category in CATEGORIES.items():
        members = [topic_id for topic_id in topics if topic_id.startswith(letter)]
        if letter == "P":
            members = ["P16"] + [topic_id for topic_id in members if topic_id != "P16"]
        for index, topic_id in enumerate(members, 1):
            title = topics[topic_id]["title"]
            safe_title = re.sub(r'[\/\\:*?"<>|／]', "-", title).strip()
            topics[topic_id]["file_name"] = f"{category}_{index:02d}_{safe_title}.mp3"

    names = [entry["file_name"] for entry in topics.values()]
    if len(set(names)) != 25:
        raise ValueError("Audio filenames must be unique")
    return topics


def format_english(paragraphs, paragraph_pause=0.50):
    # Keep the punctuation as written; do not insert mechanical pauses after
    # every sentence. Only separate the five paragraphs.
    return f" <#{paragraph_pause:.2f}#> ".join(paragraphs)


def call_minimax(text, api_key, base_url, model, voice, speed, language):
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
        "language_boost": language,
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
        # Avoid printing untrusted response bodies or credentials.
        raise RuntimeError(
            f"MiniMax HTTP {exc.code}; verify API key, endpoint region and balance"
        ) from None
    except URLError:
        raise RuntimeError("MiniMax network/DNS connection failed") from None

    status = result.get("base_resp") or {}
    code = status.get("status_code")
    if code != 0:
        raise RuntimeError(
            f"MiniMax error code={code}: {status.get('status_msg', 'Unknown error')}"
        )
    hex_audio = (result.get("data") or {}).get("audio")
    if not isinstance(hex_audio, str) or not hex_audio:
        raise RuntimeError("MiniMax returned no audio")
    try:
        audio = bytes.fromhex(hex_audio)
    except ValueError:
        raise RuntimeError("MiniMax returned invalid hex audio") from None
    if len(audio) < 1024 or not (
        audio.startswith(b"ID3")
        or (audio[0] == 0xFF and (audio[1] & 0xE0) == 0xE0)
    ):
        raise RuntimeError("MiniMax returned empty or non-MP3 audio")
    return audio


def join_audio(chinese_mp3, english_mp3, destination):
    """Join different voice clips with silence, using ffmpeg without shell calls."""
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required to combine Chinese and English speech")
    command = [
        "ffmpeg", "-hide_banner", "-loglevel", "error", "-y",
        "-i", str(chinese_mp3),
        "-i", str(english_mp3),
        "-f", "lavfi", "-i", "anullsrc=r=32000:cl=mono:d=0.65",
        "-filter_complex", "[0:a][2:a][1:a]concat=n=3:v=0:a=1[out]",
        "-map", "[out]", "-ar", "32000", "-ac", "1",
        "-c:a", "libmp3lame", "-b:a", "128k", str(destination),
    ]
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    if result.returncode != 0 or not destination.is_file() or destination.stat().st_size < 2048:
        raise RuntimeError("ffmpeg failed to combine the Chinese title and English body")


def main():
    parser = argparse.ArgumentParser(description="MiniMax IELTS Part 2 bilingual MP3")
    parser.add_argument("--topic", default="P16", help="P16, another topic ID, or all")
    parser.add_argument("--dry-run", action="store_true", help="Validate without any paid API call")
    parser.add_argument("--speed", type=float, default=0.85, help="English speed, 0.5-2.0")
    parser.add_argument("--voice", default="English_Trustworthy_Man")
    parser.add_argument("--chinese-voice", default="male-qn-qingse")
    parser.add_argument("--model", default="speech-2.8-hd")
    args = parser.parse_args()

    if not 0.5 <= args.speed <= 2.0:
        parser.error("--speed must be between 0.5 and 2.0")
    topics = load_topics()
    chosen = args.topic.upper()
    selected = list(topics) if chosen == "ALL" else [chosen]
    if any(name not in topics for name in selected):
        parser.error(f"Unknown topic ID: {args.topic}")

    if not args.dry_run:
        api_key = os.environ.get("MINIMAX_API_KEY", "").strip()
        if not api_key:
            raise RuntimeError("MINIMAX_API_KEY repository secret is missing")
        base_url = os.environ.get(
            "MINIMAX_API_BASE", "https://api.minimaxi.com/v1"
        ).strip()
        if not base_url.startswith("https://"):
            raise RuntimeError("MINIMAX_API_BASE must be HTTPS")
        if not shutil.which("ffmpeg"):
            raise RuntimeError("ffmpeg is unavailable; no paid requests were sent")
        OUTPUT.mkdir(parents=True, exist_ok=True)

    for topic_id in selected:
        item = topics[topic_id]
        english = format_english(item["paragraphs"])
        spoken = " ".join(item["paragraphs"])
        word_count = len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?", spoken))
        print(f"{topic_id}: {word_count} words, output {item['file_name']}")
        if args.dry_run:
            continue
        # One Chinese title request + one English body request. Both are billed
        # by MiniMax; the workflow will not auto-retry failures.
        with tempfile.TemporaryDirectory(prefix="ielts-minimax-") as folder:
            folder = Path(folder)
            title_audio = call_minimax(
                item["title"] + "。", api_key, base_url, args.model,
                args.chinese_voice, 1.0, "Chinese"
            )
            (folder / "title.mp3").write_bytes(title_audio)
            body_audio = call_minimax(
                english, api_key, base_url, args.model,
                args.voice, args.speed, "English"
            )
            (folder / "body.mp3").write_bytes(body_audio)
            staging = folder / "combined.mp3"
            join_audio(folder / "title.mp3", folder / "body.mp3", staging)
            destination = OUTPUT / item["file_name"]
            shutil.copy2(staging, destination)
            print(f"Generated {destination.relative_to(ROOT)} ({destination.stat().st_size} bytes)")
        if len(selected) > 1:
            time.sleep(0.5)

    print("DRY RUN PASSED" if args.dry_run else "BILINGUAL MP3 GENERATION COMPLETED")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
