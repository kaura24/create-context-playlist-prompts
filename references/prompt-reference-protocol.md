# Prompt-Shaped Reference Protocol

## Detect Prompt-Shaped References

If the user's input has generation-prompt grammar such as `Hard constraints`, `Style`, BPM, time signature, vocal, instrumentation, harmony, mixing, or exclusions, and the user provides it as a reference, record it as a `Prompt reference`. Do not ask for a Primary reference first just because there is no real song title.

Do not treat sentences inside the prompt as the final Main Prompt or Exclusion Prompt, playlist-wide constraints, or approved values for a specific track. Separate facts explicitly stated by the user from musical inferences.

## Decompose Into A Seed Design

Organize the following axes in a table.

- Context and listening scene
- Country, era, market, central genre, and adjacent genres
- BPM, time signature, and groove
- Lead vocal range, timbre, power, pronunciation, and phrasing
- Common texture and instrument roles
- Drum pattern and section transitions
- Harmonic language and cadences
- Reported form or section sequence, intro, and hook candidates
- Vocal/instrument space and mixing
- Hard constraints and possible conflicts

Mark each item as `explicit`, `strong inference`, or `unconfirmed`. Do not invent emotions, situations, or cultural zones that are not present in the prompt. This table is only a seed for the 10-track design; it is not yet an approved full design.

Treat a form or sequence written in the source prompt as explicit only for that Prompt reference. Do not generalize it into a genre-wide form, rename it, infer its permitted variations, or add it to the 10-track design pool until it passes [structure-patterns.md](structure-patterns.md) and the user approves its scope, flow, and Lyrics tag sequence.

At final generation time, route positive requirements from the source prompt into the Main Prompt and route only explicit absolute prohibitions into the separate Exclusion Prompt. The source label `Hard constraints` does not determine the output field by itself.

## Recommend Real Related Songs

Research and recommend 5-8 real songs close to the seed design. This recommendation depends on currently existing songs and accessible evidence, so use internet search and verify song title, artist, release timing, and recommendation rationale.

If internet evidence is unavailable, mark the recommendation stage `evidence-needed` and stop before reference approval or the 10-track design. Do not substitute unverified memory for real-song evidence.

Limit the recommendation and selection pool to the following three categories, based on the primary lyric language.

- `English-language pop songs`: pop-adjacent songs whose primary language is English
- `Japanese-language songs`: songs whose primary language is Japanese
- `Korean-language songs`: songs whose primary language is Korean

Classify by the song's actual primary lyric language, not by the artist's nationality or active market. Exclude songs whose primary language is outside these three categories and exclude purely instrumental pieces. Include all three categories in the default recommendation table, but do not force equal counts mechanically.

Do not push all candidates in one direction. Split them across whichever roles are needed.

- Central genre and era grammar
- Vocal phrasing and timbre
- Instrument placement and space
- Drums and groove
- Harmony and cadences
- Listening scene and emotion

For each candidate, include both `matching elements` and `different elements` to reduce copying risk. Recommended songs are not Primary or Supporting references until the user selects or approves them. Use real artist and song names at the recommendation stage only in analysis tables, never in the Main Prompt or Exclusion Prompt.

Allow general-reference overlap. The same song may be assigned to multiple analysis roles such as vocal and arrangement, reused in Primary/Supporting judgment, or reused as research evidence for multiple tracks in the 10-track plan. In the tables and design, state each repeated song's role and scope of application.

Allow only partial overlap in per-track harmony references. For two tracks' harmony-reference sets `A` and `B`, compute overlap as `|A intersection B| / min(|A|, |B|)`; values of `0.5` or higher are not allowed. If each list has three songs, one overlap is allowed but two overlaps are not. During the 10-track design and revision stages, compare the current track pairwise against every other track.

## Interview Mood After Recommendations

Show the related-song table first, then ask only 1-2 mood-disambiguation questions at a time. If the prompt already answers something, do not ask it again; confirm only axes that would materially change the result, such as:

- central emotion among loneliness, calm, tension, and release
- ratio of darkness to brightness
- stillness versus forward motion
- vocal distance and emotional depth
- chorus lift and arrangement density
- ending as resignation, recovery, or unresolved

Treat free-form descriptions as confirmed input. Once the mood and recommendation roles are approved, move to genre coordinate, reference DNA, and vocal approval. Only after that should you create the exact 10-track full design table.
