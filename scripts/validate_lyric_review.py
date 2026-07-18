#!/usr/bin/env python3
"""Validate a fresh, evidence-backed lyric content review against exact lyrics."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any


CRITERIA = (
    "design_traceability",
    "field_routing",
    "musical_coherence",
    "title_narrative_hook",
    "language_singability",
    "structure_completion",
    "main_vs_exclusion",
    "playlist_fit_differentiation",
    "premise_and_causality",
    "narrative_verisimilitude",
    "scene_and_timeline_continuity",
    "speaker_addressee_consistency",
    "line_level_semantics",
)
CONTENT_CRITERIA = CRITERIA[-5:]
MANDATORY_TWO = {
    "design_traceability",
    "field_routing",
    "structure_completion",
    *CONTENT_CRITERIA,
}
TOP_LEVEL_KEYS = {
    "schema_version",
    "track_id",
    "reviewer",
    "independent",
    "lyrics_sha256",
    "criteria",
    "contradictions",
    "verisimilitude_breaks",
    "unexplained_images",
    "status",
}
LYRICS_BLOCK = re.compile(
    r"(?ms)^\*\*가사\*\*\s*\n```text\s*\n(?P<lyrics>.*?)\n```\s*$"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("review", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--track", type=int, required=True)
    return parser.parse_args()


def read_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"Cannot read review JSON: {exc}")
        return None


def extract_lyrics(path: Path, errors: list[str]) -> str:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"Cannot read track output: {exc}")
        return ""
    match = LYRICS_BLOCK.search(text)
    if not match:
        errors.append("Cannot find exact Lyrics text block in track output")
        return ""
    return match.group("lyrics")


def validate_review(
    review: Any, lyrics: str, expected_track: int, errors: list[str]
) -> tuple[int, str]:
    if not isinstance(review, dict):
        errors.append("Review must be a JSON object")
        return 0, "unknown"

    missing = sorted(TOP_LEVEL_KEYS - set(review))
    unknown = sorted(set(review) - TOP_LEVEL_KEYS)
    if missing:
        errors.append("Review is missing keys: " + ", ".join(missing))
    if unknown:
        errors.append("Review has unknown keys: " + ", ".join(unknown))

    if review.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if review.get("track_id") != expected_track:
        errors.append(f"track_id must match --track {expected_track}")
    reviewer = review.get("reviewer")
    if not isinstance(reviewer, str) or not reviewer.strip():
        errors.append("reviewer must be a non-empty string")
        reviewer = "unknown"
    if review.get("independent") is not True:
        errors.append("independent must be true")

    expected_hash = hashlib.sha256(lyrics.encode("utf-8")).hexdigest()
    if review.get("lyrics_sha256") != expected_hash:
        errors.append("lyrics_sha256 does not match the current Lyrics block")

    for field in ("contradictions", "verisimilitude_breaks", "unexplained_images"):
        value = review.get(field)
        if not isinstance(value, list):
            errors.append(f"{field} must be a list")
        elif value:
            errors.append(f"{field} must be empty before content review can pass")

    criteria = review.get("criteria")
    total = 0
    if not isinstance(criteria, dict):
        errors.append("criteria must be an object")
    else:
        missing_criteria = sorted(set(CRITERIA) - set(criteria))
        unknown_criteria = sorted(set(criteria) - set(CRITERIA))
        if missing_criteria:
            errors.append("criteria is missing: " + ", ".join(missing_criteria))
        if unknown_criteria:
            errors.append("criteria has unknown keys: " + ", ".join(unknown_criteria))

        for name in CRITERIA:
            item = criteria.get(name)
            if not isinstance(item, dict) or set(item) != {"score", "evidence"}:
                errors.append(f"{name} must contain exactly score and evidence")
                continue
            score = item.get("score")
            evidence = item.get("evidence")
            if not isinstance(score, int) or isinstance(score, bool) or score not in {0, 1, 2}:
                errors.append(f"{name}.score must be 0, 1, or 2")
                continue
            total += score
            if name in MANDATORY_TWO and score != 2:
                errors.append(f"{name} must score 2")
            elif score == 0:
                errors.append(f"{name} cannot score 0")

            minimum_evidence = 3 if name == "line_level_semantics" else 2 if name in CONTENT_CRITERIA else 1
            if (
                not isinstance(evidence, list)
                or len(evidence) < minimum_evidence
                or any(not isinstance(entry, str) or not entry.strip() for entry in evidence)
            ):
                errors.append(
                    f"{name} requires at least {minimum_evidence} evidence items"
                )

    if total < 23:
        errors.append(f"semantic score is {total}/26; minimum is 23/26")
    if review.get("status") != "PASS":
        errors.append("status must be PASS")
    return total, str(reviewer)


def main() -> int:
    args = parse_args()
    errors: list[str] = []
    review = read_json(args.review, errors)
    lyrics = extract_lyrics(args.output, errors)
    total, reviewer = validate_review(review, lyrics, args.track, errors)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        f"LYRIC CONTENT PASS: track={args.track}, score={total}/26, "
        f"reviewer={reviewer}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
