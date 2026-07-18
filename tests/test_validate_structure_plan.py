from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_structure_plan.py"
FINGERPRINT_FIELDS = (
    "genre_lane",
    "form_id",
    "section_sequence",
    "recurrence",
    "entry",
    "groove_signature",
    "contrast_peak",
    "transition_interlude",
    "ending",
    "hook_return",
)


def project(candidate: dict[str, object]) -> dict[str, object]:
    return {field: candidate[field] for field in FINGERPRINT_FIELDS}


def valid_catalog_and_plan() -> tuple[dict[str, object], dict[str, object]]:
    profiles = (
        ("central", "verse-refrain", "V1", "E1"),
        ("central", "chorus-led", "V2", "E2"),
        ("adjacent", "through-composed", "V3", "E3"),
    )
    candidates: list[dict[str, object]] = []
    for number in range(1, 51):
        genre_lane, form_id, envelope_id, _evidence_id = profiles[(number - 1) % 3]
        optional_sections = (
            "Verse",
            "Pre-Chorus",
            "Chorus",
            "Bridge",
            "Break",
            "Refrain",
        )
        sequence = ["Intro"] + [
            section
            for bit, section in enumerate(optional_sections)
            if number & (1 << bit)
        ] + ["Outro"]
        candidates.append(
            {
                "candidate_id": f"C{number:03d}",
                "genre_lane": genre_lane,
                "form_id": form_id,
                "envelope_id": envelope_id,
                "evidence_ids": ["E1", "E2", "E3"],
                "section_sequence": sequence,
                "recurrence": f"return-pattern-{number:02d}",
                "entry": f"lead-{number:02d} | gesture-{number:02d} | vocal-bar-{number:02d}",
                "groove_signature": f"pulse-{number:02d} | accent-{number:02d} | support-{number:02d}",
                "contrast_peak": f"peak-{(number - 1) % 7 + 1}",
                "transition_interlude": f"transition-{(number - 1) % 4 + 1}",
                "ending": f"ending-{(number - 1) % 6 + 1}",
                "hook_return": "Repeated hook" if number % 2 else "Varied return",
            }
        )

    envelopes: list[dict[str, object]] = []
    for envelope_id, lane, form_id, _evidence_id in (
        ("V1", "central", "verse-refrain", "E1"),
        ("V2", "central", "chorus-led", "E2"),
        ("V3", "adjacent", "through-composed", "E3"),
    ):
        envelopes.append(
            {
                "id": envelope_id,
                "genre_lane": lane,
                "form_id": form_id,
                "evidence_ids": ["E1", "E2", "E3"],
                "permitted_combinations": [
                    project(candidate)
                    for candidate in candidates
                    if candidate["envelope_id"] == envelope_id
                ],
                "forbidden_combinations": [],
            }
        )

    catalog: dict[str, object] = {
        "catalog_revision": "test-catalog-v1",
        "genre_coordinate": "Korean 2020s indie neo-soul, slow pocket",
        "evidence": [
            {
                "id": "E1",
                "source": "https://example.com/form-entry",
                "kind": "real-song",
                "artist": "Artist One",
                "track": "Song One",
                "scope": "central form and entry",
            },
            {
                "id": "E2",
                "source": "https://example.com/contrast-peak",
                "kind": "real-song",
                "artist": "Artist Two",
                "track": "Song Two",
                "scope": "central contrast and peak",
            },
            {
                "id": "E3",
                "source": "https://example.com/adjacent-pattern",
                "kind": "real-song",
                "artist": "Artist Three",
                "track": "Song Three",
                "scope": "adjacent ending and return",
            },
        ],
        "genre_lanes": [
            {
                "id": "central",
                "label": "central neo-soul",
                "evidence_ids": ["E1", "E2"],
            },
            {
                "id": "adjacent",
                "label": "approved adjacent art-soul",
                "evidence_ids": ["E3"],
            },
        ],
        "variation_envelopes": envelopes,
        "diversity_contract": {
            "candidate_minimums": {
                "genre_lane": 2,
                "form_id": 3,
                "section_sequence": 50,
                "recurrence": 50,
                "entry": 50,
                "groove_signature": 50,
                "contrast_peak": 7,
                "transition_interlude": 4,
                "ending": 6,
                "hook_return": 2,
            },
            "selection_minimums": {
                "genre_lane": 2,
                "form_id": 3,
                "section_sequence": 10,
                "recurrence": 10,
                "entry": 10,
                "groove_signature": 10,
                "contrast_peak": 7,
                "transition_interlude": 4,
                "ending": 6,
                "hook_return": 2,
            },
            "minimum_candidate_distance": 3,
            "minimum_selection_distance": 3,
        },
    }

    selections = []
    for number in range(1, 11):
        candidate = candidates[number - 1]
        selections.append(
            {
                "track": number,
                "slot_id": f"S{number:02d}",
                "candidate_id": candidate["candidate_id"],
                "reference_bindings": [
                    {
                        "role": "structure",
                        "evidence_id": "E1",
                        "distilled_trait": "Long verse followed by a compact return",
                    },
                    {
                        "role": "harmony",
                        "evidence_id": "E2",
                        "distilled_trait": "Slow harmonic rhythm with suspended cadences",
                    },
                    {
                        "role": "emotional_arc",
                        "evidence_id": "E3",
                        "distilled_trait": "Withheld feeling resolves in the final image",
                    },
                ],
                "locked_fingerprint": project(candidate),
                "open_axes": ["section density curve"],
                "state": "reserved",
            }
        )

    plan: dict[str, object] = {
        "catalog_revision": "test-catalog-v1",
        "candidate_pool": {
            "minimum_count": 50,
            "candidates": candidates,
        },
        "selection_contract": {
            "track_count": 10,
            "envelope_allocations": [
                {"envelope_id": "V1", "track_count": 4},
                {"envelope_id": "V2", "track_count": 3},
                {"envelope_id": "V3", "track_count": 3},
            ],
        },
        "selections": selections,
    }
    return catalog, plan


