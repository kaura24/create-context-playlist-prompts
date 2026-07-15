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
- Harmony research candidates: at least three real songs from the three allowed categories to use for chord-progression judgment, with each song's role. Partial overlap across tracks is allowed, but pairwise overlap of 50% or more is not allowed

For virtual vocals, use the IDs `V1`, `V2`, and `V3`, and use the following columns.

`Role | Gender/age impression | Range/lowest note | Timbre/voicing | Emotion/pronunciation | Forbidden traits | Expected track count`

Ask the user to review and approve genre coordinates, harmony research candidates, vocal consistency, and forbidden traits.

## 2. 10-Track Full Design Table

Provide exactly 10 rows at once.

`# | Working title | Theme/narrative | Vocal | Language | Energy | Genre blend | Target length | Common core + track-specific instruments | Intro | Drum variation | Harmony evidence/feature | Hook | Emotional depth/vocal lowest note | Core exclusions`

Immediately before writing the table, randomly assign each track's hook strategy. In the `Hook` column, record the draw result and track-specific implementation direction from: `none`, `repetition`, `varied chorus`, `final-only`, and `instrumental hook`. Do not force every track to have a hook.

After the table, check for repetition in intro, central instrument combination, drum pattern, harmonic device, hook concept, and abrupt genre leaps. Do not create actual prompts or lyrics yet; ask for approval of the full design table.

## 3. Actual Result For One Track

Use the following format without adding long explanations.

Before output, pass all of the following gates.

- Is the style world similar to the previously approved tracks?
- Is the central genre the same, and are genre variations within the adjacent range?
- Do era, country, and language coordinates match the playlist rules?
- Are speed and groove range similar to previous tracks?
- Are instrument roles and combinations sufficiently different from previous tracks?
- Are melodic hook and contour sufficiently different from previous tracks?
- Are drum pattern, fills, and accents sufficiently different from previous tracks?
- Are repeated-reference roles and application scope stated, and is harmony-reference overlap below 50% for every track pair?
- Do positive style terms avoid inducing the same trait as any exclusion?

If any gate fails, do not reveal the result. Redesign and recheck every item. Resolve semantic conflicts by removing or replacing the positive expression that causes the issue, not by adding more negative wording. Only provide the result below when every gate passes.

When outputting a revision, provide the whole format below again. Do not provide only a replacement for part of an existing code block, an add-on sentence, a diff, or a shortened patch.

### Track N - Title

**Suno Prompt**

```text
[Hard constraints: critical exclusions that must be followed. | Style: desired style, primarily in English, written in terms Suno can understand best. If needed, add compressed low-priority exclusions at the end. Maximum 800 characters total.]
```

**Lyrics**

```text
[Intro]
[If needed: Instrumental, bar count, entry instruction]

[Verse 1]
...

[Pre-Chorus]
...

[Chorus]
...

[Verse 2]
...

[Bridge]
...

[Final Chorus]
...

[Outro]
...
```

Omit or transform sections that are not needed for the genre. If a track forbids vocals for the first 16 bars, do not put lyrics in the Intro. Judge style and lyrics together so emotion, vocal range, hook, chord turns, and structure are aligned.

## 800-Character Integrated Prompt Compression Order

1. Remove duplicated modifiers.
2. Preserve genre, era, vocal, groove, and core instruments.
3. Compress intro, drums, harmony, and hook into short musical terms.
4. Preserve structure, dynamics, and mix.
5. Move core exclusions to the opening `Hard constraints:` and compress only low-priority exclusions at the end.
6. Compare `Hard constraints` against `Style`, remove contradictory words/audible traits/performance directions, and replace them with positive alternatives.

Do not exceed 800 characters including spaces and punctuation. Aim for 700-790 characters while preserving both the desired sound and mandatory exclusions. Do not output a separate Exclude Styles code block. Do not apply the 800-character limit to lyrics or the full design table.
