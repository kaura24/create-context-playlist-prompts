---
name: create-context-playlist-prompts
description: Design cohesive 10-track, reference-led playlists and generate one compact Suno style prompt plus synchronized lyrics at a time. Use for situation-specific playlists, prompt-form reference parsing, related-song discovery, reference-song style translation, vocalist consistency, adjacent-genre variation, user-supplied audio target matching, failed-render diagnosis, prompt revision, playlist reset, or project history tracking.
---

# Create Context Playlist Prompts

Preserve the reference's high-level musical identity, but newly design the melody, hooks, exact chord progression, lyrics, and signature riffs. Get approval for the full 10-track design first, then provide the actual Suno Prompt and Lyrics one track at a time.

## Read The Required References

- New playlist and full design: [references/design-rules.md](references/design-rules.md), [references/output-contract.md](references/output-contract.md)
- Prompt-shaped references such as `Hard constraints` and `Style`: [references/prompt-reference-protocol.md](references/prompt-reference-protocol.md)
- Audio files, generated renders, and "make it feel like this" comparisons: [references/audio-reference-protocol.md](references/audio-reference-protocol.md)
- Revision, regeneration, reset, and common-requirement propagation: [references/revision-protocol.md](references/revision-protocol.md)

## Convert Prompt-Shaped References Into Seeds First

When the user provides a reference prompt that combines `Hard constraints`, `Style`, tempo, vocal, instrumentation, and exclusions, do not use it directly as a finished Prompt or as approved constraints. First decompose it into a seed design that separates explicit values from inferred values, then research and recommend real related songs, then interview the user about the desired mood in batches of 1-2 questions. Do not finalize recommended songs as Primary or Supporting references until the user selects them. At this stage, do not output the 10-track design or any single-track Prompt/Lyrics.

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

## 3. Get Approval For Reference DNA And Vocal Design

From the references, extract genre grammar, era feel, tempo range, groove, vocal phrasing, instrument roles, production density, and space. Present the high-level traits to preserve separately from the lower-level elements to newly design. Use real artist and song names only as analysis evidence, never in the generation prompt.

Offer 1-3 virtual lead vocal candidates for the user to choose from. If the user specifies one vocalist, keep exactly that one lead across all tracks and do not create additional IDs or alternate leads. Each track has a single lead; background chorus and harmony are allowed within the approved scope. Get approval for the vocal's range, lowest note, timbre, power, pronunciation, phrasing, emotional depth, and forbidden traits.

## 4. Separate The Full Design From Actual Outputs

Create the full design table for exactly 10 tracks at once. Keep the same world, central genre, adjacent genres, and tempo zone while changing each track's instrument roles, intro, drum performance, harmonic device, and narrative. Hooks are not mandatory; apply the random hook-strategy assignment rules in [references/design-rules.md](references/design-rules.md). Each track must stand alone as a complete piece. Before the full design is approved, do not create actual prompts or lyrics.

After approval, output only the one track the user selects, using the following two blocks.

1. `Suno Prompt`: primarily English, with exclusions integrated, maximum 800 characters including spaces and punctuation
2. `Lyrics`: complete lyrics in the approved single language, within +/-20% of the genre-standard length

Follow the format and checking gates in [references/output-contract.md](references/output-contract.md).

## 5. Compile Prompts Atomically

Do not stitch old sentences together. Each time, rewrite the whole prompt from the approved design and the latest requirements. Use this order.

1. `Hard constraints:` place only the short core constraints that would break the result if violated
2. `Style:` country, era, central/adjacent genre, tempo, and groove
3. The single lead vocalist's identity and phrasing
4. Any confirmed values among the four dynamic axes
5. Instrument roles, intro, drums, harmony, hook, and mix
6. Briefly add only necessary low-priority exclusions

If positive and negative wording would induce the same audible trait at the same time, do not add more negative wording; remove or replace the positive wording that causes the conflict. If the user says to remove a concept entirely, delete that concept from both positive and negative wording. Keep `Hard constraints` as short as possible and describe the desired sound in clear positive terms.

## 6. Diagnose Revisions Before Regenerating

When there is a failed result, do not revise by guessing from the prompt alone. First classify the difference between the approved design and the actual result. If the user has already described the cause and goal specifically, revise without additional interview. Ask 1-2 diagnostic questions only when the issue is ambiguous.

For revisions, re-evaluate both Prompt and Lyrics from scratch and provide a complete regenerated version. Do not provide partial patches, add-on sentences, or diffs. Propagate common requirements to remaining tracks, and apply track-specific requirements only to that track.

## 7. Treat Reset As A Full Reset

When the user explicitly says `reset`, `full reset`, `complete reset`, `project reset`, or `playlist reset`, do not treat it as current-track regeneration. Preserve only the history, and clear all active Context, all reference roles, Target/Rejected renders, Approved constraints, genre/language/vocal/voicing, common rules, 10-track design and approval, selected track, and per-track Prompt/Lyrics progress.

After reset, restart with the initial interview for a new project. When enough high-level inputs are gathered, present exactly 10 tracks in a new full design table and wait for approval. Before approval, do not output any single-track Prompt or Lyrics.

`Redesign the current track from scratch` is not a reset; it is a track-level full regeneration. Do not confuse the two. Follow the detailed state transitions in [references/revision-protocol.md](references/revision-protocol.md).

## 8. Complete Checks And Records

If any check fails, do not reveal the result. Internally redesign and rerun all checks. After outputting one track, do not automatically generate the next one; wait for approval or revision requests.

When a workspace is available, use `PROJECT_HISTORY.md` as the index and `history/YYYY-MM-DD__topic-slug.md` as the detailed record. Accumulate approved designs, user feedback, Prompt versions, failure causes, check results, and state. Do not overwrite prior versions.
