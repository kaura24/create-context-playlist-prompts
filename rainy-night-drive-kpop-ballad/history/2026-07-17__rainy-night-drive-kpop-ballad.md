# Rainy Night Drive K-pop Ballad

## Playlist Contract

| Use case | Common sound | Variation pool | Drift boundaries |
|---|---|---|---|
| 비 오는 밤 드라이브 | K-pop 발라드, 좁은 편곡 다이내믹, A3-D5 저음 중심의 일본 모던 여성 재즈 보컬 음색과 프레이징 | 구조·화성 리듬·카덴스·베이스 움직임·악기 역할을 곡별로 변화 | 전 곡 고음 클라이맥스·드럼 크레셴도·재즈 반주 금지; 스윙·워킹 베이스·재즈 컴핑·브러시·혼·스캣·랩 벌스 금지 |

## Assumption Ledger

| Assumption | Why | Confidence | Easy correction |
|---|---|---|---|
| Track 1-9는 영어, Track 10은 임시 한국어 값 | Track 2-9 영어는 사용자 확정; Track 10은 출력 전 언어 확인 필요 | high | 각 트랙 생성 직전 명시 언어로 교체 |
| 10곡 모두 A3-D5, 주요 음역 A3-C#5 | 편곡과 보컬 고음 모두의 다이내믹을 줄이라는 playlist-lock 피드백 | high | 범위 변경 시 전 트랙 Vocal·Flow·Mix·금지 프롬프트 동시 수정 |
| 훅 전면성은 seed rainy-night-drive-hook-v1 | 사용자 요청에 따라 3 subtle, 4 moderate, 3 strong 균형 셔플 | high | seed 변경 후 전 트랙 Form/Flow 재컴파일 |
| fast mode | 트랙별 승인 요청이 없고 기본 모드 | high | listen-each-track으로 전환 가능 |

## 10-track Map

| # | Working title | Scene and emotional turn | Tempo | Form and planned duration | Differentiator | Status |
|---|---|---|---|---|---|---|
| 1 | Voice Beyond the Wipers | 심야 라디오가 고독을 조용한 동행으로 바꾼다 | 88 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Pre-Chorus–Chorus–Bridge–Chorus–Outro, 218.2초 | 피아노 모티프와 하행 베이스의 라디오형 빌드 | PLAN PASS after opening/groove migration |
| 2 | While the Light Stays Red | 보내지 못한 말이 붉은 신호 아래 편지처럼 머문다 | 78 BPM | Intro–Verse–Chorus–Verse–Chorus–Coda, 209.2초 | 기타 아르페지오와 짧은 두 번의 후렴 | PLAN PASS after opening/groove migration |
| 3 | Past Your Exit | 돌려줄 열쇠를 들고 옛집으로 가다가 직접 만나지 않고 우편으로 보내기로 결정한다 | 76 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Pre-Chorus–Chorus–Bridge–Refrain–Outro, 227.4초 | 신스 펄스와 마지막 독립 리프레인 | PLAN PASS after opening/groove migration |
| 4 | Not That Exit Again | An old address still saved as Home stops controlling the route | 82 BPM | Intro–Verse–Pre-Chorus–Chorus–Break–Verse–Pre-Chorus–Chorus–Coda, 234.1초 | A four-note descending title hook stays catchy at low volume; the coda alone names the new home | PLAN PASS after opening/groove migration |
| 5 | Under the Station Light | A driver crosses the rainy city to collect her younger sister after the last bus fails to arrive | 84 BPM | Intro–Verse–Chorus–Break–Verse–Chorus–Bridge–Chorus–Outro, 205.7초 | A final semitone modulation changes harmonic color while the melody stays in the same low register | PLAN PASS after opening/groove migration |
| 6 | What You Meant Was Care | A driver safely parks and apologizes after mistaking a partner's flood-route warning for control | 82 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Pre-Chorus–Chorus–Bridge–Pre-Chorus–Chorus–Outro, 234.1초 | A low guitar ostinato and recurring withheld downbeat delay the direct apology until the final return | PLAN PASS after opening/groove migration |
| 7 | I'll Keep the Road Quiet | A driver takes an exhausted night-shift passenger home without disturbing their sleep | 80 BPM | Intro–Verse–Chorus–Verse–Chorus–Bridge–Chorus–Coda, 216.0초 | Filtered synth and reverse guitar hold the quietest interior point before the coda fully releases the final chorus | PLAN PASS after opening/groove migration |
| 8 | Same Time Next Sunday | After visiting hours, a daughter drives home through light rain carrying her mother's cardigan and the promise to return next Sunday | 74 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Pre-Chorus–Chorus–Bridge–Chorus–Coda, 214.1초 | A low five-note title hook returns unchanged while the ordinary care once received from her mother is discovered in reverse | PLAN PASS after opening/groove migration |
| 9 | Quiet, Not Lonely | After leaving a crowded hotel reception alone, the driver finds that unexamined solitude feels kinder than having to explain herself | 74 BPM | Verse–Chorus–Verse–Chorus–Bridge–Chorus–Coda, 214.1초 | Lead and pad enter together on bar one; a five-note low title motif makes quiet relief catchy without raising intensity | PLAN PASS after opening/groove migration |
| 10 | 비가 멎기 전까지 | 새벽이 가까워질수록 상실을 놓고 앞으로 달려간다 | 82 BPM | Intro–Verse–Hook–Verse–Hook–Bridge–Chorus–Outro, 210.7초 | 짧은 훅은 두 번만, 완전한 코러스는 마지막에만 등장 | planned |

