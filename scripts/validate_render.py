#!/usr/bin/env python3
"""Verify that an audio render is inside the project's 3-4 minute contract."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import wave
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("audio", type=Path)
    parser.add_argument("--min-seconds", type=float, default=180)
    parser.add_argument("--max-seconds", type=float, default=240)
    return parser.parse_args()


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as audio:
        frame_rate = audio.getframerate()
        if frame_rate <= 0:
            raise ValueError("WAV frame rate must be positive")
        return audio.getnframes() / frame_rate


def ffprobe_duration(path: Path) -> float:
    executable = shutil.which("ffprobe")
    if executable is None:
        raise RuntimeError("ffprobe is required for non-WAV audio")
    result = subprocess.run(
        [
            executable,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        capture_output=True,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or "ffprobe could not read the audio")
    return float(result.stdout.strip())


def read_duration(path: Path) -> float:
    if path.suffix.casefold() in {".wav", ".wave"}:
        return wav_duration(path)
    return ffprobe_duration(path)


def main() -> int:
    args = parse_args()
    if args.min_seconds > args.max_seconds:
        print("ERROR: minimum duration cannot exceed maximum duration")
        return 1
    try:
        duration = read_duration(args.audio)
    except (OSError, ValueError, RuntimeError, wave.Error) as exc:
        print(f"ERROR: Cannot measure render duration: {exc}")
        return 1

    if not args.min_seconds <= duration <= args.max_seconds:
        print(
            "ERROR: Render duration must be between "
            f"{args.min_seconds:g} and {args.max_seconds:g} seconds; "
            f"found {duration:.3f}"
        )
        return 1

    print(f"RENDER PASS: duration={duration:.3f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
