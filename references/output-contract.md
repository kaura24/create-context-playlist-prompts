# Output Contract

## Contents

- Prompt-shaped reference intake
- Research, form evidence, and vocal approval
- 10-track full design table
- Track-by-track final result and approval cycle
- Main Prompt compression
- Exclusion Prompt compression

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
- Form Evidence Table and Permitted Variation Envelopes: verified names or literal sequences, sources, representative songs, invariants, allowed ranges, boundary violations, and confidence
- Vocal And Engineering Contract: vocal identity, performance naturalness, language delivery, mic/room, dynamics, tonal balance, stereo position, accepted texture, and rejected artifacts
- Initial Playlist Harmony Candidate Pool: verified real songs and each song's possible harmonic role. This is a starting pool, not the final per-track assignment; expand it during the 10-track design as needed

For virtual vocals, use the IDs `V1`, `V2`, and `V3`, and use the following columns.

`Role | Gender/age impression | Range/lowest note | Timbre/voicing | Emotion/pronunciation | Forbidden traits | Expected track count`

Approve these artifacts sequentially and ask for no more than 1-2 decisions at a time.

`Approval state | Requires | Revalidate when this state changes`

`Genre And Reference DNA | approved intake | every downstream contract and draft`

`Playlist Sound Contract | Genre And Reference DNA | Form Evidence applicability and the full design`

`Form Evidence And Variation Envelopes | Genre And Reference DNA; Playlist Sound Contract | full-design form assignments, Structural Flows, and Lyrics tag sequences`

`Vocal And Engineering Contract | Genre And Reference DNA; Playlist Sound Contract | vocal and engineering fields in the full design and every unapproved prompt set`

`Initial Harmony Candidate Pool | Genre And Reference DNA; Playlist Sound Contract | harmony assignments and newly designed progressions in the full design`

Rejecting an artifact blocks dependent work until that artifact is revised and approved. Changing an approved artifact invalidates only the listed dependent approvals or drafts; retain unaffected upstream approvals. Full Design Approval requires all five states above.

## 2. 10-Track Full Design Table

Provide exactly 10 rows at once.

Restate the approved shared contract once above the table as:

`Use case | Common sound | Track variation pool | Drift boundaries | Approved evidence-backed form pool and variation envelopes`

Use these columns for the 10 rows:

`# | Working title | Theme/narrative | Track differentiator | Vocal | Language | Energy | Genre blend | Target length | Track-specific instrument roles | Verified form/source | Structural flow and permitted development | Lyrics tag sequence | Drum variation | Harmony evidence | New section-level progression/cadences | Hook | Emotional depth/vocal lowest note | Vocal naturalness/audio engineering | Core exclusions`

Before assigning hooks, select every track's form only from the approved Form Evidence Table through [structure-patterns.md](structure-patterns.md). If no form name is verified, write the approved literal sequence and evidence status; never coin a name. Keep every invariant and select the exact sequence, intro/entry, contrast, peak, repeats, and ending only inside the approved Permitted Variation Envelope and Structural Flow Contract. Record the exact bracketed Lyrics tag sequence separately. Then draw each track's hook strategy only from compatible candidates. In the `Hook` column, use the canonical values `No hook`, `Repeated hook`, `Varied return`, `Final-only callback`, or `Instrumental hook`. Do not force every track to have a hook.

Expand and assign harmony evidence during this table so every track has at least three confirmed real-song harmony references. Validate every track pair with `intersection / shorter-list size < 0.5`; the initial candidate pool alone does not satisfy this gate.

After the table, check whether each track varies within the shared use case and approved structural envelopes. Also check form evidence, boundary compliance, Structural Flow Contract, actual sequence, development signature, Lyrics tag sequence, intro/entry, central instrument combination, drum pattern, new progression, harmonic device, hook concept, and abrupt genre leaps. Do not penalize a supported form merely for recurring, and do not import an unsupported form to increase variety. Present the per-track flows, tag sequences, and progressions as part of the table approval. Do not create actual prompts or lyrics yet; ask for approval of the full design table.

## 3. Per-Track Three-Prompt Preference Cycle

After the full design table is approved, process Tracks 1-10 one at a time. Apply the public platform contract in [suno-style-guide.md](suno-style-guide.md) and the private project contract from the approved design, latest user instructions, and accumulated Calibration Lock.