class StructurePlanValidatorTests(unittest.TestCase):
    def run_validator(
        self,
        catalog: dict[str, object],
        plan: dict[str, object],
    ) -> subprocess.CompletedProcess[str]:
        with (
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as plan_handle,
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as catalog_handle,
        ):
            json.dump(plan, plan_handle)
            plan_handle.flush()
            json.dump(catalog, catalog_handle)
            catalog_handle.flush()
            return subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    plan_handle.name,
                    "--catalog",
                    catalog_handle.name,
                ],
                capture_output=True,
                check=False,
                text=True,
            )

    def test_accepts_catalog_bound_fifty_candidate_plan(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("50 catalog-bound candidates; 10 structural slots", result.stdout)

    def test_rejects_catalog_revision_mismatch(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        plan["catalog_revision"] = "wrong-revision"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("catalog_revision does not match", result.stdout)

    def test_rejects_evidence_without_url_or_user_approval(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        evidence = catalog["evidence"]
        assert isinstance(evidence, list)
        evidence[0]["source"] = "source-1"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("must be an http(s) URL or user: approval", result.stdout)

    def test_selected_slots_require_three_role_bound_real_song_references(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        plan["selections"][0].pop("reference_bindings")
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("reference_bindings must contain exactly 3 rows", result.stdout)

        catalog, plan = valid_catalog_and_plan()
        catalog["evidence"][0]["source"] = "user:approved-reference"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("evidence E1 must resolve to an HTTP(S) source", result.stdout)

        catalog, plan = valid_catalog_and_plan()
        candidate_id = plan["selections"][0]["candidate_id"]
        candidate = next(
            row
            for row in plan["candidate_pool"]["candidates"]
            if row["candidate_id"] == candidate_id
        )
        candidate["evidence_ids"].remove("E2")
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("evidence E2 is not cited by candidate", result.stdout)

    def test_rejects_duplicate_or_missing_reference_roles(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        bindings = plan["selections"][0]["reference_bindings"]
        bindings[2]["role"] = "harmony"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("roles must be exactly emotional_arc, harmony, structure", result.stdout)

    def test_rejects_duplicate_reference_songs_and_empty_distillation(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        bindings = plan["selections"][0]["reference_bindings"]
        bindings[1]["evidence_id"] = "E1"
        bindings[2]["distilled_trait"] = ""
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("must use 3 distinct evidence IDs", result.stdout)
        self.assertIn("distilled_trait must be non-empty", result.stdout)

    def test_rejects_reference_without_real_song_identity(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        catalog["evidence"][0].pop("artist")
        catalog["evidence"][1]["kind"] = "article"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("evidence E1 must name a real song with artist and track", result.stdout)
        self.assertIn("evidence E2 must have kind real-song", result.stdout)

    def test_rejects_duplicate_song_or_source_under_different_evidence_ids(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        catalog["evidence"][1]["source"] = catalog["evidence"][0]["source"]
        catalog["evidence"][2]["artist"] = catalog["evidence"][0]["artist"]
        catalog["evidence"][2]["track"] = catalog["evidence"][0]["track"]
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("must use 3 distinct source URLs", result.stdout)
        self.assertIn("must use 3 distinct real songs", result.stdout)

    def test_rejects_candidate_pool_below_fifty(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        pool["candidates"] = candidates[:49]
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("at least 50 candidates", result.stdout)

    def test_rejects_superficial_recurrence_only_candidates(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        for candidate in candidates:
            candidate.update(
                section_sequence=["Intro", "Verse", "Chorus", "Outro"],
                entry="same-entry",
                contrast_peak="same-peak",
                transition_interlude="same-transition",
                ending="same-ending",
                hook_return="Repeated hook",
            )
        envelopes = catalog["variation_envelopes"]
        assert isinstance(envelopes, list)
        for envelope in envelopes:
            envelope["permitted_combinations"] = [
                project(candidate)
                for candidate in candidates
                if candidate["envelope_id"] == envelope["id"]
            ]
        selections = plan["selections"]
        assert isinstance(selections, list)
        by_id = {candidate["candidate_id"]: candidate for candidate in candidates}
        for selection in selections:
            selection["locked_fingerprint"] = project(
                by_id[selection["candidate_id"]]
            )
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("structural distance", result.stdout)

    def test_catalog_owns_dimension_minimums(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        contract = catalog["diversity_contract"]
        assert isinstance(contract, dict)
        minimums = contract["selection_minimums"]
        assert isinstance(minimums, dict)
        minimums["entry"] = 51
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("entry requires 51 distinct values", result.stdout)

    def test_rejects_duplicate_candidate_fingerprint(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        duplicate = deepcopy(candidates[0])
        duplicate["candidate_id"] = "C002"
        candidates[1] = duplicate
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicate structural fingerprint", result.stdout)

    def test_rejects_candidate_outside_catalog_envelope(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["section_sequence"] = ["Drop", "Coda"]
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("not a permitted complete combination", result.stdout)

    def test_rejects_selection_with_wrong_locked_fingerprint(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        selections = plan["selections"]
        assert isinstance(selections, list)
        fingerprint = selections[0]["locked_fingerprint"]
        assert isinstance(fingerprint, dict)
        fingerprint["ending"] = "wrong-ending"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("locked_fingerprint does not match", result.stdout)

    def test_rejects_malformed_opening_or_groove_signature(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["entry"] = "only one opening clause"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("entry must contain exactly 3 pipe-separated clauses", result.stdout)

        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        assert isinstance(pool, dict)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        candidates[0]["groove_signature"] = "pulse | accent"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn(
            "groove_signature must contain exactly 3 pipe-separated clauses",
            result.stdout,
        )

    def test_rejects_selected_signatures_differing_on_only_one_axis(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        pool = plan["candidate_pool"]
        selections = plan["selections"]
        assert isinstance(pool, dict) and isinstance(selections, list)
        candidates = pool["candidates"]
        assert isinstance(candidates, list)
        first = candidates[0]
        second = candidates[1]
        second["entry"] = "other-lead | gesture-01 | vocal-bar-01"
        second["groove_signature"] = "other-pulse | accent-01 | support-01"
        envelopes = catalog["variation_envelopes"]
        assert isinstance(envelopes, list)
        for envelope in envelopes:
            envelope["permitted_combinations"] = [
                project(candidate)
                for candidate in candidates
                if candidate["envelope_id"] == envelope["id"]
            ]
        selections[1]["locked_fingerprint"] = project(second)
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 1)
        self.assertIn("opening signatures must differ on at least 2 of 3 axes", result.stdout)
        self.assertIn("groove signatures must differ on at least 2 of 3 axes", result.stdout)

    def test_accepts_post_design_lifecycle_snapshot(self) -> None:
        catalog, plan = valid_catalog_and_plan()
        selections = plan["selections"]
        assert isinstance(selections, list)
        selections[0]["state"] = "active"
        selections[0]["main_prompt_form_flow"] = "approved active flow"
        selections[1]["state"] = "finalized"
        selections[1]["main_prompt_form_flow"] = "approved finalized flow"
        result = self.run_validator(catalog, plan)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