## Playlist Revision 3

- Scope: playlist-lock for low dynamics and vocal ceiling; lyric-content review for Tracks 1-3
- Changes: all 10 tracks use narrow arrangement dynamics and an A3-D5 low vocal ceiling with no high-note climax; Tracks 1-3 use concrete causal narratives and English lyrics
- Status: Tracks 1-3 draft-validated after deterministic validation and bound lyric-content review
- Audio duration, pronunciation, performance, and mix remain unverified until a render is supplied.

## Playlist Revision 4

- User-described issue: different BPM values still produced similar intros, drums, percussion patterns, and rhythmic feel across tracks
- Global skill repair: every playlist project now locks `entry` and `groove_signature` as three pipe-separated axes; every selected pair must differ on at least two axes, and every clause must appear in the compiled prompt
- Current-project migration: Tracks 1-10 now use distinct lead-source/onset/vocal-entry signatures and subdivision/accent/support-cycle signatures while percussion remains support-only and macro-dynamics remain narrow
- Evidence boundary: Tracks 1-9 pass deterministic validation after prompt migration; their existing lyric reviews remain valid for unchanged lyrics, while revised audible intros and grooves require new renders

## Track 1 Revision 3

- Narrative: a midnight radio host accompanies the driver from a breakup block to her building while she leaves the final message unanswered
- Status: draft-validated after causal rewrite; review: `reviews/track-01.json`

## Track 2 Revision 2

- Language: English, explicitly confirmed by user
- Hook prominence: subtle, assigned by seed `rainy-night-drive-hook-v1`
- Status: draft-validated; bound lyric-content review 26/26 PASS; review: `reviews/track-02.json`

## Track 3 Revision 4

- Language: English, explicitly confirmed by user
- Hook prominence: moderate, assigned by seed `rainy-night-drive-hook-v1`
- User-described render feedback: 92 BPM felt too fast and the Em-to-major-seventh chorus color did not read as rainy
- Listening-directed change: 76 BPM half-time feel; 72-bar plan; D minor add9 center; two-bar harmonic rhythm, descending bass, and suspended cadences; sparse orchestration and A3-C5 vocal range retained
- Status: draft-validated; fresh bound review 26/26 PASS; audible result remains unverified without the revised render; review: `reviews/track-03.json`

## Track 4 Revision 1

- Language: English, explicitly confirmed by user
- Hook prominence: strong track-local override; catchiness comes from a repeated four-note descending motif and fixed syncopated title rhythm, not louder or higher singing
- Vocal capture: clean joins and silent phrase gaps, without naming unwanted vocal artifacts in generation fields
- Status: draft-validated; fresh bound lyric-content review 25/26 PASS; audible catchiness remains unverified without a render; review: `reviews/track-04.json`

## Track 5 Revision 1

- Language: English, explicitly confirmed by user
- Narrative: a driver takes the hill route to collect her younger sister after the last bus fails to arrive
- Peak design: the final chorus shifts from C-sharp minor to D minor while the melody remains in the same A3-D5 register; no octave lift or loudness peak
- Arrangement boundary: violin and cello removed from the positive instrumentation and named only in the exclusion field
- Status: draft-validated; fresh bound lyric-content review 26/26 PASS; audible result remains unverified without a render; review: `reviews/track-05.json`

## Track 5 Revision 2

- User-described render feedback: repeated piano-led openings made the playlist feel uniform
- Track-local change: muted guitar harmonics and diffuse ambient pad lead the intro; piano is delayed until after the Break
- Preserved locks: narrow macro-dynamics, no density crescendo, A3-D5 ceiling, same-register modulation, and no violin or cello
- Remaining-track rule: rotate entry timbres across guitar ostinato, filtered synth, bass-and-guitar, direct voice, and sub-synth; avoid consecutive piano-led intros
- Status: draft-validated; revised-prompt review 26/26 PASS; audible result remains unverified without a revised render