For every current track, present this short comparison table in Korean:

`Main Prompt | Constants | Test axis 1 | Test axis 2, if necessary | Expected audible difference`

Then output exactly three controlled Main Prompts, `A`, `B`, and `C`, plus one shared Exclusion Prompt and one shared Title And Lyrics. Keep title, lyrics, exact Lyrics tag sequence, lead-vocal identity, language, absolute exclusions, and central genre fixed. Treat the shared Lyrics tag sequence as the common scaffold. Keep feel, harmonic language, form development, Structural Flow, arrangement, and production similar rather than identical within the approved envelopes. This is a variation-permission envelope, not an instruction to alter every field. Change only one primary unresolved axis, or at most two tightly related axes; keep every non-test-axis field semantically at the approved A baseline even if concise wording differs. Do not add unapproved mood, geography, instrumentation, harmony, form, or production details merely to make B/C sound distinct. Useful comparison axes include emotional shade, harmonic variant, peak or transition treatment, vocal performance naturalness, arrangement density, groove pressure, instrument prominence, transient character, room distance, or processing intensity.

Do not create three unrelated prompt rewrites. On the first listening round for a track, compile Main Prompt A directly from that track's approved 10-track design row plus the active Calibration Lock, without adding a comparison-axis deviation. Track 1 begins with no listening-derived Calibration Lock entries; the approved project contracts still apply. B and C make bounded, explicitly stated alternatives.

On a later listening round for the same track, recompile A from the revised current-track design and active Calibration Lock. Do not silently carry rejected wording into the new baseline. The one Exclusion Prompt and one Title And Lyrics are shared by all three generations.

Before revealing the set, verify that every difference belongs to the declared test axes, remains inside the approved similarity and variation envelopes, and that A, B, and C independently pass the 800-character and structural checks below.

Use the exact section headings and fenced `text` blocks in the template below. When a shell is available, write the complete draft to a temporary Markdown file and run the skill's `scripts/validate_track_output.py` with the approved tag sequence. Treat a nonzero exit as a failed output gate and regenerate the complete set before revealing it.

After the user generates and listens to all three versions, record:

`Track | Chosen Main Prompt | Preserved audible traits | Rejected audible traits | Prompt correction | Scope/expiry | Updated Calibration Lock`

If no Main Prompt is acceptable, redesign three new controlled Main Prompts. Keep the shared Exclusion Prompt and Title And Lyrics unless the feedback specifically targets them. Do not proceed to the next track until the current track is approved and its preference update is added to the Calibration Lock.

Before revealing the current set, pass all of the following gates against the approved design, Calibration Lock, approved tracks, and remaining 10-track plan.

- Are Main Prompts A, B, and C each at most 800 characters including spaces and punctuation?
- Is the Exclusion Prompt at most 100 characters including spaces and punctuation?
- Are feel, harmony, form development, Structural Flow, arrangement, and production similar rather than forcibly identical, with all A/B/C differences limited to the declared 1-2 comparison axes?
- Does the comparison table name the actual fixed scaffold and baseline fields instead of labeling all musical content `same` or `identical`?
- Do all non-test-axis values trace directly to the approved track row, project contracts, or active Calibration Lock?
- Does every Main Prompt include a complete approved chord progression, with any variant staying inside the shared harmonic direction?
- Are all bracketed section tags absent from Main Prompts and present only in Title And Lyrics?
- Is the style world similar to the previously approved tracks?
- Is the central genre the same, and are genre variations within the adjacent range?
- Does every Main Prompt state the approved listening feel instead of relying on genre labels alone?
- Does every vocal-naturalness or engineering direction name an audible trait rather than only saying natural, human, or non-AI?
- Do era, country, and language coordinates match the playlist rules?
- Are speed and groove range similar to previous tracks?
- Does the track vary within the approved Playlist sound contract rather than replacing it?
- Are instrument roles and combinations sufficiently different from previous tracks?
- Does the form or literal sequence come from the approved Form Evidence Table?
- Does every structural variation stay inside the approved envelope?
- Do the Main Prompt and Title And Lyrics preserve the approved section sequence, development signature, and ending behavior?
- Does Title And Lyrics use the exact approved bracketed Lyrics tag sequence?
- Are melodic hook and contour sufficiently different from previous tracks?
- Are drum pattern, fills, and accents sufficiently different from previous tracks?
- Are repeated-reference roles and application scope stated, and is harmony-reference overlap below 50% for every track pair?
- Do positive style terms avoid inducing the same trait as any exclusion?

