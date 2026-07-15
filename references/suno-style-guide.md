# Suno Style Guide

Use this reference when compiling the final Main Prompt, Exclusion Prompt, and Title And Lyrics. Keep the three fields separate because Suno Custom Mode treats Styles, Advanced options such as Exclude, Lyrics, and Title as distinct inputs.

## Two-Layer Contract

Treat Suno's official published guidance as the `public platform contract`. It defines what each Suno field is for, which musical vocabulary the platform documents, and how Styles, Exclude, Lyrics, and Title are separated.

Treat the user's latest instructions, approved Playlist sound contract, approved 10-track design, and this skill's output limits as the `private project contract`. It defines the desired music, exclusions, structure, language, vocalist, and operating caps.

Compile Main Prompt, Exclusion Prompt, and Title And Lyrics against both contracts. Use the public contract to route information into the correct field. Use the private contract to decide the actual content. When both define a limit, follow the stricter limit. Never let a public example override an approved private requirement.

## Evidence Boundary

The following rules reflect Suno's published guidance.

- Put genre-specific information in the Style field.
- Put lyrics and additional section-level song context in the Lyrics field.
- Use Exclude for unwanted genres, instruments, voice styles, and similar traits.
- Use specific musical vocabulary for tempo, groove, dynamics, structure, instrumentation, texture, vocal technique, harmony, and production.
- Combine compatible genre terms, emotional detail, instruments, and sonic texture when they are part of the approved design.
- Detailed and evocative descriptions can work, but each phrase should still indicate an audible trait.

Suno's accessible official guidance does not publish an exact character maximum for Exclude. Treat `800 characters for Main Prompt` and `100 characters for Exclusion Prompt` as this skill's operating caps, not as claims about Suno's documented platform maximum.

## Main Prompt

Write the Main Prompt primarily in concise English. Use this order unless the approved design requires another priority.

1. Country or cultural zone, era, central genre, and adjacent genre
2. BPM or tempo feel, meter when important, and groove
3. Lead vocal range, timbre, power, pronunciation, and phrasing
4. Core instruments, track-specific roles, register, and texture
5. Structure family, intro or first entry, development, peak, and ending
6. Drum performance, harmonic color, hook behavior, dynamics, space, and mix

Prefer direct musical terms such as `72 BPM`, `syncopated pocket`, `sparse felt piano`, `close dry vocal`, `loop-evolution form`, or `diminuendo coda`. Use evocative wording only when it adds a usable audible direction. Front-load the identity-defining traits and compress secondary details first.

Do not include artist or song names. Do not repeat exclusions, write conflicting descriptors, or use long narrative prose that belongs in the lyrics. Do not use a genre label as a substitute for the listening use case; preserve the approved Playlist sound contract.

## Exclusion Prompt

Write a separate comma-separated list of only absolute prohibitions. Prefer bare traits such as `belting, trap hi-hats, key change` over sentences. Prioritize exclusions whose violation would make the result unusable.

Keep the Exclusion Prompt at 100 characters or fewer, including spaces and punctuation. Do not repeat an exclusion in the Main Prompt. If naming an unwanted concept itself causes the model to produce it, omit the concept from both prompts and express only the desired replacement in the Main Prompt.

## Title And Lyrics

Put the title on the first line, then write complete lyrics using the approved single language and exact section sequence. Use recognizable section labels where they match the approved structure. For nonstandard structures, use concise labels that describe the actual function of each section.

Keep genre and production description in the Main Prompt. Put only section-specific performance or development context in the Lyrics field, such as a delayed entry, instrumental break, restrained delivery, or final shortened line. Do not add a universal Verse-Pre-Chorus-Chorus form that was not approved.

## Final Check

- Main Prompt is at most 800 characters, including spaces and punctuation.
- Exclusion Prompt is at most 100 characters, including spaces and punctuation.
- Title And Lyrics uses the approved title, language, structure, and development signature.
- Main and Exclusion prompts contain no contradiction or duplicated prohibition.
- Every phrase belongs in the Suno field where it will be entered.

## Official Sources

- [Music Glossary for Suno](https://help.suno.com/en/articles/9010177)
- [Create in V4.5: Better Prompts in Lyrics](https://help.suno.com/en/articles/5782977)
- [What's new in V4.5](https://help.suno.com/en/articles/5782593)
- [How do I exclude elements of a song?](https://help.suno.com/en/articles/3161921)
- [Android Create: Custom Mode](https://help.suno.com/en/articles/3726721)
