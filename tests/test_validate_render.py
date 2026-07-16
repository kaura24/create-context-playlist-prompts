from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
import wave
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "scripts" / "validate_render.py"


class RenderValidatorTests(unittest.TestCase):
    def run_validator(self, duration_seconds: int) -> subprocess.CompletedProcess[str]:
        with tempfile.NamedTemporaryFile(suffix=".wav") as handle:
            with wave.open(handle.name, "wb") as audio:
                audio.setnchannels(1)
                audio.setsampwidth(1)
                audio.setframerate(1)
                audio.writeframes(b"\x80" * duration_seconds)
            return subprocess.run(
                [sys.executable, str(VALIDATOR), handle.name],
                capture_output=True,
                check=False,
                text=True,
            )

    def test_accepts_render_duration_boundaries(self) -> None:
        for duration in (180, 240):
            with self.subTest(duration=duration):
                result = self.run_validator(duration)
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
                self.assertIn("RENDER PASS", result.stdout)

    def test_rejects_render_outside_duration_boundaries(self) -> None:
        for duration in (179, 241):
            with self.subTest(duration=duration):
                result = self.run_validator(duration)
                self.assertEqual(result.returncode, 1)
                self.assertIn("must be between 180 and 240 seconds", result.stdout)


if __name__ == "__main__":
    unittest.main()