If any gate fails, do not reveal the current set. Redesign it and rerun both per-track and cross-track gates. Resolve semantic conflicts by removing or replacing the positive expression that causes the issue, not by adding more negative wording.

When outputting a revision, repeat all three Main Prompts plus the one shared Exclusion Prompt and one shared Title And Lyrics. Do not provide only a replacement phrase, add-on sentence, diff, or shortened patch.

### Track N - Title

**Main Prompt A**

```text
[Approved baseline direction. Maximum 800 characters total.]
```

**Main Prompt B**

```text
[Controlled alternative B. Maximum 800 characters total.]
```

**Main Prompt C**

```text
[Controlled alternative C. Maximum 800 characters total.]
```

**Exclusion Prompt**

```text
[Only absolute prohibitions. Maximum 100 characters total.]
```

**Title And Lyrics**

```text
Title: [approved title]

[<approved bracketed Lyrics opening tag>]

[<first approved bracketed Lyrics section tag>]
...

[<next approved bracketed Lyrics section tag>]
...

[<continue with the exact approved bracketed Lyrics tag sequence>]
...

[<approved bracketed Lyrics ending tag>]
...
```

Replace every placeholder with the track's approved bracketed Lyrics tag and omit any inapplicable line. Use only tags supported by current official Suno guidance or a user-provided verified instruction. Route bar-count and vocal-entry directions to Main Prompt `Form/Flow` as plain prose, never to an unsupported bracketed Lyrics instruction. Do not insert `[Verse]`, `[Pre-Chorus]`, `[Chorus]`, or `[Bridge]` unless that function exists in the approved source structure. Never use poetic scene names as tags. If a functional tag cannot be verified, stop before final output and resolve it. If a track forbids vocals for the first 16 bars, do not put lyrics in the opening. Judge style and lyrics together so emotion, vocal range, hook, chord turns, and structure are aligned.

## 800-Character Main Prompt Compression Order

Write one compact semicolon-separated clause per required field rather than full narrative sentences. Represent harmony once per unique section function, for example `Verse Am9-D13-Gmaj7-Cmaj7; Chorus Fmaj7-G6-Em7-Am9`, rather than repeating the same progression for every return. Do not expand a field with unapproved synonyms, extra subclauses, or decorative explanation.

Never omit central genre/era identity, `Feel`, lead-vocal identity, the complete compact harmonic plan, form/flow identity, or the declared A/B/C comparison axis. Keep at least one precise phrase for tempo/groove, core instrumentation, and defining production/mix.

Compress in this order:

1. Remove duplicated modifiers and non-audible prose.
2. Remove decorative emotional synonyms after preserving the approved `Feel`.
3. Drop secondary instruments, effects, and low-priority arrangement details.
4. Compress drum, hook, and non-test-axis mix details into the shortest precise terms.
5. Compress positive guardrails without turning them into negative instructions.
6. Scan for negative command words such as `no`, `without`, `avoid`, and `exclude`; route absolute prohibitions to the shared Exclusion Prompt and rewrite lower-priority controls positively.
7. Compare the Main Prompt against the Exclusion Prompt and replace conflicting or duplicated wording.

If the prompt still exceeds 800 characters, rewrite the compact notation or redesign low-priority wording; do not omit the required minimum or reveal an over-limit prompt.

Do not exceed 800 Unicode characters including spaces and punctuation. Use a deterministic character counter when a tool is available and rewrite until the measured result passes. Without a counter, target 650-700 characters to retain a safety margin. Do not count the Exclusion Prompt, title, or lyrics toward this limit.

## 100-Character Exclusion Prompt

Include only absolute prohibitions that must be entered separately from the Main Prompt. Prefer short comma-separated English terms over sentences. Prioritize prohibitions whose violation would make the result unusable; express lower-priority control as positive guidance in the Main Prompt.

Do not exceed 100 characters including spaces and punctuation. Do not count this limit toward the Main Prompt's 800 characters. Do not repeat an exclusion in the Main Prompt. If naming a forbidden concept itself induces the unwanted result, omit that concept from both prompts and use only a positive replacement in the Main Prompt.
