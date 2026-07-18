#!/usr/bin/env python3
"""Validate a ten-track PlaylistSpec from catalog through bound TrackSpecs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from validate_structure_plan import TRACK_COUNT, validate as validate_structure_plan
from validate_track_output import validate_spec


PLAYLIST_KEYS = {
    "schema_version",
    "catalog_revision",
    "playlist_contract",
    "structure_plan",
    "tracks",
}
CONTRACT_KEYS = {
    "use_case",
    "common_sound",
    "variation_pool",
    "drift_boundaries",
}
BOUND_TRACK_KEYS = {
    "track_id",
    "slot_id",
    "candidate_id",
    "locked_fingerprint",
    "spec",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("playlist", type=Path)
    parser.add_argument(
        "--catalog",
        type=Path,
        required=True,
        help="Versioned genre structure catalog JSON",
    )
    return parser.parse_args()


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def signature_is_encoded(signature: Any, prompt_text: str) -> bool:
    if not isinstance(signature, str):
        return False
    parts = [" ".join(part.casefold().split()) for part in signature.split("|")]
    haystack = " ".join(prompt_text.casefold().split())
    return len(parts) == 3 and all(part and part in haystack for part in parts)


def validate_exact_keys(
    value: Any,
    expected: set[str],
    label: str,
    errors: list[str],
) -> bool:
    if not isinstance(value, dict):
        errors.append(f"{label} must be an object")
        return False
    missing = sorted(expected - set(value))
    unknown = sorted(set(value) - expected)
    if missing:
        errors.append(f"{label} is missing keys: {', '.join(missing)}")
    if unknown:
        errors.append(f"{label} has unknown keys: {', '.join(unknown)}")
    return not missing and not unknown


def validate(
    playlist: Any,
    catalog: Any,
) -> tuple[list[str], dict[int, dict[str, Any]]]:
    errors: list[str] = []
    tracks_by_id: dict[int, dict[str, Any]] = {}
    if not validate_exact_keys(playlist, PLAYLIST_KEYS, "PlaylistSpec", errors):
        return errors, tracks_by_id

    if playlist.get("schema_version") != "1.0":
        errors.append("PlaylistSpec schema_version must equal 1.0")
    if playlist.get("catalog_revision") != (
        catalog.get("catalog_revision") if isinstance(catalog, dict) else None
    ):
        errors.append("PlaylistSpec catalog_revision does not match catalog")

    contract = playlist.get("playlist_contract")
    if validate_exact_keys(contract, CONTRACT_KEYS, "playlist_contract", errors):
        for key in CONTRACT_KEYS:
            if not nonempty_string(contract.get(key)):
                errors.append(f"playlist_contract.{key} must be a non-empty string")

    structure_plan = playlist.get("structure_plan")
    structure_errors = validate_structure_plan(structure_plan, catalog)
    errors.extend(f"structure_plan: {error}" for error in structure_errors)
    if not isinstance(structure_plan, dict):
        return errors, tracks_by_id

    selections = structure_plan.get("selections")
    selection_by_track = {
        selection.get("track"): selection
        for selection in selections
        if isinstance(selection, dict)
    } if isinstance(selections, list) else {}

    tracks = playlist.get("tracks")
    if not isinstance(tracks, list):
        errors.append("PlaylistSpec tracks must be a list")
        return errors, tracks_by_id
    if len(tracks) != TRACK_COUNT:
        errors.append(f"PlaylistSpec must contain exactly {TRACK_COUNT} bound tracks")

    seen_ids: set[int] = set()
    seen_titles: set[str] = set()
    seen_harmony: set[str] = set()
    for index, track in enumerate(tracks, start=1):
        label = f"tracks[{index}]"
        if not validate_exact_keys(track, BOUND_TRACK_KEYS, label, errors):
            continue
        track_id = track.get("track_id")
        if not isinstance(track_id, int) or isinstance(track_id, bool):
            errors.append(f"{label}.track_id must be an integer")
            continue
        if track_id in seen_ids:
            errors.append(f"duplicate track_id {track_id}")
        seen_ids.add(track_id)
        tracks_by_id[track_id] = track

        selection = selection_by_track.get(track_id)
        if selection is None:
            errors.append(f"track {track_id} has no structure-plan selection")
            continue
        for field in ("slot_id", "candidate_id"):
            if track.get(field) != selection.get(field):
                errors.append(f"track {track_id} {field} does not match selection")
        if canonical(track.get("locked_fingerprint")) != canonical(
            selection.get("locked_fingerprint")
        ):
            errors.append(
                f"track {track_id} locked_fingerprint does not match selection"
            )
        if selection.get("state") == "reserved":
            errors.append(
                f"track {track_id} has a compiled TrackSpec but its slot cannot remain reserved"
            )

        spec = track.get("spec")
        spec_errors: list[str] = []
        normalized = validate_spec(spec, spec_errors) if isinstance(spec, dict) else None
        if not isinstance(spec, dict):
            spec_errors.append("TrackSpec must be an object")
        errors.extend(f"track {track_id}: {error}" for error in spec_errors)
        if normalized is None:
            continue

        title = normalized.get("title")
        if nonempty_string(title):
            if title in seen_titles:
                errors.append(f"duplicate TrackSpec title {title}")
            seen_titles.add(title)

        actual_sequence = [
            section["tag"] for section in normalized.get("sections", [])
        ]
        expected_sequence = (
            track.get("locked_fingerprint", {}).get("section_sequence")
            if isinstance(track.get("locked_fingerprint"), dict)
            else None
        )
        if actual_sequence != expected_sequence:
            errors.append(
                f"track {track_id} section sequence does not match locked fingerprint"
            )

        fields = normalized.get("prompt_fields", {})
        harmony = fields.get("Harmony")
        if isinstance(harmony, str):
            harmony_key = " ".join(harmony.casefold().split())
            if harmony_key in seen_harmony:
                errors.append(f"track {track_id} duplicates another TrackSpec Harmony field")
            seen_harmony.add(harmony_key)
        expected_flow = selection.get("main_prompt_form_flow")
        if fields.get("Form/Flow") != expected_flow:
            errors.append(f"track {track_id} Form/Flow does not match selected slot")
        fingerprint = track.get("locked_fingerprint")
        if isinstance(fingerprint, dict):
            opening_text = " ".join(
                str(fields.get(field, "")) for field in ("Instrumentation", "Form/Flow")
            )
            if not signature_is_encoded(fingerprint.get("entry"), opening_text):
                errors.append(
                    f"track {track_id} prompt does not encode locked entry signature"
                )
            if not signature_is_encoded(
                fingerprint.get("groove_signature"),
                str(fields.get("Tempo/Groove", "")),
            ):
                errors.append(
                    f"track {track_id} prompt does not encode locked groove signature"
                )

    if sorted(seen_ids) != list(range(1, TRACK_COUNT + 1)):
        errors.append(f"PlaylistSpec track_ids must be exactly 1 through {TRACK_COUNT}")
    return errors, tracks_by_id


def load_json(path: Path, label: str) -> tuple[Any | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except (OSError, json.JSONDecodeError) as error:
        return None, f"unable to read {label}: {error}"


def load_and_validate(
    playlist_path: Path,
    catalog_path: Path,
) -> tuple[list[str], dict[int, dict[str, Any]]]:
    playlist, playlist_error = load_json(playlist_path, "PlaylistSpec")
    catalog, catalog_error = load_json(catalog_path, "catalog")
    errors = [error for error in (playlist_error, catalog_error) if error]
    if errors:
        return errors, {}
    validation_errors, tracks = validate(playlist, catalog)
    return errors + validation_errors, tracks


def main() -> int:
    args = parse_args()
    errors, tracks = load_and_validate(args.playlist, args.catalog)
    if errors:
        for error in dict.fromkeys(errors):
            print(f"ERROR: {error}")
        return 1
    print(
        f"PLAYLIST PASS: {len(tracks)} bound tracks; "
        "catalog, slots, TrackSpecs, sections, and Form/Flow agree"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
