---
name: create-context-playlist-prompts
description: Create, test, and revise cohesive 10-track Suno playlist plans, canonical TrackSpec manifests, paste-ready basic prompts, absolute-exclusion prompts, and complete 3-4 minute lyrics with the title outside the lyric block. Use for context-led playlists, prompt or song references, vocalist and production continuity, Track 1 pilots, batch track production, generated-audio diagnosis, duration verification, targeted revisions, resets, and project history.
---

# Create Context Playlist Prompts

Create original songs that preserve only high-level reference traits. Design new melodies, hooks, chord progressions, lyrics, and signature parts.

## Autonomy Contract

Produce a useful artifact in the first response whenever the request contains enough direction to make safe defaults.

- Treat explicit user facts as fixed.
- Fill noncritical gaps with a reversible assumption and list it in an Assumption Ledger.
- Ask one concise question only when conflicting core requirements, ownership or upload permission, or an irreplaceable choice would materially change the result.
- Use a single design checkpoint. In the default fast mode, make it informational and continue to the Track 1 pilot in the same response. Pause there only when the user requests approval-sensitive work.
- Treat missing research as a confidence limit, not a workflow blocker. Use literal observed structure, label provisional claims, and continue without invented citations.
- Keep drafting later tracks when render evidence is unavailable. Mark them draft-validated and reserve render-verified for listened audio.

## Read Only What The Task Needs

- New playlist, reset, or revision state: [workflow](references/workflow.md)
- Ten-track map, form, harmony, duration, and vocal design: [design rules](references/design-rules.md)
- TrackSpec and exact user-facing fields: [output contract](references/output-contract.md)
- Suno field routing and supported vocabulary: [Suno style guide](references/suno-style-guide.md)
- Semantic scoring, audio diagnosis, and render verification: [quality and render protocol](references/quality-and-render-protocol.md)

## Run The Default Path

1. Extract Context, reference roles, language, lead-vocal identity, central genre, absolute exclusions, and requested delivery scope.
2. Record only material inferred values in the Assumption Ledger.
3. Create a concise Playlist Contract and exactly 10 differentiated track rows.
4. Create the canonical TrackSpec for Track 1 before writing prose output.
5. Compile one Basic Prompt from the TrackSpec's eight ordered prompt fields.
6. Write one Absolute Exclusion Prompt, one title outside all code blocks, and one complete Lyrics block.
7. Validate the complete set. Repair deterministic failures internally, with a maximum of three full validation attempts.
8. Label the result PLAN PASS or draft-validated. Continue with the requested tracks without waiting unless the user selected listen-each-track mode.

## Keep One Canonical TrackSpec

Store title, language, BPM, metrical pulses per bar, target duration, ordered sections with bars and vocal flags, all eight prompt_fields, and exclusion_prompt in the TrackSpec. Recompile from it after revisions; do not stitch old prose fragments together.

Plan every song for 180-240 seconds. Prefer a 195-225 second center to absorb generation variance. Calculate:

    planned seconds = total bars × metrical pulses per bar × 60 / BPM

Treat lyric-volume checks as duration readiness, not proof of actual runtime. Write every repeated lyric in full and supply enough vocal lines and language-specific lyric units for the planned vocal bars. Confirm actual duration only from a rendered audio file.

## Compile One Paste-Ready Track Set

Treat TrackSpec as the single source of truth. Compile the Basic Prompt deterministically from its eight prompt_fields. Keep the title outside every fenced block so Title, Styles, Exclude, and Lyrics can be pasted into separate Suno fields.

Use these Basic Prompt fields exactly once and in this order:

1. Style
2. Feel
3. Tempo/Groove
4. Vocal
5. Instrumentation
6. Harmony
7. Form/Flow
8. Production/Mix

Keep the Basic Prompt at 800 characters or fewer and the Absolute Exclusion Prompt at 100 characters or fewer. Put positive audible direction in Basic Prompt, only unusable traits in Absolute Exclusion Prompt, and only structural tags plus complete lyrics in Lyrics. Emit exactly three fenced `text` blocks under `**기본프롬프트**`, `**절대불가프롬프트**`, and `**가사**`; place the title between the second and third fields as `### <title>`.

## Revise Narrowly

Default feedback scope to track-local. Promote a rule to playlist-lock only when the user explicitly applies it broadly or repeated render evidence supports it. Recompile only affected fields, then validate the whole current-track set. Preserve unaffected tracks and history.

Treat an explicit playlist or project reset as a full active-state reset while preserving archived history. Treat a current-track rewrite as local.

## Verify Before Delivery

When a shell is available, run:

    python3 <skill-dir>/scripts/validate_track_output.py <draft.md> --spec <track-spec.json>

For supplied rendered audio, also run:

    python3 <skill-dir>/scripts/validate_render.py <render-file>

Apply the semantic rubric in the quality protocol after PLAN PASS. Never claim audible quality, language delivery, mix quality, or actual 3-4 minute runtime without render evidence.
