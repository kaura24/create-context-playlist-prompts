---
name: create-context-playlist-prompts
description: Design cohesive 10-track, reference-led playlists and complete Suno main prompts, exclusion prompts, and synchronized title/lyrics for all ten tracks through a track-by-track listening, revision, and approval cycle. Use for situation-specific playlists, prompt-form reference parsing, related-song discovery, reference-song style translation, vocalist consistency, adjacent-genre variation, user-supplied audio target matching, failed-render diagnosis, prompt revision, playlist reset, or project history tracking.
---

# Create Context Playlist Prompts

Preserve the reference's high-level musical identity, but newly design the melody, hooks, exact chord progression, lyrics, and signature riffs. Get approval for the full 10-track design, then complete Tracks 1-10 through controlled three-prompt listening and approval cycles.

## Read The Required References

- New playlist and full design: [references/design-rules.md](references/design-rules.md), [references/structure-patterns.md](references/structure-patterns.md), [references/output-contract.md](references/output-contract.md). Read all three before drafting the 10-track table.
- Current-track compilation: [references/suno-style-guide.md](references/suno-style-guide.md), [references/output-contract.md](references/output-contract.md), [references/vocal-audio-engineering-protocol.md](references/vocal-audio-engineering-protocol.md). Read all three before outputting the current track's controlled prompt set.
- Prompt-shaped references such as `Hard constraints` and `Style`: [references/prompt-reference-protocol.md](references/prompt-reference-protocol.md)
- Audio files, generated renders, and "make it feel like this" comparisons: [references/audio-reference-protocol.md](references/audio-reference-protocol.md)
- Vocal naturalness, AI-like vocal symptoms, A/B/C sound comparison, and mix engineering: [references/vocal-audio-engineering-protocol.md](references/vocal-audio-engineering-protocol.md)
- Revision, regeneration, reset, and common-requirement propagation: [references/revision-protocol.md](references/revision-protocol.md)

## Convert Prompt-Shaped References Into Seeds First

When the user provides a reference prompt that combines `Hard constraints`, `Style`, tempo, vocal, instrumentation, and exclusions, do not use it directly as a finished output or as approved constraints. First decompose it into a seed design that separates explicit values from inferred values, then research and recommend real related songs, then interview the user about the desired mood in batches of 1-2 questions. Do not finalize recommended songs as Primary or Supporting references until the user selects them. At this stage, do not output the 10-track design or any final Main Prompt, Exclusion Prompt, or Title And Lyrics.

Reference candidates and final selected songs must come only from `English-language pop songs`, `Japanese-language songs`, or `Korean-language songs`, classified by the primary lyric language. The same song may be reused across analysis axes, reference roles, and playlist tracks. However, two tracks' harmony-reference lists must not overlap by 50% or more. Follow the classification and calculation rules in [references/prompt-reference-protocol.md](references/prompt-reference-protocol.md).

## 1. Separate Work State From Evidence Roles

Keep the following roles explicit and do not mix them.

- `Primary reference`: the main axis for style and musical grammar
- `Supporting references`: songs that support harmony or arrangement judgment
- `Target render`: an output audio render the user has approved as "like this"
- `Rejected render`: a failed result used only to extract failure causes, not to imitate
- `Context`: weather, time, place, activity, emotion, and other listening situations
- `Approved constraints`: user-approved rules for vocal, language, exclusions, length, and similar constraints

Prioritize the user's latest explicit instruction. Keep the Primary reference as the default style axis, but when the user provides a Target render, apply that audio first for the disputed audible traits. Mark unverifiable musical facts as inferences.

## 2. Do Not Ask What Has Already Been Answered

Organize country/region, era, market/cultural zone, macro-genre, subgenre, tempo/groove, language, and production grammar hierarchically. Ask only about blanks that would materially change the result, and ask only 1-2 questions at a time. Treat the user's free-form descriptions as confirmed input.

Always keep the following scopes separate.

- `Energy`: relative playlist momentum, levels 3, 4, and 5
- `Arrangement dynamics`: section-level loudness, density, drum intensity, and layer movement
- `Vocal emotional depth`: the emotional depth conveyed by the vocal
- `Vocal lowest note`: the lowest note in the lead vocal melody

If the user defines dynamics as "emotional depth and vocal lowest note," apply only that definition. Do not expand it into flattened arrangement, no chorus lift, no fills, or no layer growth. Only constrain arrangement dynamics separately when the user explicitly asks for that.

## 3. Get Approval For Reference DNA, Form Evidence, Playlist Contract, Vocal Design, And Engineering

From the references, extract genre grammar, era feel, tempo range, groove, vocal phrasing, instrument roles, production density, and space. Present the high-level traits to preserve separately from the lower-level elements to newly design. Use real artist and song names only as analysis evidence, never in the generation prompt.

