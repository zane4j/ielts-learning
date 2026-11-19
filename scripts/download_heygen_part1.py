#!/usr/bin/env python3
"""Download 40 already-generated HeyGen IELTS Speaking Part 1 MP3s and ZIP them.

No HeyGen API key and no third-party Python packages required.
Usage:
    python3 scripts/download_heygen_part1.py --dry-run
    python3 scripts/download_heygen_part1.py
"""
from __future__ import annotations

import argparse
import csv
from concurrent.futures import ThreadPoolExecutor, as_completed
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

EXPECTED_TOPICS = 40
EXPECTED_QUESTIONS = 197
MAX_BYTES = 50 * 1024 * 1024
DEFAULT_MANIFEST = Path("speaking/part1/heygen_audio_40.csv")
DEFAULT_OUTPUT = Path("dist/IELTS_Part1_40_Topics_MP3.zip")


def read_manifest(path: Path) -> list[dict]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        tracks = list(csv.DictReader(handle))
    if len(tracks) != EXPECTED_TOPICS:
        raise ValueError(f"Expected {EXPECTED_TOPICS} topics, found {len(tracks)}")

    seen_names = set()
    total_questions = 0
    for n, track in enumerate(tracks, start=1):
        if int(track["index"]) != n:
            raise ValueError(f"Wrong topic index at row {n}")
        filename = track["filename"]
        if (
            not filename.startswith(f"{n:02d}_")
            or not filename.endswith(".mp3")
            or filename != Path(filename).name
            or "/" in filename
            or "\\" in filename
            or filename in seen_names
        ):
            raise ValueError(f"Unsafe or duplicate filename at row {n}: {filename}")
        seen_names.add(filename)
        parts = urlparse(track["url"])
        if (
            parts.scheme != "https"
            or parts.hostname != "resource2.heygen.ai"
            or not parts.path.endswith(".mp3")
            or parts.query
        ):
            raise ValueError(f"Invalid HeyGen MP3 URL at row {n}")
        if not track["topic"].strip():
            raise ValueError(f"Missing Topic at row {n}")
        count = int(track["question_count"])
        duration = float(track["duration_seconds"])
        if count < 1 or not 10 < duration < 1800:
            raise ValueError(f"Unexpected questions/duration at row {n}")
        total_questions += count
    if total_questions != EXPECTED_QUESTIONS:
        raise ValueError(
            f"Expected {EXPECTED_QUESTIONS} questions, found {total_questions}"
        )
    return tracks


def verify_mp3(path: Path, expected_seconds: float) -> None:
    size = path.stat().st_size
    if not 20_000 <= size <= MAX_BYTES:
        raise ValueError(f"Unexpected MP3 file size: {size} bytes")
    with path.open("rb") as handle:
        header = handle.read(4)
    if not (
        header.startswith(b"ID3")
        or (len(header) >= 2 and header[0] == 0xFF and header[1] & 0xE0 == 0xE0)
    ):
        raise ValueError("Downloaded content does not have an MP3 header")
    if shutil.which("ffprobe"):
        result = subprocess.run(
            [
                "ffprobe", "-v", "error", "-show_entries", "format=duration",
                "-of", "default=noprint_wrappers=1:nokey=1", str(path),
            ],
            capture_output=True, text=True, timeout=30, check=False,
        )
        if result.returncode:
            raise ValueError(f"ffprobe rejected MP3: {result.stderr[:150]}")
        duration = float(result.stdout.strip())
        if abs(duration - expected_seconds) > max(8.0, expected_seconds * 0.15):
            raise ValueError(
                f"MP3 duration mismatch: {duration:.1f}s vs {expected_seconds:.1f}s"
            )


def download_one(track: dict, directory: Path) -> tuple[str, int]:
    filename = track["filename"]
    destination = directory / filename
    last_error = None
    for attempt in range(1, 4):
        partial = destination.with_suffix(".part")
        try:
            req = Request(
                track["url"],
                headers={
                    "User-Agent": "Mozilla/5.0 (IELTS-HeyGen-Downloader/1.0)",
                    "Accept": "audio/mpeg,*/*",
                },
            )
            with urlopen(req, timeout=90) as response, partial.open("wb") as out:
                size = 0
                while chunk := response.read(256 * 1024):
                    size += len(chunk)
                    if size > MAX_BYTES:
                        raise ValueError("MP3 exceeds 50 MiB size limit")
                    out.write(chunk)
            verify_mp3(partial, float(track["duration_seconds"]))
            partial.replace(destination)
            return filename, destination.stat().st_size
        except HTTPError as exc:
            last_error = f"HTTP {exc.code}"
            partial.unlink(missing_ok=True)
            if exc.code not in (408, 429, 500, 502, 503, 504):
                break
        except (URLError, OSError, TimeoutError, ValueError, subprocess.TimeoutExpired) as exc:
            last_error = f"{type(exc).__name__}: {exc}"
            partial.unlink(missing_ok=True)
        if attempt < 3:
            time.sleep(2 ** attempt)
    raise RuntimeError(f"{filename}: {last_error} (HeyGen URL may have expired)")


def write_zip(tracks: list[dict], directory: Path, manifest: Path, output: Path) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    partial = output.with_suffix(".tmp")
    try:
        with ZipFile(partial, "w", compression=ZIP_STORED) as archive:
            for track in tracks:
                path = directory / track["filename"]
                verify_mp3(path, float(track["duration_seconds"]))
                archive.write(path, arcname=track["filename"])
            archive.write(manifest, arcname="audio_links.csv")
            archive.writestr(
                "README.txt",
                "IELTS Speaking Part 1 - 40 HeyGen MP3s / 197 Q&A.\n"
                "One track per Topic, in workbook order.\n"
                "Topic -> longer pause -> Question -> Answer, repeated.\n"
                "American English male voice; original worksheet responses.\n",
            )
        with ZipFile(partial) as archive:
            mp3_names = [n for n in archive.namelist() if n.endswith(".mp3")]
            if mp3_names != [x["filename"] for x in tracks]:
                raise ValueError("ZIP does not contain the expected 40 ordered MP3s")
            if archive.testzip() is not None:
                raise ValueError("ZIP integrity check failed")
        partial.replace(output)
    finally:
        partial.unlink(missing_ok=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        tracks = read_manifest(args.manifest)
        print(f"Validated {len(tracks)} topics and {EXPECTED_QUESTIONS} Q&A pairs.")
        if args.dry_run:
            print("Dry-run complete; no network requests or ZIP created.")
            return 0

        with tempfile.TemporaryDirectory(prefix="heygen-part1-") as folder:
            directory = Path(folder)
            failures = []
            with ThreadPoolExecutor(max_workers=4) as pool:
                futures = [pool.submit(download_one, t, directory) for t in tracks]
                for future in as_completed(futures):
                    try:
                        name, size = future.result()
                        print(f"OK: {name} ({size // 1024} KiB)", flush=True)
                    except Exception as exc:
                        failures.append(str(exc))
            if failures:
                for error in failures:
                    print("ERROR: " + error, file=sys.stderr)
                raise RuntimeError(
                    f"{len(failures)} downloads failed; incomplete ZIP will not be created"
                )
            write_zip(tracks, directory, args.manifest, args.output)
        print(f"SUCCESS: {args.output} — {EXPECTED_TOPICS} MP3s")
        return 0
    except (OSError, KeyError, TypeError, ValueError, RuntimeError, csv.Error) as exc:
        print(f"FAILED: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
