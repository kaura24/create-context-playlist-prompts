"""Canonical structural vocabulary and fingerprint helpers for validators."""

from __future__ import annotations

from typing import Any


STRUCTURAL_DIMENSIONS = (
    "genre_lane",
    "form_id",
    "section_sequence",
    "recurrence",
    "entry",
    "contrast_peak",
    "transition_interlude",
    "ending",
    "hook_return",
)

HOOK_RETURNS = {
    "No hook",
    "Repeated hook",
    "Varied return",
    "Final-only callback",
    "Instrumental hook",
}

# This is a versioned project contract derived from the official Suno glossary.
# Additions require a coordinated documentation, validator, and regression-test update.
SUPPORTED_SECTIONS = {
    "Intro",
    "Verse",
    "Pre-Chorus",
    "Chorus",
    "Bridge",
    "Outro",
    "Hook",
    "Refrain",
    "Break",
    "Drop",
    "Coda",
}

SELECTION_STATES = {
    "reserved",
    "consumed-by-design",
    "active",
    "finalized",
}


def fingerprint_projection(item: dict[str, Any]) -> dict[str, Any]:
    """Return the complete locked fingerprint without candidate metadata."""

    return {field: item.get(field) for field in STRUCTURAL_DIMENSIONS}