Approve the research contracts in dependency order rather than as one bundled decision: Genre And Reference DNA, Playlist Sound Contract, Form Evidence And Variation Envelopes, Vocal And Engineering Contract, then Initial Harmony Candidate Pool. Ask for no more than 1-2 decisions at a time. When an approved upstream contract changes, revalidate only its dependent downstream artifacts and preserve unaffected approvals.

Translate the Context into a concise `Playlist sound contract` with four parts: listening use case, Common sound, Track variation pool, and Drift boundaries. Treat the use case as a shared audible function, not as a substitute for genre. Get approval for this contract before designing the 10 tracks.

Before designing track structures, use [references/structure-patterns.md](references/structure-patterns.md) to research and get approval for the genre's Form Evidence Table and each form's Permitted Variation Envelope. Use only established sources, verified real-song structures, or forms explicitly supplied and approved by the user. Never invent, rename, or assume a form. If no established name is verified, preserve only the literal observed sequence and its limited evidence scope.

Offer 1-3 virtual lead vocal candidates for the user to choose from. If the user specifies one vocalist, keep exactly that one lead across all tracks and do not create additional IDs or alternate leads. Each track has a single lead; background chorus and harmony are allowed within the approved scope. Get approval for the vocal's range, lowest note, timbre, power, pronunciation, phrasing, emotional depth, and forbidden traits.

Use [references/vocal-audio-engineering-protocol.md](references/vocal-audio-engineering-protocol.md) to approve a Vocal And Engineering Contract. Translate vague feedback such as `AI-like voice` into audible symptoms involving identity, performance, pronunciation, capture, mix, or generation artifacts. Use those symptoms as controlled A/B/C axes and update the contract from every listening round.

## 4. Separate The Full Design From Actual Outputs

Create the full design table for exactly 10 tracks at once. Keep the approved Common sound, central genre, adjacent genres, and tempo zone while giving every track a clear differentiator. For each row, select only an approved evidence-backed form or literal sequence, keep its invariants, and write the exact sequence, Structural Flow Contract, Lyrics tag sequence, and development signature inside its Permitted Variation Envelope. Then design the new section-level chord progression and draw a compatible hook strategy using [references/design-rules.md](references/design-rules.md). Do not choose a hook before the structure it must serve.

Do not impose a universal quota for form count or reuse. Follow the approved genre evidence even when one form recurs. Create differences only through the form's permitted sequence, repeat, entry, contrast, peak, and ending ranges plus track-specific instruments, drums, harmony, and narrative. Each track must stand alone while serving the shared use case. Before the full design is approved, do not create actual prompts or lyrics.

After approval, start with Track 1 and process one track per approval cycle. For each track, output exactly:

1. `Main Prompt A`, `Main Prompt B`, and `Main Prompt C`: three controlled alternatives, each primarily English and at most 800 characters
2. `Exclusion Prompt`: one shared set of absolute prohibitions, at most 100 characters
3. `Title And Lyrics`: one shared approved title and complete lyric containing the exact approved bracketed tags such as `[Verse]` and `[Chorus]`

Keep title, lyrics, shared Exclusion Prompt, exact Lyrics tag sequence, lead-vocal identity, language, absolute constraints, and central genre fixed across A/B/C. Treat the shared Lyrics tag sequence as a common scaffold, not as a demand for identical musical realization. Keep feel, harmony, form development, Structural Flow, arrangement, and production similar rather than identical within their approved envelopes, while varying only 1-2 declared axes. This similarity envelope makes those fields eligible for bounded variation; it does not require every eligible field to change in every round. Keep non-test-axis fields semantically at the approved baseline and do not rewrite them merely to create artificial difference. State the controlled differences briefly in Korean.

Wait for the user to generate and listen to the three versions. Record which Main Prompt is closest and which audible traits worked or failed. Classify every correction as `track-local`, `next-track-only`, `remaining-common`, or `project-global`. A chosen A/B/C preference defaults to `remaining-common` unless it depends on the current track's unique design or the user narrows its scope. Store scoped entries in the `Calibration Lock`; expire `next-track-only` after the next track is approved, and never revise an approved track without explicit user instruction. If none is acceptable, create a new controlled set of three Main Prompts while preserving the shared Exclusion Prompt and Title And Lyrics unless the feedback targets those fields. Continue until all ten tracks have approved final results.

Follow the format and checking gates in [references/output-contract.md](references/output-contract.md).

## 5. Compile The Current Track's Controlled Prompt Set Atomically

Do not stitch old sentences together. Write the current track's three Main Prompt alternatives, one shared Exclusion Prompt, and one shared Title And Lyrics from the approved design and latest requirements. Apply the public platform contract in [references/suno-style-guide.md](references/suno-style-guide.md) to field routing and wording, and apply the private project contract from the user's latest instructions, approved design, cumulative Calibration Lock, and this skill to the actual musical content and operating limits. Validate A/B/C as a controlled comparison and validate the track against approved tracks and the remaining 10-track plan.

