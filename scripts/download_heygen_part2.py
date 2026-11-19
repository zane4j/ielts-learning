#!/usr/bin/env python3
"""Download and package the 24 already-generated HeyGen IELTS Part 2 MP3s.

Usage:
  python3 scripts/download_heygen_part2.py \
    --manifest speaking/part2/people/heygen_audio_24.json \
    --output dist/IELTS_Part2_Zoe_24_MP3.zip

No HeyGen API key, text-to-speech generation, or third-party Python package is required.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen
from zipfile import ZIP_STORED, ZipFile

TRACK_COUNT = 24
MAX_BYTES = 25 * 1024 * 1024


def read_manifest(path: Path) -> list[dict]:
    tracks = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(tracks, list) or len(tracks) != TRACK_COUNT:
        raise ValueError("The manifest must contain exactly 24 tracks.")

    numbers = []
    filenames = []
    for track in tracks:
        number = track["no"]
        filename = track["filename"]
        url = track["url"]
        parts = urlparse(url)
        if not isinstance(number, int) or not (1 <= number <= TRACK_COUNT):
            raise ValueError("Invalid track number.")
        if (
            not isinstance(filename, str)
            or filename != Path(filename).name
            or not filename.endswith(".mp3")
        ):
            raise ValueError("Unsafe track filename.")
        if (
            parts.scheme != "https"
            or parts.netloc.lower() != "resource2.heygen.ai"
            or not parts.path.endswith(".mp3")
        ):
            raise ValueError(f"Track {number:02d}: invalid HeyGen MP3 URL.")
        numbers.append(number)
        filenames.append(filename)

    if sorted(numbers) != list(range(1, TRACK_COUNT + 1)):
        raise ValueError("Track numbers must be exactly 1–24.")
    if len(set(filenames)) != TRACK_COUNT:
        raise ValueError("Duplicate MP3 filenames.")
    return sorted(tracks, key=lambda t: t["no"])


def verify_mp3(path: Path) -> None:
    size = path.stat().st_size
    if not 20_000 <= size <= MAX_BYTES:
        raise ValueError(f"Unexpected file size: {size} bytes")
    with path.open("rb") as f:
        header = f.read(4)
    if not (
        header.startswith(b"ID3")
        or (header[0] == 0xFF and header[1] & 0xE0 == 0xE0)
    ):
        raise ValueError("Not an MP3 file; the server may have returned an HTML error.")
    if shutil.which("ffprobe"):
        result = subprocess.run(
            [
                "ffprobe", "-v", "error",
                "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1",
                str(path),
            ],
            capture_output=True, text=True, timeout=20, check=False,
        )
        if result.returncode != 0:
            raise ValueError("ffprobe could not read the MP3.")
        try:
            duration = float(result.stdout.strip())
        except ValueError as exc:
            raise ValueError("MP3 duration is not readable.") from exc
        if not 20 <= duration <= 600:
            raise ValueError(f"Unexpected audio duration: {duration:.1f}s")


def download_one(track: dict, directory: Path) -> tuple[int, int]:
    number = track["no"]
    destination = directory / track["filename"]
    for attempt in range(1, 4):
        temporary = destination.with_suffix(".part")
        try:
            req = Request(
                track["url"],
                headers={
                    "User-Agent": "IELTS-Part2-Audio-Downloader/1.0",
                    "Accept": "audio/mpeg,*/*",
                },
            )
            with urlopen(req, timeout=60) as response, temporary.open("wb") as out:
                size = 0
                while chunk := response.read(256 * 1024):
                    size += len(chunk)
                    if size > MAX_BYTES:
                        raise ValueError("File exceeded maximum expected size.")
                    out.write(chunk)
            verify_mp3(temporary)
            temporary.rename(destination)
            return number, destination.stat().st_size
        except HTTPError as exc:
            temporary.unlink(missing_ok=True)
            if exc.code not in (408, 429, 500, 502, 503, 504) or attempt == 3:
                raise RuntimeError(
                    f"Track {number:02d}: HTTP {exc.code} (URL may have expired)"
                ) from exc
        except (URLError, OSError, TimeoutError, ValueError, subprocess.TimeoutExpired) as exc:
            temporary.unlink(missing_ok=True)
            if attempt == 3:
                raise RuntimeError(
                    f"Track {number:02d}: {type(exc).__name__}: {exc}"
                ) from exc
        time.sleep(2 ** attempt)
    raise AssertionError("unreachable")


def make_zip(tracks: list[dict], directory: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_suffix(".tmp")
    try:
        # MP3 is compressed already; ZIP_STORED avoids unnecessary recompression.
        with ZipFile(temporary, "w", compression=ZIP_STORED) as archive:
            for track in tracks:
                source = directory / track["filename"]
                verify_mp3(source)
                archive.write(source, arcname=track["filename"])
            archive.writestr(
                "README.txt",
                "IELTS Speaking Part 2 — 24 Zoe practice recordings.\n"
                "Generated by HeyGen Voice, male en-US voice (Keanu).\n"
                "Each MP3 contains the English question and complete English answer.\n",
            )
        with ZipFile(temporary) as archive:
            names = [n for n in archive.namelist() if n.endswith(".mp3")]
            expected = [t["filename"] for t in tracks]
            if names != expected or archive.testzip() is not None:
                raise ValueError("ZIP integrity check failed.")
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--manifest", type=Path,
        default=Path("speaking/part2/people/heygen_audio_24.json"),
    )
    parser.add_argument(
        "--output", type=Path,
        default=Path("dist/IELTS_Part2_Zoe_24_MP3.zip"),
    )
    args = parser.parse_args()
    try:
        tracks = read_manifest(args.manifest)
        with tempfile.TemporaryDirectory(prefix="heygen-part2-") as temp:
            directory = Path(temp)
            failures = []
            with ThreadPoolExecutor(max_workers=4) as pool:
                tasks = {
                    pool.submit(download_one, track, directory): track
                    for track in tracks
                }
                for future in as_completed(tasks):
                    try:
                        number, size = future.result()
                        print(f"[{number:02d}/24] Validated {size // 1024} KB", flush=True)
                    except Exception as exc:
                        failures.append(str(exc))
            if failures:
                for error in failures:
                    print(f"ERROR: {error}", file=sys.stderr)
                raise RuntimeError(
                    f"{len(failures)} download(s) failed; refusing to create a partial ZIP."
                )
            make_zip(tracks, directory, args.output)
        print(f"SUCCESS: {args.output} — 24 MP3 files")
        return 0
    except (OSError, KeyError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