## Track 6 Revision 1

- Language: English, explicitly confirmed by user
- Entry identity: low electric-guitar ostinato, mono bass drone, soft floor tom, and diffuse dark synth; no piano-led intro
- Narrative: after a flood-route warning is mistaken for control, the driver parks safely before sending a direct apology
- Preserved locks: narrow dynamics, flat density, ambient space, low vocal range, no high-note climax, and no violin or cello
- Status: draft-validated; fresh bound lyric-content review 26/26 PASS; audible result remains unverified without a render; review: `reviews/track-06.json`

## Track 6 Revision 2

- User-described issue: lyric volume was too high and melody-to-lyric consistency was weak
- Density change: 48 lyric lines / 365 English units reduced to 36 lines / 248 units; every eight-bar vocal section now has four two-bar lines
- Prosody change: paired Verse lines target about ten syllables, paired Pre-Chorus lines about eight, and all Chorus returns share identical first three lines plus an aligned eight-syllable fourth-line frame
- Review history: the first fresh prosody review failed on shifting Chorus stress; SAVE/DRAFT/SEND and PARK/PARKED/HOME were realigned before the final 26/26 PASS
- Evidence boundary: text prosody and structural fit are validated; audible melody timing remains unverified without a revised render

## Track 6 Revision 3

- Root cause: style diversification incorrectly promoted percussion from background support to an unconfirmed lead role, conflicting with the rainy low-dynamic ambient goal
- Prompt repair: Style changed to dark ambient K-pop OST ballad; floor tom moved to recessed support; percussion-led moved to Exclusion
- Vocal-artifact control: smoky-adjacent wording removed from the current Vocal field; stable tone and clean joins now state the desired result
- Process repair: percussion role is an explicit intake option with support-only first; repeated vocal artifacts activate lexical suppression across Basic, Exclusion, Title, and Lyrics
- Evidence boundary: prompt structure is revised; audible results remain unverified until a new render is supplied

## Track 7 Revision 1

- Language: English, explicitly confirmed by user
- Narrative: after a 1:15 a.m. night shift, the driver takes an exhausted passenger home on a rainy river road, parks at 2:03 a.m., then wakes them
- Prosody: each 12-bar verse uses six two-bar lines, each eight-bar Chorus or Bridge uses four two-bar lines, and the 12-bar final Chorus expands to six lines
- Arrangement: filtered synth and reverse guitar open; percussion stays support-only; piano enters only at the Bridge; no violin or cello
- Status: draft-validated after deterministic validation and fresh bound lyric-content review; audible results remain unverified without a render

## Track 8 Revision 1

- Reference distillation: Paul Kim's `Every Day, Every Moment` supplies two complete Verse-Pre-Chorus-Chorus cycles before Bridge and final return; Heize's `You, Clouds, Rain` supplies slow minor harmonic color; Epik High feat. Younha's `Umbrella` supplies only the high-level rain-separation-return arc
- Narrative: after visiting hours, a daughter drives home with her mother's cardigan and discovers that care still travels in both directions
- Preserved locks: English lyrics, low A3-C5 lead, no high-note climax, narrow dynamics, large ambient space, support-only percussion, no violin or cello, and no piano-led intro
- Status: draft-validated after deterministic validation and fresh bound lyric-content review; audible results remain unverified without a render

## Track 9 Revision 1

- Language: English, explicitly confirmed by user
- Reference distillation: Yoon Mirae's `Always` supplies direct Verse-Chorus cycles; Jonghyun's `End of a Day` supplies major-center, relative-minor, and borrowed minor-subdominant behavior; Lee Hi's `HOLO` supplies the crowd-to-solitude acceptance arc and only a compact title-return hook model
- Narrative: after leaving a crowded hotel reception alone, the driver stops inventing an absent companion and discovers that the empty passenger seat is simply space
- Hook design: `Quiet, Not Lonely` opens and closes every Chorus on a newly composed five-note 3-3-2-1-2 motif with fixed rhythm; catchiness does not use higher pitch, louder singing, or added density
- Preserved locks: English lyrics, A3-C5 low lead, no high-note climax, narrow dynamics, large ambient space, support-only percussion, no violin or cello, no piano-led intro, and no respiratory lexical cues
- Status: draft-validated after deterministic validation and fresh independent lyric-content review 26/26 PASS; audible catchiness and mix remain unverified without a render; review: `reviews/track-09.json`
