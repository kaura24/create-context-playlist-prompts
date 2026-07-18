from __future__ import annotations

import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tests.test_validate_structure_plan import valid_catalog_and_plan


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_playlist_spec.py"
MAIN_FIELDS = (
    "Style",
    "Feel",
    "Tempo/Groove",
    "Vocal",
    "Instrumentation",
    "Harmony",
    "Form/Flow",
    "Production/Mix",
)
INSTRUMENTAL_TAGS = {"Intro", "Outro", "Break", "Drop", "Coda"}


def valid_playlist_spec() -> tuple[dict[str, object], dict[str, object]]:
    catalog, plan = valid_catalog_and_plan()
    candidates = plan["candidate_pool"]["candidates"]
    selections = plan["selections"]
    by_id = {candidate["candidate_id"]: candidate for candidate in candidates}
    tracks: list[dict[str, object]] = []

    for selection in selections:
        candidate = by_id[selection["candidate_id"]]
        flow = f"Locked catalog flow for track {selection['track']}"
        selection["state"] = (
            "active" if selection["track"] == 1 else "consumed-by-design"
        )
        selection["main_prompt_form_flow"] = flow
        sequence = candidate["section_sequence"]
        sections = [
            {
                "tag": tag,
                "bars": 8,
                "vocal": tag not in INSTRUMENTAL_TAGS,
            }
            for tag in sequence
        ]
        total_bars = sum(section["bars"] for section in sections)
        bpm = total_bars * 4 * 60 / 210
        prompt_fields = dict(
            zip(
                MAIN_FIELDS,
                (
                    "Korean catalog-bound soul pop",
                    f"Distinct scene {selection['track']}; steady motion",
                    f"{bpm:.2f} BPM, 4/4; relaxed pocket",
                    "One Korean alto; stable formants and clear consonants",
                    f"Unique instrument role {selection['track']}; compact drums",
                    f"Original progression family {selection['track']}; clear cadence",
                    flow,
                    f"Mix profile {selection['track']}; centered lead and short room",
                ),
                strict=True,
            )
        )
        tracks.append(
            {
                "track_id": selection["track"],
                "slot_id": selection["slot_id"],
                "candidate_id": selection["candidate_id"],
                "locked_fingerprint": copy.deepcopy(
                    selection["locked_fingerprint"]
                ),
                "spec": {
                    "title": f"Track {selection['track']}",
                    "language": "ko",
                    "target_duration_seconds": 210,
                    "bpm": bpm,
                    "metrical_pulses_per_bar": 4,
                    "sections": sections,
                    "prompt_fields": prompt_fields,
                    "exclusion_prompt": "metallic vocals, trap hats",
                },
            }
        )

    playlist = {
        "schema_version": "1.0",
        "catalog_revision": plan["catalog_revision"],
        "playlist_contract": {
            "use_case": "rainy-night reading",
            "common_sound": "warm Korean soul-pop with one alto lead",
            "variation_pool": "catalog-bound structure, harmony, and instruments",
            "drift_boundaries": "Korean lyrics; no unrelated genre jumps",
        },
        "structure_plan": plan,
        "tracks": tracks,
    }
    return catalog, playlist


class PlaylistSpecValidatorTests(unittest.TestCase):
    def run_validator(
        self,
        catalog: dict[str, object],
        playlist: dict[str, object],
    ) -> subprocess.CompletedProcess[str]:
        with (
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as playlist_handle,
            tempfile.NamedTemporaryFile(
                "w", encoding="utf-8", suffix=".json"
            ) as catalog_handle,
        ):
            json.dump(playlist, playlist_handle, ensure_ascii=False)
            playlist_handle.flush()
            json.dump(catalog, catalog_handle, ensure_ascii=False)
            catalog_handle.flush()
            return subprocess.run(
                [
                    sys.executable,
                    str(VALIDATOR),
                    playlist_handle.name,
                    "--catalog",
                    catalog_handle.name,
                ],
                capture_output=True,
                check=False,
                text=True,
            )

    def assert_rejected(
        self,
        playlist: dict[str, object],
        message: str,
        catalog: dict[str, object] | None = None,
    ) -> None:
        valid_catalog, _ = valid_playlist_spec()
        result = self.run_validator(catalog or valid_catalog, playlist)
        self.assertEqual(result.returncode, 1, result.stdout + result.stderr)
        self.assertIn(message, result.stdout)

    def test_accepts_ten_bound_track_specs(self) -> None:
        catalog, playlist = valid_playlist_spec()
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PLAYLIST PASS: 10 bound tracks", result.stdout)

    def test_rejects_playlist_without_structure_plan(self) -> None:
        catalog, playlist = valid_playlist_spec()
        del playlist["structure_plan"]
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("missing keys: structure_plan", result.stdout)

    def test_rejects_missing_or_extra_track(self) -> None:
        catalog, playlist = valid_playlist_spec()
        playlist["tracks"] = playlist["tracks"][:9]
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("exactly 10 bound tracks", result.stdout)

    def test_rejects_slot_or_candidate_mismatch(self) -> None:
        catalog, playlist = valid_playlist_spec()
        playlist["tracks"][0]["slot_id"] = "S99"
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("slot_id does not match selection", result.stdout)

        catalog, playlist = valid_playlist_spec()
        playlist["tracks"][0]["candidate_id"] = "C050"
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("candidate_id does not match selection", result.stdout)

    def test_rejects_locked_fingerprint_mismatch(self) -> None:
        catalog, playlist = valid_playlist_spec()
        playlist["tracks"][0]["locked_fingerprint"]["ending"] = "wrong"
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("locked_fingerprint does not match selection", result.stdout)

    def test_rejects_trackspec_section_sequence_mismatch(self) -> None:
        catalog, playlist = valid_playlist_spec()
        playlist["tracks"][0]["spec"]["sections"][1]["tag"] = "Hook"
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("section sequence does not match locked fingerprint", result.stdout)

    def test_rejects_form_flow_mismatch(self) -> None:
        catalog, playlist = valid_playlist_spec()
        playlist["tracks"][0]["spec"]["prompt_fields"]["Form/Flow"] = "Different flow"
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("Form/Flow does not match selected slot", result.stdout)

    def test_rejects_duplicate_harmony_plans(self) -> None:
        catalog, playlist = valid_playlist_spec()
        first_harmony = playlist["tracks"][0]["spec"]["prompt_fields"]["Harmony"]
        playlist["tracks"][1]["spec"]["prompt_fields"]["Harmony"] = first_harmony
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("duplicates another TrackSpec Harmony field", result.stdout)

    def test_rejects_reserved_slot_with_compiled_trackspec(self) -> None:
        catalog, playlist = valid_playlist_spec()
        playlist["structure_plan"]["selections"][0]["state"] = "reserved"
        del playlist["structure_plan"]["selections"][0]["main_prompt_form_flow"]
        result = self.run_validator(catalog, playlist)
        self.assertEqual(result.returncode, 1)
        self.assertIn("cannot remain reserved", result.stdout)


if __name__ == "__main__":
    unittest.main()
