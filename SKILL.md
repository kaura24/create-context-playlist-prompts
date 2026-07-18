---
name: create-context-playlist-prompts
description: Create, test, and revise cohesive 10-track Suno playlists from versioned genre-structure catalogs, pools of at least 50 structurally distinct candidates, three role-bound real-song web references per track, and one bound PlaylistSpec. Compile paste-ready prompts, exclusions, and complete 3-4 minute lyrics with Suno section tags only in Lyrics and the title outside every code block. Use for context-led playlists, Track 1 pilots, batch production, audio diagnosis, revision, resets, and project history.
---

# Create Context Playlist Prompts

Create original songs that preserve only high-level reference traits. Design new melodies, hooks, chord progressions, lyrics, and signature parts.

## Autonomy Contract

Produce a useful artifact in the first response whenever the request contains enough direction to make safe defaults.

- Treat explicit user facts as fixed.
- Fill noncritical gaps with a reversible assumption and list it in an Assumption Ledger.
- Resolve missing language, dynamic-profile, and percussion-role choices with one concise combined question before research; otherwise question only conflicting core requirements, ownership or upload permission, or an irreplaceable choice.
- Use a single design checkpoint. In the default fast mode, make it informational and continue to the Track 1 pilot in the same response. Pause there only when the user requests approval-sensitive work.
- Treat missing research or render evidence as confidence limits, not workflow blockers. Use literal observed structure, keep drafting, label provisional claims, and reserve render-verified for listened audio.

## Read Only What The Task Needs

- New playlist, reset, or revision state: [workflow](references/workflow.md)
- Ten-track map, form, harmony, duration, and vocal design: [design rules](references/design-rules.md)
- PlaylistSpec, TrackSpec, and exact user-facing fields: [output contract](references/output-contract.md)
- Suno field routing and supported vocabulary: [Suno style guide](references/suno-style-guide.md)
- Semantic scoring, audio diagnosis, and render verification: [quality and render protocol](references/quality-and-render-protocol.md)

## Resolve Language, Dynamics, And Percussion Role Before Research, Then Run The Default Path

1. Extract Context, references, exact language policy, lead identity, arrangement dynamics, percussion role, vocal high-note policy, hook-prominence policy, genre, exclusions, and scope; resolve missing required values, then ledger only other inferences.
2. Browse the web for the current genre and shortlist real, existing songs from reliable, inspectable sources.
3. Generate at least 50 permitted candidates, reserve exactly 10, and bind exactly three distinct real songs to every slot as `structure`, `harmony`, and `emotional_arc`; choose exactly one of the three as the hook-melody model, record every distilled trait, then apply any requested seeded hook-prominence shuffle without changing locked structure.
4. Create one PlaylistSpec that binds all 10 reserved slots to all 10 TrackSpecs before compiling any playlist track.
5. Validate the PlaylistSpec, then compile the requested track from its bound TrackSpec.
6. Emit one Basic Prompt, one Absolute Exclusion Prompt, one outside title, and one complete Lyrics block. Validate them in playlist-bound mode.
7. Repair deterministic failures internally, with a maximum of three full validation attempts, then label the result PLAN PASS or draft-validated.

## Keep One Canonical PlaylistSpec

For a 10-track playlist, PlaylistSpec is the single source of truth. It contains the Playlist Contract, validated StructurePlan, and exactly 10 slot-bound TrackSpecs. Each binding repeats `slot_id`, `candidate_id`, and `locked_fingerprint`; its TrackSpec section sequence and plain-prose `Form/Flow` must match the selected slot. A standalone TrackSpec is allowed only for an explicit single-track request.

Each nested TrackSpec stores title, language, BPM, metrical pulses per bar, target duration, ordered sections with bars and vocal flags, all eight `prompt_fields`, and `exclusion_prompt`. Recompile from it after revisions; do not stitch old prose fragments together.
Plan every song for 180-240 seconds. Prefer a 195-225 second center to absorb generation variance. Calculate:

    planned seconds = total bars × metrical pulses per bar × 60 / BPM

Treat lyric-volume checks as duration readiness, not proof of actual runtime. Write every repeated lyric in full and supply enough vocal lines and language-specific lyric units for the planned vocal bars. Confirm actual duration only from a rendered audio file.

## Enforce Structural Diversity For Every Playlist

