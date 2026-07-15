# Output Contract

## 0. Prompt-Shaped Reference Intake

When the user provides a prompt-shaped reference, output the following two tables in Korean before any 10-track design.

`Seed axis | Value found in the prompt | Explicit/inferred | Role in the 10-track design`

Seed axes must include Context, genre coordinates, tempo/groove, vocal, instrument roles, drums, harmony, structure/hook, mix/space, and Hard constraints.

`Category | Related-song candidate | Recommended role | Matching elements | Different elements | Evidence`

Recommend 5-8 real related songs and include all three categories: `English-language pop songs`, `Japanese-language songs`, and `Korean-language songs`. Indicate which evidence axis each song supports, such as genre, vocal phrasing, arrangement, harmony, or production. Exclude songs whose primary lyric language is outside these three categories, and exclude purely instrumental pieces. The same song may be assigned to multiple roles or reused across later tracks; when reused, state its role and scope of application. Only per-track harmony references must keep overlap below 50% between any two tracks. Do not auto-approve candidates. After the table, ask 1-2 mood-disambiguation questions at a time. Do not proceed to the 10-track design until mood and reference roles are approved.

## 1. Basic Research Result And Vocal Approval Proposal

Provide the following in Korean.

- Genre coordinates: country/region, era, cultural zone/market, macro-genre, subgenre, speed/groove, language, production grammar
- Reference DNA: high-level traits to preserve, elements to newly design, listening-situation adjustments, unique elements to avoid copying
- Playlist sound contract: listening use case, Common sound, Track variation pool, and Drift boundaries
- Harmony research candidates: at least three real songs from the three allowed categories to use for chord-progression judgment, with each song's role. Partial overlap across tracks is allowed, but pairwise overlap of 50% or more is not allowed

For virtual vocals, use the IDs `V1`, `V2`, and `V3`, and use the following columns.

`Role | Gender/age impression | Range/lowest note | Timbre/voicing | Emotion/pronunciation | Forbidden traits | Expected track count`

Ask the user to review and approve genre coordinates, the Playlist sound contract, harmony research candidates, vocal consistency, and forbidden traits.

## 2. 10-Track Full Design Table

Provide exactly 10 rows at once.

Restate the approved shared contract once above the table as:

`Use case | Common sound | Track variation pool | Drift boundaries | Genre-valid structure pool`

Use these columns for the 10 rows:

`# | Working title | Theme/narrative | Track differentiator | Vocal | Language | Energy | Genre blend | Target length | Track-specific instrument roles | Structure/development, including intro/entry | Drum variation | Harmony evidence/feature | Hook | Emotional depth/vocal lowest note | Core exclusions`

Before assigning hooks, select every track's genre-valid structure family and development signature through [structure-patterns.md](structure-patterns.md). Record the actual section sequence, intro/entry, peak or contrast mechanism, and ending behavior compactly in `Structure/development`. Then randomly draw each track's hook strategy only from compatible candidates. In the `Hook` column, record the draw result and track-specific implementation direction from: `none`, `repetition`, `varied return`, `final-only`, and `instrumental hook`. Do not force every track to have a hook.

After the table, check whether each track varies within the shared use case rather than reinventing it. Also check for repetition in structure family plus development signature, intro/entry, central instrument combination, drum pattern, harmonic device, hook concept, and abrupt genre leaps. When a structure family repeats, confirm that at least two development dimensions differ. Do not create actual prompts or lyrics yet; ask for approval of the full design table.

## 3. Actual Result For One Track

Apply the public platform contract in [suno-style-guide.md](suno-style-guide.md) and the private project contract from the approved design and latest user instructions, then use the following format without adding long explanations.

Before output, pass all of the following gates.

- Is the Main Prompt at most 800 characters including spaces and punctuation?
- Is the Exclusion Prompt at most 100 characters including spaces and punctuation?
- Is the style world similar to the previously approved tracks?
- Is the central genre the same, and are genre variations within the adjacent range?
- Do era, country, and language coordinates match the playlist rules?
- Are speed and groove range similar to previous tracks?
- Does the track vary within the approved Playlist sound contract rather than replacing it?
- Are instrument roles and combinations sufficiently different from previous tracks?
- Do the Main Prompt and Title And Lyrics preserve the approved structure family, section sequence, development signature, and ending behavior?
- If another track shares the structure family, do at least two development dimensions differ?
- Are melodic hook and contour sufficiently different from previous tracks?
- Are drum pattern, fills, and accents sufficiently different from previous tracks?
- Are repeated-reference roles and application scope stated, and is harmony-reference overlap below 50% for every track pair?
- Do positive style terms avoid inducing the same trait as any exclusion?

If any gate fails, do not reveal the result. Redesign and recheck every item. Resolve semantic conflicts by removing or replacing the positive expression that causes the issue, not by adding more negative wording. Only provide the result below when every gate passes.

When outputting a revision, provide the whole format below again. Do not provide only a replacement for part of an existing code block, an add-on sentence, a diff, or a shortened patch.

### Track N - Title

**Main Prompt**

```text
[Desired style, primarily in English, written in terms Suno can understand best. Maximum 800 characters total.]
```

**Exclusion Prompt**

```text
[Only absolute prohibitions. Maximum 100 characters total.]
```

**Title And Lyrics**

```text
Title: [approved title]

[<approved opening or intro label>]
[<approved bar count or entry instruction, if needed>]

[<first approved section label>]
...

[<next approved section label>]
...

[<continue only with sections in the approved sequence>]
...

[<approved ending or outro label>]
...
```

Replace every placeholder with the track's actual approved section label and omit any inapplicable line. Do not insert Verse, Pre-Chorus, Chorus, Bridge, or Final Chorus unless that section exists in the approved structure. If a track forbids vocals for the first 16 bars, do not put lyrics in the opening. Judge style and lyrics together so emotion, vocal range, hook, chord turns, and structure are aligned.

## 800-Character Main Prompt Compression Order

1. Remove duplicated modifiers.
2. Preserve genre, era, vocal, groove, and core instruments.
3. Preserve the structure family, intro/entry, and defining development or ending behavior.
4. Compress drums, harmony, and hook into short musical terms.
5. Preserve dynamics and mix.
6. Preserve necessary positive guardrails.
7. Compare the Main Prompt against the Exclusion Prompt. Remove contradictory positive words, audible traits, or performance directions and replace them with positive alternatives.

Do not exceed 800 characters including spaces and punctuation. Aim for 700-790 characters while preserving the desired sound. Do not count the Exclusion Prompt, title, or lyrics toward this limit.

## 100-Character Exclusion Prompt

Include only absolute prohibitions that must be entered separately from the Main Prompt. Prefer short comma-separated English terms over sentences. Prioritize prohibitions whose violation would make the result unusable; express lower-priority control as positive guidance in the Main Prompt.

Do not exceed 100 characters including spaces and punctuation. Do not count this limit toward the Main Prompt's 800 characters. Do not repeat an exclusion in the Main Prompt. If naming a forbidden concept itself induces the unwanted result, omit that concept from both prompts and use only a positive replacement in the Main Prompt.
