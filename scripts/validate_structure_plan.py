#!/usr/bin/env python3
"""Validate a genre-conditioned structural candidate pool and ten-slot plan."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from structure_contract import (
    HOOK_RETURNS,
    SELECTION_STATES,
    STRUCTURAL_DIMENSIONS,
    SUPPORTED_SECTIONS,
    fingerprint_projection,
)


MINIMUM_CANDIDATES = 50
TRACK_COUNT = 10
SECTION_MENTION = re.compile(
    r"\b(" + "|".join(re.escape(section) for section in sorted(SUPPORTED_SECTIONS)) + r")\b"
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    return parser.parse_args()


def nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_string_list(
    value: Any, label: str, errors: list[str], *, allow_empty: bool = False
) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{label} must be a list")
        return []
    if not allow_empty and not value:
        errors.append(f"{label} must not be empty")
    if any(not nonempty_string(item) for item in value):
        errors.append(f"{label} must contain only non-empty strings")
        return []
    return value


def canonical(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def fingerprint(candidate: dict[str, Any]) -> tuple[str, ...]:
    return tuple(canonical(candidate.get(field)) for field in STRUCTURAL_DIMENSIONS)


def validate_combination(
    value: Any,
    label: str,
    errors: list[str],
    *,
    allow_partial: bool,
) -> dict[str, Any] | None:
    if not isinstance(value, dict) or not value:
        errors.append(f"{label} must be a non-empty object")
        return None
    unknown = [field for field in value if field not in STRUCTURAL_DIMENSIONS]
    if unknown:
        errors.append(f"{label} has unknown dimensions: {', '.join(unknown)}")
    missing = [field for field in STRUCTURAL_DIMENSIONS if field not in value]
    if missing and not allow_partial:
        errors.append(f"{label} is missing dimensions: {', '.join(missing)}")
    if unknown or (missing and not allow_partial):
        return None
    return value


def matches_partial(candidate: dict[str, Any], rule: dict[str, Any]) -> bool:
    return all(canonical(candidate.get(field)) == canonical(value) for field, value in rule.items())


def validate_requirements(
    requirements: Any,
    items: list[dict[str, Any]],
    label: str,
    errors: list[str],
) -> None:
    if not isinstance(requirements, dict):
        errors.append(f"{label} must be an object")
        return

    missing = [field for field in STRUCTURAL_DIMENSIONS if field not in requirements]
    unknown = [field for field in requirements if field not in STRUCTURAL_DIMENSIONS]
    if missing:
        errors.append(f"{label} is missing dimensions: {', '.join(missing)}")
    if unknown:
        errors.append(f"{label} has unknown dimensions: {', '.join(unknown)}")

    for field in STRUCTURAL_DIMENSIONS:
        required = requirements.get(field)
        if not isinstance(required, int) or isinstance(required, bool) or required < 1:
            errors.append(f"{label}.{field} must be a positive integer")
            continue
        actual = len({canonical(item.get(field)) for item in items})
        if actual < required:
            errors.append(
                f"{label}: {field} requires {required} distinct values; found {actual}"
            )


def validate(plan: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(plan, dict):
        return ["Plan root must be a JSON object"]

    if not nonempty_string(plan.get("genre_coordinate")):
        errors.append("genre_coordinate must be a non-empty string")

    evidence_items = plan.get("evidence")
    if not isinstance(evidence_items, list) or not evidence_items:
        errors.append("evidence must be a non-empty list")
        evidence_items = []
    evidence_ids: set[str] = set()
    for index, item in enumerate(evidence_items, start=1):
        if not isinstance(item, dict):
            errors.append(f"evidence[{index}] must be an object")
            continue
        evidence_id = item.get("id")
        if not nonempty_string(evidence_id):
            errors.append(f"evidence[{index}].id must be a non-empty string")
            continue
        if evidence_id in evidence_ids:
            errors.append(f"duplicate evidence id {evidence_id}")
        evidence_ids.add(evidence_id)
        for field in ("source", "scope"):
            if not nonempty_string(item.get(field)):
                errors.append(f"evidence {evidence_id}.{field} must be a non-empty string")

    def check_evidence_ids(value: Any, label: str) -> list[str]:
        ids = validate_string_list(value, label, errors)
        for evidence_id in ids:
            if evidence_id not in evidence_ids:
                errors.append(f"{label} references unknown evidence id {evidence_id}")
        return ids

    lane_items = plan.get("genre_lanes")
    if not isinstance(lane_items, list) or not lane_items:
        errors.append("genre_lanes must be a non-empty list")
        lane_items = []
    lane_ids: set[str] = set()
    for index, item in enumerate(lane_items, start=1):
        if not isinstance(item, dict):
            errors.append(f"genre_lanes[{index}] must be an object")
            continue
        lane_id = item.get("id")
        if not nonempty_string(lane_id):
            errors.append(f"genre_lanes[{index}].id must be a non-empty string")
            continue
        if lane_id in lane_ids:
            errors.append(f"duplicate genre lane id {lane_id}")
        lane_ids.add(lane_id)
        if not nonempty_string(item.get("label")):
            errors.append(f"genre lane {lane_id}.label must be a non-empty string")
        check_evidence_ids(item.get("evidence_ids"), f"genre lane {lane_id}.evidence_ids")

    envelope_items = plan.get("variation_envelopes")
    if not isinstance(envelope_items, list) or not envelope_items:
        errors.append("variation_envelopes must be a non-empty list")
        envelope_items = []
    envelopes: dict[str, dict[str, Any]] = {}
    envelope_permitted: dict[str, set[str]] = {}
    envelope_forbidden: dict[str, list[dict[str, Any]]] = {}
    for index, item in enumerate(envelope_items, start=1):
        if not isinstance(item, dict):
            errors.append(f"variation_envelopes[{index}] must be an object")
            continue
        envelope_id = item.get("id")
        if not nonempty_string(envelope_id):
            errors.append(f"variation_envelopes[{index}].id must be a non-empty string")
            continue
        if envelope_id in envelopes:
            errors.append(f"duplicate variation envelope id {envelope_id}")
        envelopes[envelope_id] = item
        if item.get("genre_lane") not in lane_ids:
            errors.append(
                f"variation envelope {envelope_id} references unknown genre lane {item.get('genre_lane')}"
            )
        if not nonempty_string(item.get("form_id")):
            errors.append(f"variation envelope {envelope_id}.form_id must be a non-empty string")
        check_evidence_ids(
            item.get("evidence_ids"), f"variation envelope {envelope_id}.evidence_ids"
        )

        permitted_items = item.get("permitted_combinations")
        if not isinstance(permitted_items, list) or not permitted_items:
            errors.append(
                f"variation envelope {envelope_id}.permitted_combinations must be a non-empty list"
            )
            permitted_items = []
        permitted_keys: set[str] = set()
        for combination_index, combination in enumerate(permitted_items, start=1):
            validated = validate_combination(
                combination,
                f"variation envelope {envelope_id}.permitted_combinations[{combination_index}]",
                errors,
                allow_partial=False,
            )
            if validated is None:
                continue
            if validated.get("genre_lane") != item.get("genre_lane"):
                errors.append(
                    f"variation envelope {envelope_id} has a permitted combination with a different genre lane"
                )
            if validated.get("form_id") != item.get("form_id"):
                errors.append(
                    f"variation envelope {envelope_id} has a permitted combination with a different form"
                )
            key = canonical(validated)
            if key in permitted_keys:
                errors.append(
                    f"variation envelope {envelope_id} has a duplicate permitted combination"
                )
            permitted_keys.add(key)
        envelope_permitted[envelope_id] = permitted_keys

        forbidden_items = item.get("forbidden_combinations")
        if not isinstance(forbidden_items, list):
            errors.append(
                f"variation envelope {envelope_id}.forbidden_combinations must be a list"
            )
            forbidden_items = []
        forbidden_rules: list[dict[str, Any]] = []
        for combination_index, combination in enumerate(forbidden_items, start=1):
            validated = validate_combination(
                combination,
                f"variation envelope {envelope_id}.forbidden_combinations[{combination_index}]",
                errors,
                allow_partial=True,
            )
            if validated is not None:
                forbidden_rules.append(validated)
        envelope_forbidden[envelope_id] = forbidden_rules

        for permitted in permitted_items:
            if not isinstance(permitted, dict):
                continue
            for forbidden in forbidden_rules:
                if matches_partial(permitted, forbidden):
                    errors.append(
                        f"variation envelope {envelope_id} permits a forbidden structural combination"
                    )

    pool = plan.get("candidate_pool")
    if not isinstance(pool, dict):
        errors.append("candidate_pool must be an object")
        pool = {}
    minimum_count = pool.get("minimum_count")
    if (
        not isinstance(minimum_count, int)
        or isinstance(minimum_count, bool)
        or minimum_count < MINIMUM_CANDIDATES
    ):
        errors.append(f"candidate_pool.minimum_count must be at least {MINIMUM_CANDIDATES}")
        minimum_count = MINIMUM_CANDIDATES

    candidate_items = pool.get("candidates")
    if not isinstance(candidate_items, list):
        errors.append("candidate_pool.candidates must be a list")
        candidate_items = []
    if len(candidate_items) < minimum_count:
        errors.append(
            f"candidate_pool must contain at least {minimum_count} candidates; found {len(candidate_items)}"
        )

    candidates: dict[str, dict[str, Any]] = {}
    fingerprints: dict[tuple[str, ...], str] = {}
    for index, item in enumerate(candidate_items, start=1):
        if not isinstance(item, dict):
            errors.append(f"candidate_pool.candidates[{index}] must be an object")
            continue
        candidate_id = item.get("candidate_id")
        if not nonempty_string(candidate_id):
            errors.append(f"candidate_pool.candidates[{index}].candidate_id must be non-empty")
            continue
        if candidate_id in candidates:
            errors.append(f"duplicate candidate id {candidate_id}")
        candidates[candidate_id] = item

        lane_id = item.get("genre_lane")
        if lane_id not in lane_ids:
            errors.append(f"candidate {candidate_id} references unknown genre lane {lane_id}")
        if not nonempty_string(item.get("form_id")):
            errors.append(f"candidate {candidate_id}.form_id must be non-empty")

        envelope_id = item.get("envelope_id")
        envelope = envelopes.get(envelope_id)
        if envelope is None:
            errors.append(f"candidate {candidate_id} references unknown envelope {envelope_id}")
        else:
            if item.get("genre_lane") != envelope.get("genre_lane"):
                errors.append(f"candidate {candidate_id} genre lane does not match {envelope_id}")
            if item.get("form_id") != envelope.get("form_id"):
                errors.append(f"candidate {candidate_id} form does not match {envelope_id}")
        candidate_evidence = check_evidence_ids(
            item.get("evidence_ids"), f"candidate {candidate_id}.evidence_ids"
        )
        if envelope is not None:
            outside_evidence = set(candidate_evidence) - set(envelope.get("evidence_ids", []))
            if outside_evidence:
                errors.append(
                    f"candidate {candidate_id} cites evidence outside envelope {envelope_id}: "
                    + ", ".join(sorted(outside_evidence))
                )

        sequence = item.get("section_sequence")
        sections = validate_string_list(
            sequence, f"candidate {candidate_id}.section_sequence", errors
        )
        for section in sections:
            if section not in SUPPORTED_SECTIONS:
                errors.append(
                    f"candidate {candidate_id} uses unsupported Suno section {section}"
                )
        for field in (
            "recurrence",
            "entry",
            "contrast_peak",
            "transition_interlude",
            "ending",
            "hook_return",
        ):
            if not nonempty_string(item.get(field)):
                errors.append(f"candidate {candidate_id}.{field} must be non-empty")
            for mentioned in SECTION_MENTION.findall(str(item.get(field, ""))):
                if mentioned not in sections:
                    errors.append(
                        f"candidate {candidate_id}.{field} mentions absent section {mentioned}"
                    )
        if item.get("hook_return") not in HOOK_RETURNS:
            errors.append(f"candidate {candidate_id} has unsupported hook_return")

        for count, section in re.findall(
            r"\b(\d+)\s+(" + "|".join(re.escape(name) for name in sorted(SUPPORTED_SECTIONS))
            + r")\s+occurrence\(s\)",
            str(item.get("recurrence", "")),
        ):
            actual_count = sections.count(section)
            if actual_count != int(count):
                errors.append(
                    f"candidate {candidate_id}.recurrence reports {count} {section} occurrence(s); "
                    f"sequence has {actual_count}"
                )

        projection = fingerprint_projection(item)
        if envelope is not None:
            if canonical(projection) not in envelope_permitted.get(envelope_id, set()):
                errors.append(
                    f"candidate {candidate_id} is not a permitted complete combination in envelope {envelope_id}"
                )
            for forbidden in envelope_forbidden.get(envelope_id, []):
                if matches_partial(projection, forbidden):
                    errors.append(
                        f"candidate {candidate_id} matches a forbidden combination in envelope {envelope_id}"
                    )

        key = fingerprint(item)
        if key in fingerprints:
            errors.append(
                "duplicate structural fingerprint for candidates "
                f"{fingerprints[key]} and {candidate_id}"
            )
        else:
            fingerprints[key] = candidate_id

    validate_requirements(
        pool.get("dimension_requirements"),
        list(candidates.values()),
        "candidate_pool.dimension_requirements",
        errors,
    )

    contract = plan.get("selection_contract")
    if not isinstance(contract, dict):
        errors.append("selection_contract must be an object")
        contract = {}
    if contract.get("track_count") != TRACK_COUNT:
        errors.append(f"selection_contract.track_count must equal {TRACK_COUNT}")

    allocation_items = contract.get("envelope_allocations")
    if not isinstance(allocation_items, list) or not allocation_items:
        errors.append("selection_contract.envelope_allocations must be a non-empty list")
        allocation_items = []
    allocations: dict[str, int] = {}
    for index, item in enumerate(allocation_items, start=1):
        if not isinstance(item, dict):
            errors.append(f"envelope_allocations[{index}] must be an object")
            continue
        envelope_id = item.get("envelope_id")
        count = item.get("track_count")
        if envelope_id not in envelopes:
            errors.append(f"envelope allocation references unknown envelope {envelope_id}")
            continue
        if envelope_id in allocations:
            errors.append(f"duplicate envelope allocation {envelope_id}")
        if not isinstance(count, int) or isinstance(count, bool) or count < 1:
            errors.append(f"envelope allocation {envelope_id}.track_count must be positive")
            continue
        allocations[envelope_id] = count
    if sum(allocations.values()) != TRACK_COUNT:
        errors.append(f"envelope allocation counts must sum to {TRACK_COUNT}")

    selection_items = plan.get("selections")
    if not isinstance(selection_items, list):
        errors.append("selections must be a list")
        selection_items = []
    if len(selection_items) != TRACK_COUNT:
        errors.append(f"selections must contain exactly {TRACK_COUNT} rows")

    tracks: list[int] = []
    slot_ids: set[str] = set()
    selected_ids: set[str] = set()
    selected_candidates: list[dict[str, Any]] = []
    selected_envelopes: Counter[str] = Counter()
    selected_states: Counter[str] = Counter()
    for index, item in enumerate(selection_items, start=1):
        if not isinstance(item, dict):
            errors.append(f"selections[{index}] must be an object")
            continue
        track = item.get("track")
        if not isinstance(track, int) or isinstance(track, bool):
            errors.append(f"selections[{index}].track must be an integer")
        else:
            tracks.append(track)
        slot_id = item.get("slot_id")
        if not nonempty_string(slot_id):
            errors.append(f"selections[{index}].slot_id must be non-empty")
        elif slot_id in slot_ids:
            errors.append(f"duplicate slot id {slot_id}")
        else:
            slot_ids.add(slot_id)

        candidate_id = item.get("candidate_id")
        if candidate_id in selected_ids:
            errors.append(f"candidate {candidate_id} is selected more than once")
        elif nonempty_string(candidate_id):
            selected_ids.add(candidate_id)
        candidate = candidates.get(candidate_id)
        if candidate is None:
            errors.append(f"selection {slot_id} references unknown candidate {candidate_id}")
        else:
            selected_candidates.append(candidate)
            selected_envelopes[candidate.get("envelope_id")] += 1

            locked_fingerprint = item.get("locked_fingerprint")
            if not isinstance(locked_fingerprint, dict):
                errors.append(f"selection {slot_id}.locked_fingerprint must be an object")
            elif canonical(locked_fingerprint) != canonical(fingerprint_projection(candidate)):
                errors.append(
                    f"selection {slot_id}.locked_fingerprint does not match candidate {candidate_id}"
                )

        open_axes = validate_string_list(
            item.get("open_axes"), f"selection {slot_id}.open_axes", errors, allow_empty=True
        )
        for axis in open_axes:
            if axis in STRUCTURAL_DIMENSIONS:
                errors.append(f"selection {slot_id} opens locked structural axis {axis}")
        state = item.get("state")
        if state not in SELECTION_STATES:
            errors.append(
                f"selection {slot_id}.state must be one of {', '.join(sorted(SELECTION_STATES))}"
            )
        else:
            selected_states[state] += 1
        if state != "reserved":
            form_flow = item.get("main_prompt_form_flow")
            if not nonempty_string(form_flow):
                errors.append(
                    f"selection {slot_id}.main_prompt_form_flow is required after reservation"
                )
            elif re.search(r"\[[^\]\n]+\]", form_flow):
                errors.append(
                    f"selection {slot_id}.main_prompt_form_flow must use plain prose without bracketed tags"
                )

    if sorted(tracks) != list(range(1, TRACK_COUNT + 1)):
        errors.append(f"selection tracks must be exactly 1 through {TRACK_COUNT}")
    for envelope_id, expected in allocations.items():
        actual = selected_envelopes.get(envelope_id, 0)
        if actual != expected:
            errors.append(
                f"envelope allocation {envelope_id} requires {expected} tracks; found {actual}"
            )
    for envelope_id in selected_envelopes.keys() - allocations.keys():
        errors.append(f"selected envelope {envelope_id} has no envelope allocation")
    if selected_states.get("active", 0) > 1:
        errors.append("selections may contain at most one active slot")

    validate_requirements(
        contract.get("dimension_requirements"),
        selected_candidates,
        "selection_contract.dimension_requirements",
        errors,
    )
    return errors


def main() -> int:
    args = parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"ERROR: unable to read plan: {error}")
        return 1

    errors = validate(plan)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    candidate_count = len(plan["candidate_pool"]["candidates"])
    states = Counter(item["state"] for item in plan["selections"])
    state_summary = ", ".join(f"{state}={states.get(state, 0)}" for state in sorted(SELECTION_STATES))
    print(
        f"PASS: {candidate_count} genre-valid candidates; "
        f"{TRACK_COUNT} structural slots ({state_summary})"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