Before every 10-track playlist, research real, existing songs on the web and build the structural plan from a separately versioned catalog. Every final slot must carry `reference_bindings` with exactly three distinct candidate-cited songs: one each for `structure`, `harmony`, and `emotional_arc`. Each binding records a nonempty `distilled_trait`; each evidence record uses `kind: real-song`, artist, track, and an HTTP(S) source. Do not use `user:` approval as a final reference.

Record at least 50 evidence-linked candidate fingerprints across approved genre lanes, then reserve exactly 10 candidates that meet catalog-owned distinct-value and pairwise-distance minimums. A fingerprint contains genre lane, form, exact section sequence, recurrence, opening signature, groove signature, contrast/peak, transition/interlude, ending, and hook-return behavior. Encode each signature as exactly three pipe-separated clauses and require every selected pair to differ on at least two of three axes; groove variation must retain support-only percussion when locked. Distill only high-level traits: section logic from the structure song, tonal-center behavior, harmonic rhythm, cadence, bass motion, and color from the harmony song, and tension-turn-release logic from the emotional-arc song. From the named hook-melody model, extract only motif length, contour class, rhythmic cell, title placement, and return pattern; compose a new note sequence and lyric stress pattern, never its actual melody. Synthesize them into a new design. All 10 `Harmony` fields must be distinct. Never copy melody, hook, exact progression, lyrics, signature riff, or source-specific imagery.

Each variation envelope must enumerate its permitted complete fingerprint combinations and any forbidden partial combinations. Do not treat a Cartesian product of separately plausible options as valid. Each reserved slot must copy its candidate as `locked_fingerprint`; after design it may move through `reserved`, `consumed-by-design`, `active`, and `finalized` with an approved plain-prose `main_prompt_form_flow`.

Run the catalog, plan, and playlist validators in order. Do not compile a playlist track until all 10 bindings pass. Use plain prose in `Form/Flow`; put bracketed Suno structural tags only in Lyrics, never in the Basic Prompt or Exclusion Prompt, and keep the title outside every code block.

## Compile One Paste-Ready Track Set

Compile the Basic Prompt deterministically from the bound TrackSpec's eight `prompt_fields`. Keep the title outside every fenced block so Title, Styles, Exclude, and Lyrics can be pasted into separate Suno fields.

Use these Basic Prompt fields exactly once and in this order:

1. Style
2. Feel
3. Tempo/Groove
4. Vocal
5. Instrumentation
6. Harmony
7. Form/Flow
8. Production/Mix

Target 800 characters or fewer for the Basic Prompt; allow a 100-character grace and fail only above 900. Keep the Absolute Exclusion Prompt at 100 characters or fewer. Put positive audible direction in Basic Prompt, only unusable traits in Absolute Exclusion Prompt, and only structural tags plus complete lyrics in Lyrics. Emit exactly three fenced `text` blocks under `**기본프롬프트**`, `**절대불가프롬프트**`, and `**가사**`; place the title between the second and third fields as `### <title>`.

## Revise Narrowly

Default feedback scope to track-local. Promote a rule to playlist-lock only when the user explicitly applies it broadly or repeated render evidence supports it. Recompile only affected fields, then validate the whole current-track set. Preserve unaffected tracks and history.

Treat an explicit playlist or project reset as a full active-state reset while preserving archived history. Treat a current-track rewrite as local.

## Verify Before Delivery

For a 10-track playlist, run:

    python3 <skill-dir>/scripts/validate_structure_plan.py <plan.json> --catalog <catalog.json>
    python3 <skill-dir>/scripts/validate_playlist_spec.py <playlist-spec.json> --catalog <catalog.json>
    python3 <skill-dir>/scripts/validate_track_output.py <draft.md> --playlist <playlist-spec.json> --catalog <catalog.json> --track <N>

For an explicit single-track request only, run:

    python3 <skill-dir>/scripts/validate_track_output.py <draft.md> --spec <track-spec.json>

For supplied rendered audio, also run:

    python3 <skill-dir>/scripts/validate_render.py <render-file>

After PLAN PASS, create a fresh independent review JSON and run `python3 <skill-dir>/scripts/validate_lyric_review.py <review.json> --output <draft.md> --track <N>` before `draft-validated`. Never claim audible quality, language delivery, mix quality, or actual runtime without render evidence.