Compile the Main Prompt in this order.

1. `Style:` country, era, market, and central/adjacent genre
2. `Feel:` listening use case, emotional tone, arousal, brightness/darkness, and sense of motion
3. `Tempo/Groove:` BPM, meter, pocket, and rhythmic feel
4. `Vocal:` the single lead's range, timbre, phrasing, pronunciation, emotional depth, and naturalness target
5. `Instrumentation:` instrument roles, register, texture, and arrangement behavior
6. `Harmony:` the new section-level chord progression, mode/color, cadence, and bass motion
7. `Form/Flow:` the approved form, section functions, buildup/release path, hook return, peak, and ending in plain prose
8. `Production/Mix:` mic distance, room, stereo placement, transients, dynamics, tonal balance, and processing
9. Necessary positive guardrails that would break the result if omitted

Compile the Exclusion Prompt separately from only the absolute prohibited styles, instruments, vocal traits, performance behaviors, or mix traits. Keep it at 100 characters or fewer, including spaces and punctuation. Do not count it toward the Main Prompt's 800-character limit. Route positive requirements from a source `Hard constraints` section into the Main Prompt and route explicit prohibitions into the Exclusion Prompt.

Do not place title, lyric lines, artist/song names, citations, absolute prohibitions, or bracketed Lyrics tags such as `[Verse]` or `[Chorus]` in any Main Prompt. A plain structural phrase such as `restrained chorus lift` is allowed; the bracketed `[Chorus]` header belongs only inside Title And Lyrics.

If positive wording in the Main Prompt would induce a trait prohibited by the Exclusion Prompt, remove or replace the conflicting positive wording instead of adding more exclusions. If the user says to remove a concept entirely because mentioning it induces the unwanted result, delete that concept from both prompts and describe only the desired replacement. Do not duplicate exclusions across both prompts.

## 6. Diagnose Revisions Before Regenerating

When there is a failed result, do not revise by guessing from the prompt alone. First classify the difference between the approved design and the actual result. If the user has already described the cause and goal specifically, revise without additional interview. Ask 1-2 diagnostic questions only when the issue is ambiguous.

For revisions, rebuild all three Main Prompt alternatives when the comparison axis or audible target changes. Rebuild the shared Exclusion Prompt or Title And Lyrics only when feedback targets that field, but always revalidate the entire current-track set. Do not provide partial patches, add-on sentences, or diffs. Apply each approved correction only according to its recorded scope and expiry; do not alter already approved tracks unless the user asks.

## 7. Treat Reset As A Full Reset

When the user explicitly says `reset`, `full reset`, `complete reset`, `project reset`, or `playlist reset`, do not treat it as current-track regeneration. Preserve only the history, and clear all active Context, the Playlist sound contract, form evidence, variation envelopes, Structural Flow Contracts, Lyrics tag sequences, Vocal And Engineering Contract, Calibration Lock, all reference roles, Target/Rejected renders, Approved constraints, genre/language/vocal/voicing, common rules, 10-track design and approval, selected revision track, and all result sets.

After reset, restart with the initial interview for a new project. When enough high-level inputs are gathered, present exactly 10 tracks in a new full design table and wait for approval. Before approval, do not output any final Main Prompt, Exclusion Prompt, or Title And Lyrics.

`Redesign the current track from scratch` is not a reset; it is a track-level full regeneration. Do not confuse the two. Follow the detailed state transitions in [references/revision-protocol.md](references/revision-protocol.md).

## 8. Complete Checks And Records

If the controlled-comparison, current-track, or cross-track check fails, do not reveal the result. Internally redesign and rerun all checks. After every track's three Main Prompts, wait for comparative listening feedback, approve one direction, and update the Calibration Lock; do not generate the next track automatically. Keep the completion ledger until all ten tracks have approved final results.

When a shell and scratch file are available, draft the complete current-track output in a temporary Markdown file and run `python3 <this-skill-directory>/scripts/validate_track_output.py <draft-file> --expected-tags <comma-separated-approved-tag-sequence>`. Do not reveal or copy the draft into the response until the validator passes. If it fails, rewrite the complete set and rerun it; never patch only the reported fragment. When no shell is available, apply the same checks manually and target 650-700 Main Prompt characters for margin.

When a workspace is available, use `PROJECT_HISTORY.md` as the index and `history/YYYY-MM-DD__topic-slug.md` as the detailed record. Accumulate approved designs, Main Prompt A/B/C versions, the chosen Main Prompt, shared Exclusion Prompt and Title And Lyrics versions, audible feedback, Calibration Lock updates, failure causes, check results, and state. Do not overwrite prior versions.
