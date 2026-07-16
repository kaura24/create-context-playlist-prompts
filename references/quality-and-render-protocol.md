# Quality And Render Protocol

Separate deterministic correctness, semantic quality, and audible evidence. Passing one level never implies the next.

## Use Five Evidence Labels

| Label | Evidence |
|---|---|
| planned | TrackSpec exists but has not passed validation |
| PLAN PASS | TrackSpec and compiled text pass deterministic checks |
| draft-validated | PLAN PASS plus a passing semantic quality score |
| render-duration-verified | Supplied audio metadata is 180-240 seconds |
| render-verified | Duration and the semantic listening rubric pass |

Continue drafting after PLAN PASS when audio is unavailable. State the evidence boundary instead of turning it into a serial blocker.

## Run Deterministic Checks

Use validate_track_output.py with TrackSpec. Treat these as hard failures:

- malformed or contradictory TrackSpec
- planned duration outside 180-240 seconds
- missing requested code block, outside title, field, section, tag, or vocal lyrics
- prompt or exclusion character overflow
- Basic Prompt text that does not compile exactly from TrackSpec
- placeholder or repeat shorthand
- clear selected-language mismatch

Repair these internally before delivery. Keep uncertain lyric density and mixed-language nuance conservative; do not claim precise sung timing from text alone.

## Score Semantic Quality

After PLAN PASS, score each item from 0 to 2:

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Design traceability | contradicts TrackSpec | partial | every major choice traces |
| Field routing and output contract | mixed or malformed | minor leak | three clean paste-ready fields and outside title |
| Musical coherence | conflicting | usable | form, harmony, groove, and mix reinforce |
| Title, narrative, and hook | generic or inconsistent | serviceable | distinctive and aligned |
| Language and singability | broken | uneven | natural, performable phrasing |
| Structure and lyric completion | incomplete | minor weakness | complete and bar-aware |
| Main versus Exclusion | conflict | redundant | clean field separation |
| Playlist fit and differentiation | off-contract | weak distinction | cohesive and clearly differentiated |

Require at least 13 of 16, no zero, and a score of 2 for design traceability, field routing and output contract, and structure and lyric completion. Use a fresh independent reviewer when available. Revise the canonical TrackSpec or affected field, then rescore.

This score tests prompt and lyric quality. It does not prove the generator will follow every instruction.

## Measure Render Duration

For a supplied WAV, MP3, M4A, FLAC, or other ffprobe-readable file, run:

    python3 scripts/validate_render.py render-file

Accept 180.000 through 240.000 seconds inclusive. Record measured duration. A bar plan near 195-225 seconds provides useful variance margin but does not replace this measurement.

## Review Audible Quality

Listen to the full file before assigning render-verified. Record:

| Axis | Match, partial, mismatch, or unknown | Evidence |
|---|---|---|
| Last planned lyric completes |  |  |
| Lead identity and register stability |  |  |
| Pronunciation and phrase timing |  |  |
| Basic Prompt choices are audible |  |  |
| Absolute-exclusion traits are absent |  |  |
| Form, peak, return, and ending follow TrackSpec |  |  |
| Instrument and groove roles fit |  |  |
| Space, transients, tone, and low end fit |  |  |
| Context and playlist use case fit |  |  |

Do not infer an audible match from a prompt or filename.

## Diagnose Artificial Vocals Precisely

Separate:

- identity: range, register, timbre, and formant stability
- performance: breath, onset, pitch motion, vibrato, melisma, and endings
- language: consonants, vowels, stress, accent, and timing
- capture: mic distance, dryness, room, proximity, and noise
- mix: compression, sibilance, saturation, EQ, ambience, and stereo
- generation artifacts: metallic resonance, formant wobble, timbre jumps, smeared consonants, phasey doubling, or clipped breaths

Record the heard symptom, desired opposite, evidence level, proposed positive direction, possible Exclusion term, and affected TrackSpec field. Revise one causal axis at a time.

## Handle Audio Roles

- Primary reference: overall style grammar
- Supporting reference: one bounded design axis
- Target render: positive audible target for named traits
- Rejected render: counterexample used only for diagnosis

Prioritize a Target render for the disputed audible trait while preserving the Playlist Contract elsewhere. Never claim to have listened when only metadata or a user description is available.

## Batch Calibration Safely

The user may return several renders together. Measure and review them in a batch, update track-local overrides first, and promote only repeated or explicitly broad findings to playlist-lock. Keep later draft production independent from missing render evidence.
