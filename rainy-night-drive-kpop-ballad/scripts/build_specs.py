from __future__ import annotations

import json
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN_FIELDS = (
    "Style",
    "Feel",
    "Tempo/Groove",
    "Vocal",
    "Instrumentation",
    "Harmony",
    "Form/Flow",
    "Production/Mix",
)
FINGERPRINT_FIELDS = (
    "genre_lane",
    "form_id",
    "section_sequence",
    "recurrence",
    "entry",
    "groove_signature",
    "contrast_peak",
    "transition_interlude",
    "ending",
    "hook_return",
)
HOOK_RETURNS = (
    "No hook",
    "Repeated hook",
    "Varied return",
    "Final-only callback",
    "Instrumental hook",
)
HOOK_SEED = "rainy-night-drive-hook-v1"
HOOK_LEVEL_BAG = ["subtle"] * 3 + ["moderate"] * 4 + ["strong"] * 3
INSTRUMENTAL_TAGS = {"Intro", "Break", "Drop", "Outro", "Coda"}
EXCLUSION = "swing, walking bass, jazz comping, brushes, horns, scat, drum crescendos, notes above D5, belting"
TRACK_ONE_EXCLUSION = EXCLUSION
TRACK_THREE_EXCLUSION = "jazz backing, swing, walking bass, brushes, horns, scat, dense layers, nonstop drums, >C5, belting"
TRACK_FOUR_EXCLUSION = "jazz backing, swing, walking bass, brushes, horns, scat, >D5, belting"
TRACK_FIVE_EXCLUSION = "jazz backing, swing, brushes, horns, scat, violin, cello, piano intro, octave lift, >D5, belting"
TRACK_SIX_EXCLUSION = "jazz backing, swing, brushes, horns, scat, violin, cello, piano intro, percussion-led, >D5, belting"
TRACK_SEVEN_EXCLUSION = "jazz backing, swing, brushes, horns, scat, violin, cello, piano intro, percussion-led, >D5, belting"
TRACK_EIGHT_EXCLUSION = "jazz backing,swing,brushes,horns,scat,violin,cello,piano intro,percussion-led,>C5,belting"
TRACK_NINE_EXCLUSION = "jazz backing,swing,brushes,horns,scat,violin,cello,piano intro,percussion-led,>C5,belting"
TRACK_STYLES = (
    "Nocturnal K-pop ambient ballad",
    "Nocturnal K-pop ballad",
    "Rainy nocturnal K-pop ballad",
    "Rainy K-pop ballad with a restrained pop hook",
    "Rainy ambient-electronic K-pop OST ballad",
    "Dark ambient K-pop OST ballad",
    "Rainy dream-pop K-pop lullaby ballad",
    "Nocturnal ambient K-pop promise ballad",
    "Ambient K-pop ballad",
    "Nocturnal synth-pop K-pop OST ballad",
)
OPENING_SIGNATURES = (
    "felt piano | two-note gaps | vocal bar 5",
    "nylon guitar | broken thirds | vocal bar 5",
    "low synth | single-note pulses | vocal bar 5",
    "muted guitar | offbeat knocks | vocal bar 5",
    "guitar harmonics | alternating dyads | vocal bar 5",
    "mono bass | guitar-answer pedal | vocal bar 5",
    "reverse guitar | paired swells | vocal bar 5",
    "analog pad | guitar-answer chord | vocal bar 5",
    "lead voice | pad-unison onset | vocal bar 1",
    "FM bell | three-note sub-synth cell | vocal bar 5",
)
GROOVE_SIGNATURES = (
    "quarters | bass pickup to beat 1 | rim alternate bars",
    "straight eighths | guitar on 2-and | kick every 2 bars",
    "half notes | synth on beat 4 | full-bar drum gaps",
    "dotted eighths | guitar on 4-and | kick alternate bars",
    "two-beat cycle | bass before beat 3 | drums at section turns",
    "withheld downbeat | bass on beat 2 | tom every 4 bars",
    "even eighths | fourth-bar drop | kick on Chorus beat 1",
    "half-bar pulse | bass on 3-and | kick on first Chorus bars",
    "two-bar pulse | bass on beat 3 | kick alternate Chorus bars",
    "3+3+2 synth cell | bass across barline | kick at section turns",
)
TRACK_INSTRUMENTATIONS = (
    "felt piano | two-note gaps | vocal bar 5; ambient synth, round bass, rim support",
    "nylon guitar | broken thirds | vocal bar 5; warm bass, muted keys, soft kick",
    "low synth | single-note pulses | vocal bar 5; round bass, delayed sparse piano, rim support",
    "muted guitar | offbeat knocks | vocal bar 5; warm bass, muted synth answers, compact drums",
    "guitar harmonics | alternating dyads | vocal bar 5; ambient pad, mono bass, soft kick",
    "mono bass | guitar-answer pedal | vocal bar 5; low guitar, dark synth, recessed tom",
    "reverse guitar | paired swells | vocal bar 5; filtered pad, warm bass, support pulse",
    "analog pad | guitar-answer chord | vocal bar 5; rounded bass, delayed electric keys, recessed kick",
    "lead voice | pad-unison onset | vocal bar 1; low bass, Verse-2 muted guitar, recessed kick",
    "FM bell | three-note sub-synth cell | vocal bar 5; sustained guitar, warm bass, soft kick",
)
VOCAL_KO = (
    "Japanese modern female jazz alto A3-D5, mostly A3-C#5; clear natural Korean, "
    "stable tone, clean phrase joins, small intervals, D5 ceiling"
)
VOCAL_EN = (
    "Japanese modern female jazz alto A3-D5, centered A3-C#5; clear English, "
    "stable tone, clean joins, small intervals, restrained vibrato"
)


REFERENCES = [
    {
        "evidence_id": "E01",
        "artist": "Lee So-ra feat. SUGA",
        "track": "Song Request",
        "source": "https://www.akboclass.co.kr/uploads/cmallitemdetail/2019/01/4bfdec7c9d9d94dea881acf12039d4f7.pdf",
        "lane": "central-night-ballad",
        "form_id": "radio-build-ballad",
        "sequence": ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Chorus", "Outro"],
        "bars": [4, 12, 8, 8, 12, 8, 8, 8, 8, 4],
        "bpm": 88,
        "title": "Voice Beyond the Wipers",
        "scene": "심야 라디오가 고독을 조용한 동행으로 바꾼다",
        "differentiator": "피아노 모티프와 하행 베이스의 라디오형 빌드",
        "feel": "Rainy midnight drive; a radio voice softens solitude; steady low intensity",
        "instrumentation": "Felt piano, deep ambient synth bed, round bass, soft pop kit, diffuse guitar and strings",
        "harmony": "Bm; Verse Bm-Gmaj7-D/F#-A; Pre Em7-F#7-Bm-A/C#; Chorus Gmaj7-A-F#m7-Bm, Em7-A-Dmaj7-F#7; final G-A-D",
        "flow": "4-bar ambient entry; even density and low register; color-shift bridge; final return dissolves into rain",
        "mix": "Centered low lead, narrow dynamics, long dark reverb, air, soft transients, stable lows",
        "scope": "Primary mood reference; radio-night verse build and minor-to-relative-major relief; selected for rainy-drive emotional center",
    },
    {
        "evidence_id": "E02",
        "artist": "IU",
        "track": "Through the Night",
        "source": "https://www.kpopchords.com/2021/02/iu-through-night-chords.html",
        "lane": "intimate-pop-ballad",
        "form_id": "letter-refrain-ballad",
        "sequence": ["Intro", "Verse", "Chorus", "Verse", "Chorus", "Coda"],
        "bars": [4, 16, 12, 16, 12, 8],
        "bpm": 78,
        "title": "While the Light Stays Red",
        "scene": "보내지 못한 말이 붉은 신호 아래 편지처럼 머문다",
        "differentiator": "기타 아르페지오와 짧은 두 번의 후렴",
        "feel": "Rainy red light; an unsent confession held in patient motion",
        "instrumentation": "Nylon guitar arpeggio, muted piano, warm bass, soft straight pop percussion, distant strings",
        "harmony": "C; Verse C-Em7-Fmaj7-G; Chorus F-Fm-Em7-Am7-Dm7-G-C; coda Fm-C with descending inner voice",
        "flow": "4-bar guitar entry; long verse, compact chorus, long verse, compact chorus; 8-bar coda fades with the red light",
        "mix": "Centered low lead, narrow dynamics, gentle chorus bloom, tape haze, soft transients, steady drums",
        "scope": "Intimate form reference; long verse and compact chorus with minor-subdominant color; selected for low-energy contrast",
    },
    {
        "evidence_id": "E03",
        "artist": "Taeyeon",
        "track": "Rain",
        "source": "https://www.kpopchords.com/2022/05/taeyeon-rain-chords.html",
        "lane": "central-night-ballad",
        "form_id": "rain-memory-refrain",
        "sequence": ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Refrain", "Outro"],
        "bars": [4, 10, 6, 8, 10, 6, 8, 8, 8, 4],
        "bpm": 76,
        "title": "Past Your Exit",
        "scene": "돌려줄 열쇠를 들고 옛집으로 가다가 직접 만나지 않고 우편으로 보내기로 결정한다",
        "differentiator": "신스 펄스와 마지막 독립 리프레인",
        "feel": "Slow rainy drive; returning a spare key becomes quiet separation",
        "instrumentation": "Sparse piano, low synth, round bass; rim and kick in choruses; single strings at turns",
        "harmony": "Dm(add9); Verse Dm-C/E-Bbmaj7-F/A; Pre Gm7-Dm/F-Eb-Asus4-A; Chorus Bbmaj7-C-Am7-Dm, Gm7-Asus4-Dm; Refrain Bb-C-Dm-Dm/C; two-bar changes, descending bass, suspended cadences",
        "flow": "Near-empty intro; half-bar vocal rests; one-bar air before choruses; drumless bridge; standalone refrain; bare outro",
        "mix": "Centered low lead, clean phrase gaps, intermittent ambience, short dark tails, centered lows, narrow dynamics, soft transients",
        "scope": "Rain-memory structure reference; recurring build and late independent refrain; harmony adapted away from jazz accompaniment",
    },
    {
        "evidence_id": "E04",
        "artist": "AKMU",
        "track": "How Can I Love the Heartbreak, You're the One I Love",
        "source": "https://www.kpopchords.com/2020/10/akmu-how-can-i-love-chords.html",
        "lane": "intimate-pop-ballad",
        "form_id": "narrative-coda-ballad",
        "sequence": ["Intro", "Verse", "Pre-Chorus", "Chorus", "Break", "Verse", "Pre-Chorus", "Chorus", "Coda"],
        "bars": [4, 12, 8, 12, 4, 12, 8, 12, 8],
        "bpm": 82,
        "title": "Not That Exit Again",
        "scene": "An old address still saved as Home stops controlling the route",
        "differentiator": "A four-note descending title hook stays catchy at low volume; the coda alone names the new home",
        "feel": "Steady rainy drive; breaking the habit of returning to an old address",
        "instrumentation": "Muted piano stabs, palm-muted guitar, warm bass, compact chorus drums, low cello replies",
        "harmony": "F#m; Verse F#m-D-A/E-E; Pre Bm-D-E-C#sus4-C#; Chorus A-E/G#-F#m-D, Bm-C#7-F#m; Coda D-E-C#m-F#m-Bm-C#-F#m",
        "flow": "Muted-guitar entry; four-note descending title hook on a fixed syncopated rhythm; four-bar break; varied second chorus opens into the concluding coda",
        "mix": "Centered low lead, clean silent phrase gaps, centered acoustic core, narrow dynamics, soft transients, coda-only stereo lift",
        "scope": "Narrative form reference; verse-pre-chorus storytelling and extended coda; selected for acceptance arc and diatonic clarity",
    },
    {
        "evidence_id": "E05",
        "artist": "Ailee",
        "track": "I Will Go to You Like the First Snow",
        "source": "https://www.kpopchords.com/2021/02/ailee-first-snow-chords.html",
        "lane": "dramatic-ost-ballad",
        "form_id": "modulating-peak-ballad",
        "sequence": ["Intro", "Verse", "Chorus", "Break", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
        "bars": [4, 12, 8, 4, 12, 8, 8, 12, 4],
        "bpm": 84,
        "title": "Under the Station Light",
        "scene": "A driver crosses the rainy city to collect her younger sister after the last bus fails to arrive",
        "differentiator": "A final semitone modulation changes harmonic color while the melody stays in the same low register",
        "feel": "Cold rain; collecting a stranded sister restores connection",
        "instrumentation": "Muted guitar harmonics, ambient pad, mono bass, soft electronic kick; low piano after Break",
        "harmony": "C#m(add9); Verse C#m-E/B-Amaj7-G#sus4; Chorus F#m-A-E/G#-C#m, D-B-G#7; Bridge A-F#m-Bsus4-C#sus4; final Dm: Gm-Bb-F/A-Dm, Eb-C-A7-Dm",
        "flow": "Guitar-harmonic and pad intro; two restrained cycles and four-bar break; semitone bridge pivot; same-register final title chorus; short outro",
        "mix": "Centered low lead, narrow dynamics, flat density, wide dark ambience, clear gaps, soft transients, centered lows",
        "scope": "Dramatic K-ballad reference; direct chorus and late modulation; selected for a harmonic-color crest without jazz arranging",
    },
    {
        "evidence_id": "E06",
        "artist": "Davichi",
        "track": "This Love",
        "source": "https://www.kpopchords.com/2020/12/davichi-this-love-chords.html",
        "lane": "dramatic-ost-ballad",
        "form_id": "triple-lift-ost-ballad",
        "sequence": ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Pre-Chorus", "Chorus", "Outro"],
        "bars": [4, 8, 8, 8, 8, 8, 8, 8, 8, 8, 4],
        "bpm": 82,
        "title": "What You Meant Was Care",
        "scene": "A driver safely parks and apologizes after mistaking a partner's flood-route warning for control",
        "differentiator": "A low guitar ostinato and recurring withheld downbeat delay the direct apology until the final return",
        "feel": "Rainy ring road; concern misread as control becomes a parked-car apology",
        "instrumentation": "Low electric-guitar ostinato, mono bass drone, diffuse dark synth; recessed floor tom support",
        "harmony": "Gm(add9); Verse Gm-Ebmaj7-Bb/F-F; Pre Cm-Eb-Dsus4-D; Chorus Eb-F-Dm-Gm-Cm-D7-Gm; Bridge Bb/F-Ebmaj7-Cm-Dsus4",
        "flow": "Guitar-bass intro; four two-bar lyric lines per 8-bar vocal section; fixed chorus rhythm and word stress; pre-choruses delay the downbeat; near-empty bridge; final apology at flat density; short close",
        "mix": "Centered low lead, narrow dynamics, flat density, dark ambience, recessed floor tom, mono lows",
        "scope": "OST build reference; repeated pre-chorus and delayed final arrival; selected for restrained dramatic pacing",
    },
    {
        "evidence_id": "E07",
        "artist": "IU",
        "track": "Lullaby",
        "source": "https://www.kpopchords.com/2022/05/iu-lullaby-chords.html",
        "lane": "intimate-pop-ballad",
        "form_id": "lullaby-bridge-coda",
        "sequence": ["Intro", "Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Coda"],
        "bars": [4, 12, 8, 12, 8, 8, 12, 8],
        "bpm": 80,
        "title": "I'll Keep the Road Quiet",
        "scene": "A driver takes an exhausted night-shift passenger home without disturbing their sleep",
        "differentiator": "Filtered synth and reverse guitar hold the quietest interior point before the coda fully releases the final chorus",
        "feel": "Rainy post-shift drive; an exhausted passenger sleeps through an even ride home",
        "instrumentation": "Filtered synth pad, reverse guitar, warm bass; support-only pulse; bridge piano",
        "harmony": "Eb; Verse Eb-Fm-Gm-Am7b5-Bb7; Chorus Ab-Bb-Gm-Cm-Fm-Bb; Bridge Cm-Abm-Eb/Bb-Bbsus; coda Abm-Eb",
        "flow": "Reverse-guitar intro; six two-bar lines per verse, four per chorus or bridge; chromatic bass links returns; bridge piano suspends pulse; six-line final chorus; eight-bar coda",
        "mix": "Centered low lead, narrow dynamics, dim top, slow stereo opening, quiet lows, long dark tail, soft transients",
        "scope": "Lullaby form reference; delayed harmonic resolution and releasing coda; selected for the playlist's quietest interior point",
    },
    {
        "evidence_id": "E08",
        "artist": "Paul Kim",
        "track": "Every Day, Every Moment",
        "source": "https://www.kpopchords.com/2021/11/paul-kim-every-day-every-moment-chords.html",
        "lane": "central-night-ballad",
        "form_id": "promise-return-ballad",
        "sequence": ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Pre-Chorus", "Chorus", "Bridge", "Chorus", "Coda"],
        "bars": [4, 8, 4, 8, 8, 4, 8, 6, 12, 4],
        "bpm": 74,
        "title": "Same Time Next Sunday",
        "scene": "After visiting hours, a daughter drives home through light rain carrying her mother's cardigan and the promise to return next Sunday",
        "differentiator": "A low five-note title hook returns unchanged while the ordinary care once received from her mother is discovered in reverse",
        "feel": "Rainy drive after visiting; separation becomes a kept promise",
        "instrumentation": "Low pad and bass open; clean guitar motif with voice; electric piano after Chorus 1; recessed support-only kick",
        "harmony": "Cm(add9); Verse Cm-Ab-Eb/Bb-Bbsus; Pre Fm-Cm/Eb-Db-Gsus-G; Chorus Eb/G-Ab-Cm/Bb-Bb, Fm-Abm6-Eb/Bb-G; Bridge Ab-Eb/G-Fm-Cm/Eb-Db-Bb",
        "flow": "Pad-bass intro; two eight-bar Verse-Pre-Chorus-Chorus cycles; six-bar Bridge; twelve-bar final Chorus expands the same low five-note title hook; four-bar close",
        "mix": "Centered low lead; narrow dynamics, dark wide ambience, empty sides, flat Chorus density, soft transients",
        "scope": "Structure role only: two complete Verse-Pre-Chorus-Chorus cycles lead to a Bridge and final Chorus",
    },
    {
        "evidence_id": "E09",
        "artist": "Yoon Mirae",
        "track": "Always",
        "source": "https://www.kpopchords.com/2021/01/yoon-mirae-always-chords.html",
        "lane": "central-night-ballad",
        "form_id": "voice-first-relief-ballad",
        "sequence": ["Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Coda"],
        "bars": [12, 10, 10, 10, 8, 12, 4],
        "bpm": 74,
        "title": "Quiet, Not Lonely",
        "scene": "After leaving a crowded hotel reception alone, the driver finds that unexamined solitude feels kinder than having to explain herself",
        "differentiator": "Lead and pad enter together on bar one; a five-note low title motif makes quiet relief catchy without raising intensity",
        "feel": "Rainy post-reception drive; solitude becomes relief",
        "instrumentation": "Lead and low pad enter on bar one; bass after line one; muted guitar in Verse 2; recessed support-only kick in Choruses",
        "harmony": "Bb(add9); Verse Bb-F/A-Gm-Eb(add9); Chorus Eb-F-Dm-Gm-Cm-Ebm-Bb/F-Fsus; Bridge Gm-Dm-Eb-Bb/D-Cm-Fsus-F; Coda Ebm(add9)",
        "flow": "Voice starts bar one; 12-bar Verse, 10-bar Chorus, then 10-bar Verse and Chorus; 8-bar Bridge; 12-bar final Chorus; 4-bar Coda; each Chorus opens and closes with a new low five-note 3-3-2-1-2 motif in fixed rhythm",
        "mix": "Centered low lead; narrow dynamics, dark wide ambience, empty sides, flat Chorus density, soft transients",
        "scope": "Structure role only: direct Verse-Chorus cycles begin with the voice, followed by a Bridge and final Chorus; the Coda is an original addition",
    },
    {
        "evidence_id": "E10",
        "artist": "Crush",
        "track": "Beautiful",
        "source": "https://www.kpopchords.com/2020/10/crush-beautiful-chords.html",
        "lane": "dramatic-ost-ballad",
        "form_id": "hook-led-final-ballad",
        "sequence": ["Intro", "Verse", "Hook", "Verse", "Hook", "Bridge", "Chorus", "Outro"],
        "bars": [4, 12, 8, 12, 8, 8, 16, 4],
        "bpm": 82,
        "title": "비가 멎기 전까지",
        "scene": "새벽이 가까워질수록 상실을 놓고 앞으로 달려간다",
        "differentiator": "짧은 훅은 두 번만, 완전한 코러스는 마지막에만 등장",
        "feel": "The last rainy miles before dawn; grief loosens and the road finally opens",
        "instrumentation": "Sub-synth swell, sustained clean guitar, electric bass, soft straight pop drums, muted keyboard color",
        "harmony": "F#; Verse F#-A#m-D#m-B; Hook B-C#-A#m-D#m; Bridge G#m-C#-F#-D#m-B-C#; final F#-C#/E#-D#m-B-Bm-F#",
        "flow": "FM-bell and sub-synth entry; two verse-hook cycles; bridge turns darker; the only full chorus arrives at the end and resolves into four quiet bars",
        "mix": "Dark verses, diffuse final color under the same ceiling, soft drum transients, warm low mids, centered low lead",
        "scope": "Hook-led OST reference; repeated compact hook before a final full chorus; selected as the playlist's dawn-facing resolution",
    },
]


SUPPORTING_REFERENCES = [
    {
        "evidence_id": "E11",
        "artist": "Heize feat. Shin Yong Jae",
        "track": "You, Clouds, Rain",
        "source": "https://www.guitartabsexplorer.com/heize-kr/you-clouds-rain-chords",
        "lane": "intimate-pop-ballad",
        "scope": "Harmony role for Track 8: slow minor-centered rhythm, major-seventh color, secondary-dominant pull, and a brief darkened subdominant; distilled without copying the source progression",
    },
    {
        "evidence_id": "E12",
        "artist": "Epik High feat. Younha",
        "track": "Umbrella",
        "source": "https://www.soompi.com/article/1045057wpp/epik-high-lyrics-will-hit-home-every-listen",
        "lane": "central-night-ballad",
        "scope": "Emotional-arc role for Track 8: rain intensifies separation, recurring returns keep the absent bond present, and the ending accepts distance without severing care",
    },
    {
        "evidence_id": "E13",
        "artist": "Jonghyun",
        "track": "End of a Day",
        "source": "https://chordu.com/chords-tabs-jonghyun-%EC%A2%85%ED%98%84-%ED%95%98%EB%A3%A8%EC%9D%98-%EB%81%9D-end-of-a-day-mv-id_wGP-gfCWXYI",
        "lane": "intimate-pop-ballad",
        "scope": "Harmony role for Track 9: a major center softens through relative-minor motion, borrowed minor-subdominant color, and direct cadential release; distilled without copying the source progression",
    },
    {
        "evidence_id": "E14",
        "artist": "Lee Hi",
        "track": "HOLO",
        "source": "https://www.soompi.com/article/1412368wpp/lee-hi-teases-what-may-be-her-1st-comeback-since-leaving-yg-entertainment",
        "lane": "intimate-pop-ballad",
        "scope": "Emotional-arc and secondary hook-model role for Track 9: loneliness among other people gives way to self-directed acceptance; only a compact title-centered return is distilled for catchiness, with no source melody, lyric, or image reused",
    },
]

ALL_REFERENCES = [*REFERENCES, *SUPPORTING_REFERENCES]

REFERENCE_TRIOS = {
    1: (("structure", "E01", "Radio-style verse build and color-shift bridge"), ("harmony", "E03", "Minor center, descending bass, and suspended cadence behavior"), ("emotional_arc", "E10", "Loss loosens through continued forward motion")),
    2: (("structure", "E02", "Long verse and compact refrain with a short coda"), ("harmony", "E04", "Diatonic clarity darkened by a minor-subdominant turn"), ("emotional_arc", "E01", "A remote voice turns solitude into temporary company")),
    3: (("structure", "E03", "Recurring build followed by a separate late refrain"), ("harmony", "E07", "Delayed resolution and chromatic bass connection"), ("emotional_arc", "E04", "A repeated habit yields to a final act of acceptance")),
    4: (("structure", "E04", "Two narrative cycles release into an extended coda"), ("harmony", "E02", "Minor-subdominant color shadows an otherwise clear tonal frame"), ("emotional_arc", "E03", "Rain revives a memory before a deliberate separation choice")),
    5: (("structure", "E05", "Restrained cycles prepare a late transformed final chorus"), ("harmony", "E06", "Dominant tension supports a dramatic turn without jazz motion"), ("emotional_arc", "E02", "Private concern becomes a direct promise of arrival")),
    6: (("structure", "E06", "Repeated pre-choruses delay the final direct statement"), ("harmony", "E03", "Minor add-nine color and suspended dominant release"), ("emotional_arc", "E05", "Defensiveness gives way to open care at the final return")),
    7: (("structure", "E07", "Two returns expand into a longer final chorus and coda"), ("harmony", "E01", "Chromatic bass motion links restrained minor and relative-major color"), ("emotional_arc", "E02", "Quiet protection is proved through an ordinary completed act")),
    8: (("structure", "E08", "Two complete Verse-Pre-Chorus-Chorus cycles lead to a Bridge and final Chorus"), ("harmony", "E11", "Slow minor-centered rhythm, major-seventh color, secondary-dominant pull, and a darkened subdominant"), ("emotional_arc", "E12", "Rain deepens separation; recurring returns preserve the bond; the ending accepts distance without ending care")),
    9: (("structure", "E09", "Direct Verse-Chorus cycles begin with the voice, then move through Bridge and final Chorus"), ("harmony", "E13", "A major center softens through relative-minor motion, borrowed minor-subdominant color, and direct cadence"), ("emotional_arc", "E14", "Hook model: compact title-centered return plus an arc from loneliness among people to self-directed acceptance; write a new note sequence")),
    10: (("structure", "E10", "Two compact hooks defer the only full chorus to the end"), ("harmony", "E05", "Late tonal transformation creates a final color crest"), ("emotional_arc", "E09", "Immediate address moves grief toward a dawn-facing release")),
}


BASE_BEHAVIORS = [
    {
        "recurrence": "two full chorus returns followed by a lyrically varied final return",
        "entry": OPENING_SIGNATURES[0],
        "groove_signature": GROOVE_SIGNATURES[0],
        "contrast_peak": "the bridge changes spectral color while the voice stays below D5 and the final return keeps the same narrow loudness ceiling",
        "transition_interlude": "each pre-chorus adds harmonic color while holding drum density, loudness, and the low vocal register steady",
        "ending": "four ambient instrumental bars dissolve the piano fragments into rain",
        "hook_return": "Varied return",
    },
    {
        "recurrence": "two compact chorus returns carry the same central confession",
        "entry": OPENING_SIGNATURES[1],
        "groove_signature": GROOVE_SIGNATURES[1],
        "contrast_peak": "the second chorus is the emotional ceiling rather than a large climax",
        "transition_interlude": "verse endings thin before each direct chorus arrival",
        "ending": "an eight-bar instrumental coda releases the suspended light",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "two choruses lead to a separate late refrain",
        "entry": OPENING_SIGNATURES[2],
        "groove_signature": GROOVE_SIGNATURES[2],
        "contrast_peak": "the standalone refrain becomes the peak after a drumless bridge",
        "transition_interlude": "pre-choruses tighten the pulse and lift the inner line",
        "ending": "a short pulse-and-piano outro closes the reflected image",
        "hook_return": "Final-only callback",
    },
    {
        "recurrence": "two chorus statements defer the final conclusion to the coda",
        "entry": OPENING_SIGNATURES[3],
        "groove_signature": GROOVE_SIGNATURES[3],
        "contrast_peak": "the second chorus opens into the coda instead of another peak",
        "transition_interlude": "a four-bar instrumental break separates the two narrative halves",
        "ending": "the coda states the acceptance and resolves the deceptive motion",
        "hook_return": "Varied return",
    },
    {
        "recurrence": "two restrained choruses prepare one transposed final chorus",
        "entry": OPENING_SIGNATURES[4],
        "groove_signature": GROOVE_SIGNATURES[4],
        "contrast_peak": "the bridge changes harmonic color before a same-register final chorus under the same loudness ceiling",
        "transition_interlude": "a short instrumental break resets the dynamic floor",
        "ending": "four bars sustain the new key after the final lyric",
        "hook_return": "Final-only callback",
    },
    {
        "recurrence": "three chorus arrivals are each delayed by a pre-chorus",
        "entry": OPENING_SIGNATURES[5],
        "groove_signature": GROOVE_SIGNATURES[5],
        "contrast_peak": "the bridge darkens before a third pre-chorus withholds the final downbeat",
        "transition_interlude": "pre-choruses use dominant tension as the recurring hinge",
        "ending": "a short firm close follows the final confession",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "two chorus returns expand into one longer final chorus",
        "entry": OPENING_SIGNATURES[6],
        "groove_signature": GROOVE_SIGNATURES[6],
        "contrast_peak": "the bridge suspends the pulse rather than increasing loudness",
        "transition_interlude": "chromatic bass motion connects each verse to its chorus",
        "ending": "the coda resolves the open dominant and lets the city lights fade",
        "hook_return": "Varied return",
    },
    {
        "recurrence": "two complete verse-pre-chorus-chorus cycles lead to a bridge and expanded final return",
        "entry": OPENING_SIGNATURES[7],
        "groove_signature": GROOVE_SIGNATURES[7],
        "contrast_peak": "the bridge changes harmonic color while the exact title hook stays in the same low register and loudness ceiling",
        "transition_interlude": "both pre-choruses shorten the wording and hold density before the title hook",
        "ending": "four bars hold the unresolved minor-add-nine color after the promise",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "three direct chorus returns arrive without pre-choruses",
        "entry": OPENING_SIGNATURES[8],
        "groove_signature": GROOVE_SIGNATURES[8],
        "contrast_peak": "the bridge changes perspective before the final chorus repeats the same new five-note title motif in the low register",
        "transition_interlude": "short verse endings turn directly into the chorus downbeat",
        "ending": "a four-bar coda holds the borrowed minor-subdominant after self-acceptance",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "two compact hooks prepare a single full final chorus",
        "entry": OPENING_SIGNATURES[9],
        "groove_signature": GROOVE_SIGNATURES[9],
        "contrast_peak": "the only full chorus is reserved for the ending after a darker bridge",
        "transition_interlude": "each short hook returns quickly to narrative motion",
        "ending": "four quiet bars turn the parallel-minor color back toward dawn",
        "hook_return": "Final-only callback",
    },
]


TRACK_ONE_LYRICS = """[Intro]

[Verse]
It's twelve fifteen; I leave the block
Where we agreed we would not try again
The final message waits beneath the map
I turn the radio above the rain
The midnight host reads notes from other drivers
One asks to hear a quiet song for home

[Pre-Chorus]
The host says this is for the ones still driving
A piano starts inside the dashboard
I keep both hands upon the steering wheel
And let the unread message wait

[Chorus]
Voice beyond the wipers, stay a while
Keep talking while the wet signs pass
You do not have to say that I'll be fine
Just stay until I reach my building

[Verse]
I take the river road instead of the shortcut
The station fades inside the underpass
I scan the dial until the host returns
Then merge into the right-hand lane
She says the rain should ease before the morning
I pass the bridge and see my exit sign

[Pre-Chorus]
My phone lights up, but I do not reach for it
The host gives the time as twelve forty-three
For the remaining miles I need one voice
That asks for nothing from me

[Chorus]
Voice beyond the wipers, stay a while
Keep talking while the wet signs pass
You do not have to say that I'll be fine
Just stay until I reach my building

[Bridge]
I park beneath my building after one
The host is reading one last driver's note
I switch the engine off when she says goodnight
Then carry my phone inside without replying

[Chorus]
Voice beyond the wipers, you stayed a while
And kept talking while the wet signs passed
You never had to say that I'll be fine
You only stayed until I reached my building

[Outro]"""

TRACK_FOUR_LYRICS = """[Intro]

[Verse]
The map still calls your apartment Home
I never changed it after I moved out
Rain gathers at the edge of the windshield
The blue route leads me toward the western ramp
For three straight weeks I followed it from habit
Then turned around beside the all-night store
Tonight the same green exit sign is coming
I move one lane left before the split

[Pre-Chorus]
My hand still reaches for the turn signal
Then settles back upon the wheel
The lane beside me bends toward your street
The one ahead keeps carrying me south

[Chorus]
Not that exit again
Not that exit again
I know every turn and where it ends
But that address is not my home
Not that exit again
This time I let the ramp go by

[Break]

[Verse]
I stop beneath the lights of a gas station
The rain taps softly on the metal roof
I open saved places on the dashboard
And change the word Home to my current street
The screen redraws the route toward the river
No U-turn asks me to go back
I put the phone face down beside me
Then pull out when the road is clear

[Pre-Chorus]
The old exit is behind me now
The new route keeps a steady line
I do not need to circle back
To prove the ending happened

[Chorus]
Not that exit again
Not that exit again
I know every turn and where it ends
And that address is not my home
Not that exit again
I keep driving past the sign

[Coda]
The map now says eleven minutes
To the room where I sleep tonight
When the route says Home at the final corner
For the first time, it means mine"""

TRACK_FIVE_LYRICS = """[Intro]

[Verse]
It's eleven forty when my sister calls
The last bus never came on Terminal Road
The station clerk has locked the waiting room
She stands beneath the canopy alone
I clear the bags off the passenger seat
Turn on the heater and start the car
The traffic map marks water on the low road
So I take the northern hill instead

[Chorus]
Stay under the station light
Stay under the station light
Keep your yellow hood where I can see it
I'm ten minutes down the road
Stay under the station light
I'll be there before the rain lets up

[Break]

[Verse]
The hill road bends above the flooded crossing
The dashboard counts the minutes down from eight
Your message plays through the car speakers
You say the rain is blowing through the roof
I turn the heater higher on your side
And keep below the posted warning speed
At the crest I see the terminal clock
Then your yellow coat beside the gate

[Chorus]
Stay under the station light
Stay under the station light
Keep your yellow hood where I can see it
I'm two minutes down the road
Stay under the station light
I'm turning onto Terminal Road

[Bridge]
I spent this winter keeping to myself
Letting every call go to voicemail
But the passenger side is warm tonight
And I know exactly who I'm driving for

[Chorus]
Under the station light
Under the station light
I can see your yellow coat
I'm pulling in beside the gate
Under the station light
You open the door and climb inside

[Outro]"""

TRACK_SIX_LYRICS = """[Intro]

[Verse]
At twelve twenty, I drive from your building
You said the low road was under water
I said I didn't need another guide
Your message said, let me know when you're home

[Pre-Chorus]
The ring road climbs past loading yards
The flood barriers close the road
Both hands stay steady on the wheel
Your warning starts to sound like care

[Chorus]
What you meant was only care
You were pointing to the safe road
I treated kindness as control
I save my answer till I park

[Verse]
At twelve thirty-four, I reach the plaza
I take the access lane beneath the rain
I park the car beneath the canopy
I shut the engine down; phone stays mounted

[Pre-Chorus]
I hear the words I used outside
Stop telling me which road to take
You only named the safer way
I made your care into a fight

[Chorus]
What you meant was only care
You were pointing to the safe road
I treated kindness as control
I draft my answer while I'm parked

[Bridge]
I open your message in the car
I type, You were right about the road
Then clear the line; I owe you more
I'm sorry I turned care into a fight

[Pre-Chorus]
The service plaza stays quiet
I read the message one more time
The plainest words are true enough
I send the words and let them wait

[Chorus]
What you meant was only care
You were pointing to the safe road
I treated kindness as control
I send my answer, then drive home

[Outro]"""

TRACK_SEVEN_LYRICS = """[Intro]

[Verse]
At one fifteen, you finish the late shift
You close the door and fasten your seat belt
You say the headache has not left
I dim the dash and take the river road
The rain stays steady; both lanes are clear
Before the bridge, your eyes fall shut

[Chorus]
Sleep through the lights, I'll keep the road quiet
I'll take each turn at an even pace
Nothing needs saying before we get home
Sleep through the lights, I'll keep the road quiet

[Verse]
An empty bus pulls out beside the depot
The road narrows after we cross the bridge
I keep below the posted speed
You wake once when the signal changes
I say we're ten minutes from home
You nod, then settle against the seat

[Chorus]
Sleep through the lights, I'll keep the road quiet
I'll take each turn at an even pace
Nothing needs saying before we get home
Sleep through the lights, we're nearly home now

[Bridge]
At two-oh-three, our street appears
The bakery sign is already dark
I take the ramp beneath our building
Then park the car before I wake you

[Chorus]
You slept through the lights; I kept the road quiet
I took each turn at an even pace
Nothing needed saying before we came home
I switch the engine off beneath our building
I touch your shoulder and say, we're here
You open your eyes; the road is still

[Coda]"""

TRACK_EIGHT_LYRICS = """[Intro]

[Verse]
Nine o'clock is glowing on the lobby wall
Your crossword waits unfinished by the chair
You give me your blue cardigan to mend
And press two lemon drops into my hand

[Pre-Chorus]
You catch my sleeve and ask me once again
I say, next Sunday, and you nod

[Chorus]
Same time next Sunday
Before the seven o'clock news
I'll bring your cardigan; we'll finish the page
Same time next Sunday

[Verse]
The cardigan lies folded on the seat
Your lobby window fades behind the rain
The city makes a quiet mile between us
At nine-thirty, I pull in at home

[Pre-Chorus]
I set your cardigan beside my keys
The lemon drops remain inside my hand

[Chorus]
Same time next Sunday
Before the seven o'clock news
I'll bring your cardigan; we'll finish the page
Same time next Sunday

[Bridge]
You packed these sweets in every school lunch
One small habit crossed the years with me
You lost the date, but not the way you care

[Chorus]
Same time next Sunday
Before the seven o'clock news
I'll bring your cardigan; we'll finish the page
If Sunday slips away from you
I'll remember it for us
Same time next Sunday

[Coda]"""

TRACK_NINE_LYRICS = """[Verse]
The band is packing up at eleven ten
I say goodnight beside the ballroom doors
Someone asks again if I came alone
I smile and say my friend was running late
Outside, the hotel awning holds the rain
I wait there while the valet brings my car

[Chorus]
Quiet, not lonely
The rain is all I hear
No one asking who I'm waiting for
No story I have to give
Quiet, not lonely

[Verse]
The hotel sign grows smaller in the mirror
I turn the radio off before the bridge
The empty passenger seat beside me
Is only space, not proof I was forgotten
I drive with nothing left to explain

[Chorus]
Quiet, not lonely
The rain is all I hear
No one asking who I'm waiting for
No story I have to give
Quiet, not lonely

[Bridge]
I was lonelier under those chandeliers
Than here between the darkened signs
I don't need every room to know my story
I let this quiet belong to me

[Chorus]
Quiet, not lonely
The rain is all I hear
No one asking who I'm waiting for
No story I have to give
The empty seat is only space
Quiet, not lonely

[Coda]"""

TRACK_TWO_LYRICS = """[Intro]

[Verse]
It's nearly two, I'm stopped at a red light
The wipers clear the glass, then rain returns
Your final message is still on my phone
I read it once and set the phone face down
You said we should stop trying to fix us
I knew you meant it when I left your place
The car ahead is waiting at the light
For ten more seconds I can wait here too

[Chorus]
Stay red a little longer
I'm not ready to go home
I know you won't be waiting when I get home
And stopping here won't change the way it ended
Stay red a little longer
Give me one more minute to let go

[Verse]
I take the long way south along the river
The gas station is closing for the night
I almost call you when I reach the bridge
Then keep my hands at ten and two instead
The phone stays face down on the passenger seat
At the next intersection traffic stops again
This time I pause before I read your message
And know I can finish the drive alone

[Chorus]
Stay red a little longer
Then I'll take the road back home
I know you won't be waiting when I get home
And stopping here won't change the way it ended
Stay red a little longer
I'll leave when the light turns green

[Coda]"""

TRACK_THREE_LYRICS = """[Intro]

[Verse]
Your spare key rests inside the cup holder
You asked me to leave it with the guard
The map says twelve more minutes to your building
Rain slows the traffic on the boulevard
I told you I would bring it by tonight
So I keep following the route across town

[Pre-Chorus]
The navigation says the exit is approaching
I move one lane left and pass the ramp
The route begins to search for a new way
I turn the guidance down with my hand

[Chorus]
I drive past your exit
I keep going straight
I'll send the key tomorrow
I don't need to see your place
I drive past your exit
And let the map update

[Verse]
At the next red light your message reaches me
It asks if I have left the key downstairs
I type that I will mail it in the morning
Then put the phone back in its stand
The screen redraws a shorter road toward home
The rain is lighter on this side of town

[Pre-Chorus]
I place the key inside the glove box
The small metallic rattle stops
The route no longer points toward your building
I follow it across the blocks

[Chorus]
I drive past your exit
I keep going straight
I'll send the key tomorrow
I don't need to see your place
I drive past your exit
And let the map update

[Bridge]
I thought returning it in person
Would make the ending feel complete
But an envelope can carry back the key
Without bringing me to your street

[Refrain]
Past your exit, past your street
The route is pointing home
The key can wait until tomorrow
Tonight I leave your road alone

[Outro]"""


def projection(candidate: dict[str, object]) -> dict[str, object]:
    return {field: candidate[field] for field in FINGERPRINT_FIELDS}


def write_json(path: Path, value: object) -> None:
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def hook_levels() -> list[str]:
    levels = list(HOOK_LEVEL_BAG)
    random.Random(HOOK_SEED).shuffle(levels)
    return levels


def low_dynamic_flow(reference: dict[str, object], hook_level: str) -> str:
    return f"{reference['flow']}; {hook_level} hook prominence"


def effective_hook_level(slot: int, seeded_level: str) -> str:
    return "strong" if slot == 4 else seeded_level


def reference_ids_for_slot(slot: int) -> list[str]:
    return [evidence_id for _role, evidence_id, _trait in REFERENCE_TRIOS[slot]]


def reference_bindings_for_slot(slot: int) -> list[dict[str, str]]:
    return [
        {"role": role, "evidence_id": evidence_id, "distilled_trait": trait}
        for role, evidence_id, trait in REFERENCE_TRIOS[slot]
    ]


def build_candidates() -> tuple[list[dict[str, object]], list[dict[str, object]]]:
    candidates: list[dict[str, object]] = []
    envelopes: list[dict[str, object]] = []
    inserted_tags = (None, "Break", "Refrain", "Drop", "Hook")
    candidate_number = 1

    for slot, reference in enumerate(REFERENCES, start=1):
        base_behavior = BASE_BEHAVIORS[slot - 1]
        envelope_candidates: list[dict[str, object]] = []
        for variant, inserted_tag in enumerate(inserted_tags):
            base = list(reference["sequence"])
            sequence = base if inserted_tag is None else [*base[:-1], inserted_tag, base[-1]]
            candidate = {
                "candidate_id": f"C{candidate_number:03d}",
                "genre_lane": reference["lane"],
                "form_id": reference["form_id"],
                "envelope_id": f"V{slot:02d}",
                "evidence_ids": reference_ids_for_slot(slot),
                "section_sequence": sequence,
                "recurrence": base_behavior["recurrence"] if variant == 0 else f"slot-{slot:02d}-variant-{variant}-return-logic",
                "entry": base_behavior["entry"] if variant == 0 else f"lead-{slot:02d}-{variant} | gesture-{slot:02d}-{variant} | vocal-{slot:02d}-{variant}",
                "groove_signature": base_behavior["groove_signature"] if variant == 0 else f"pulse-{slot:02d}-{variant} | accent-{slot:02d}-{variant} | support-{slot:02d}-{variant}",
                "contrast_peak": base_behavior["contrast_peak"] if variant == 0 else f"slot-{slot:02d}-variant-{variant}-peak-curve",
                "transition_interlude": base_behavior["transition_interlude"] if variant == 0 else f"slot-{slot:02d}-variant-{variant}-transition-path",
                "ending": base_behavior["ending"] if variant == 0 else f"slot-{slot:02d}-variant-{variant}-ending-shape",
                "hook_return": base_behavior["hook_return"] if variant == 0 else HOOK_RETURNS[(slot + variant - 1) % len(HOOK_RETURNS)],
            }
            candidates.append(candidate)
            envelope_candidates.append(candidate)
            candidate_number += 1

        envelopes.append(
            {
                "id": f"V{slot:02d}",
                "genre_lane": reference["lane"],
                "form_id": reference["form_id"],
                "evidence_ids": reference_ids_for_slot(slot),
                "permitted_combinations": [projection(item) for item in envelope_candidates],
                "forbidden_combinations": [],
            }
        )
    return candidates, envelopes


def build_catalog(candidates: list[dict[str, object]], envelopes: list[dict[str, object]]) -> dict[str, object]:
    lanes = []
    for lane_id, label in (
        ("central-night-ballad", "central rainy-night K-pop ballad"),
        ("intimate-pop-ballad", "intimate acoustic-adjacent K-pop ballad"),
        ("dramatic-ost-ballad", "dramatic cinematic K-pop OST ballad"),
    ):
        lanes.append(
            {
                "id": lane_id,
                "label": label,
                "evidence_ids": [
                    ref["evidence_id"] for ref in ALL_REFERENCES if ref["lane"] == lane_id
                ],
            }
        )

    return {
        "catalog_revision": "rainy-night-kpop-ballad-web-v3",
        "genre_coordinate": "K-pop ballad for rainy night driving; Japanese modern female jazz vocal character; non-jazz accompaniment; narrow arrangement dynamics and low vocal register",
        "evidence": [
            {
                "id": ref["evidence_id"],
                "source": ref["source"],
                "kind": "real-song",
                "artist": ref["artist"],
                "track": ref["track"],
                "scope": f"{ref['artist']} — {ref['track']}; {ref['scope']}",
            }
            for ref in ALL_REFERENCES
        ],
        "genre_lanes": lanes,
        "variation_envelopes": envelopes,
        "diversity_contract": {
            "candidate_minimums": {
                "genre_lane": 3,
                "form_id": 10,
                "section_sequence": 20,
                "recurrence": 50,
                "entry": 50,
                "groove_signature": 50,
                "contrast_peak": 50,
                "transition_interlude": 50,
                "ending": 50,
                "hook_return": 5,
            },
            "selection_minimums": {
                "genre_lane": 3,
                "form_id": 10,
                "section_sequence": 10,
                "recurrence": 10,
                "entry": 10,
                "groove_signature": 10,
                "contrast_peak": 10,
                "transition_interlude": 10,
                "ending": 10,
                "hook_return": 3,
            },
            "minimum_candidate_distance": 3,
            "minimum_selection_distance": 3,
        },
    }


def build_plan(candidates: list[dict[str, object]]) -> dict[str, object]:
    selections = []
    levels = hook_levels()
    for slot, (reference, hook_level) in enumerate(
        zip(REFERENCES, levels, strict=True), start=1
    ):
        candidate = candidates[(slot - 1) * 5]
        hook_level = effective_hook_level(slot, hook_level)
        selections.append(
            {
                "track": slot,
                "slot_id": f"S{slot:02d}",
                "candidate_id": candidate["candidate_id"],
                "reference_bindings": reference_bindings_for_slot(slot),
                "locked_fingerprint": projection(candidate),
                "open_axes": ["bar allocation", "new chord progression", "instrument roles", "lyric narrative", "hook prominence"],
                "state": "finalized" if slot in {1, 2, 3, 4, 5, 6, 7, 8, 9} else "active",
                "main_prompt_form_flow": low_dynamic_flow(reference, hook_level),
            }
        )

    return {
        "catalog_revision": "rainy-night-kpop-ballad-web-v3",
        "candidate_pool": {"minimum_count": 50, "candidates": candidates},
        "selection_contract": {
            "track_count": 10,
            "envelope_allocations": [
                {"envelope_id": f"V{slot:02d}", "track_count": 1}
                for slot in range(1, 11)
            ],
        },
        "selections": selections,
    }


def build_tracks(plan: dict[str, object]) -> list[dict[str, object]]:
    tracks = []
    levels = hook_levels()
    for slot, (reference, selection, hook_level) in enumerate(
        zip(REFERENCES, plan["selections"], levels, strict=True), start=1
    ):
        hook_level = effective_hook_level(slot, hook_level)
        sections = [
            {
                "tag": tag,
                "bars": bars,
                "vocal": tag not in INSTRUMENTAL_TAGS or (slot == 4 and tag == "Coda"),
            }
            for tag, bars in zip(reference["sequence"], reference["bars"], strict=True)
        ]
        planned = round(sum(reference["bars"]) * 4 * 60 / reference["bpm"], 1)
        shared_flow = low_dynamic_flow(reference, hook_level)
        shared_mix = (
            reference["mix"]
            if slot in {1, 2, 3, 4, 5, 6, 7, 8, 9}
            else f"{reference['mix']}; narrow dynamics, soft transients, steady drums"
        )
        prompt_values = (
            TRACK_STYLES[slot - 1],
            reference["feel"],
            f"{reference['bpm']} BPM, 4/4; {GROOVE_SIGNATURES[slot - 1]}",
            "Japanese modern female jazz alto A3-C5, mostly A3-B4; clear English, stable tone, clean joins, C5 ceiling, low phrases" if slot == 3 else "Japanese modern female jazz alto A3-D5, mostly A3-C#5; clear English, stable tone, compact low phrases, clean joins, silent gaps" if slot == 4 else "Japanese modern female jazz alto A3-D5; clear English, stable tone, clean joins, mostly below C#5, low phrases, same-register modulation" if slot == 5 else "Japanese modern female jazz alto A3-D5; clear English, mostly A3-C5; stable tone, clean joins, syllabic low melody, D5 ceiling" if slot in {6, 7} else "Japanese modern female jazz alto A3-C5, mostly below Bb4; clear English, stable tone, clean joins, low syllabic melody" if slot == 8 else "Japanese modern female jazz alto A3-C5, mostly below Bb4; clear English, stable tone, clean joins, syllabic" if slot == 9 else VOCAL_EN if slot in {1, 2} else VOCAL_KO,
            TRACK_INSTRUMENTATIONS[slot - 1],
            reference["harmony"],
            shared_flow,
            shared_mix,
        )
        prompt_fields = dict(zip(MAIN_FIELDS, prompt_values, strict=True))
        tracks.append(
            {
                "track_id": slot,
                "slot_id": selection["slot_id"],
                "candidate_id": selection["candidate_id"],
                "locked_fingerprint": selection["locked_fingerprint"],
                "spec": {
                    "title": reference["title"],
                    "language": "en" if slot in {1, 2, 3, 4, 5, 6, 7, 8, 9} else "ko",
                    "target_duration_seconds": planned,
                    "bpm": reference["bpm"],
                    "metrical_pulses_per_bar": 4,
                    "sections": sections,
                    "prompt_fields": prompt_fields,
                    "exclusion_prompt": TRACK_ONE_EXCLUSION if slot == 1 else TRACK_THREE_EXCLUSION if slot == 3 else TRACK_FOUR_EXCLUSION if slot == 4 else TRACK_FIVE_EXCLUSION if slot == 5 else TRACK_SIX_EXCLUSION if slot == 6 else TRACK_SEVEN_EXCLUSION if slot == 7 else TRACK_EIGHT_EXCLUSION if slot == 8 else TRACK_NINE_EXCLUSION if slot == 9 else EXCLUSION,
                },
            }
        )
    return tracks


def compile_track(track: dict[str, object], lyrics: str) -> str:
    spec = track["spec"]
    basic = " ".join(
        f"{field}: {spec['prompt_fields'][field]}" for field in MAIN_FIELDS
    )
    return (
        "**기본프롬프트**\n"
        "```text\n"
        f"{basic}\n"
        "```\n\n"
        "**절대불가프롬프트**\n"
        "```text\n"
        f"{spec['exclusion_prompt']}\n"
        "```\n\n"
        f"### {spec['title']}\n\n"
        "**가사**\n"
        "```text\n"
        f"{lyrics}\n"
        "```\n"
    )


def build_history(tracks: list[dict[str, object]]) -> tuple[str, str]:
    rows = []
    for reference, track in zip(REFERENCES, tracks, strict=True):
        spec = track["spec"]
        sequence = "–".join(section["tag"] for section in spec["sections"])
        status = "PLAN PASS after opening/groove migration" if track["track_id"] in {1, 2, 3, 4, 5, 6, 7, 8, 9} else "planned"
        rows.append(
            f"| {track['track_id']} | {spec['title']} | {reference['scene']} | "
            f"{spec['bpm']} BPM | {sequence}, {spec['target_duration_seconds']}초 | "
            f"{reference['differentiator']} | {status} |"
        )
    detail = """# Rainy Night Drive K-pop Ballad

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
""" + "\n".join(rows) + """

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
"""

    index = """# Rainy Night Drive K-pop Ballad

- Date: 2026-07-17
- State: PRODUCE (Tracks 1-9 PLAN PASS after global opening/groove migration; Track 10 active)
- Mode: fast
- Catalog: `structure-catalog.json`
- Plan: `structure-plan.json`
- PlaylistSpec: `playlist-spec.json`
- Track 1: `exports/track-01.md`
- Track 1 review: `reviews/track-01.json`
- Track 2: `exports/track-02.md`
- Track 2 review: `reviews/track-02.json`
- Track 3: `exports/track-03.md`
- Track 3 review: `reviews/track-03.json`
- Track 4: `exports/track-04.md`
- Track 4 review: `reviews/track-04.json`
- Track 5: `exports/track-05.md`
- Track 5 review: `reviews/track-05.json`
- Track 6: `exports/track-06.md`
- Track 6 review: `reviews/track-06.json`
- Track 7: `exports/track-07.md`
- Track 7 review: `reviews/track-07.json`
- Track 8: `exports/track-08.md`
- Track 8 review: `reviews/track-08.json`
- Track 9: `exports/track-09.md`
- Track 9 review: `reviews/track-09.json`
- Detail: `history/2026-07-17__rainy-night-drive-kpop-ballad.md`
- Evidence boundary: web pages inspected; no audio renders supplied
"""
    return detail, index


def main() -> None:
    candidates, envelopes = build_candidates()
    catalog = build_catalog(candidates, envelopes)
    plan = build_plan(candidates)
    tracks = build_tracks(plan)
    playlist = {
        "schema_version": "1.0",
        "catalog_revision": catalog["catalog_revision"],
        "playlist_contract": {
            "use_case": "비 오는 밤 드라이브의 외로움을 조용한 동행과 새벽의 해소로 이동",
            "common_sound": "K-pop 발라드 반주, 좁은 편곡 다이내믹, support-only 퍼커션, A3-D5 저음 중심의 일본 모던 여성 재즈 보컬 음색·프레이징",
            "variation_pool": "곡마다 실존곡 3개를 structure·harmony·emotional_arc 역할로 웹 조사해 고수준 특성만 증류; hook seed rainy-night-drive-hook-v1 균형 셔플; 각 곡의 3축 opening·groove signature는 다른 곡과 최소 2축이 다르고 실제 프롬프트에 결합됨",
            "drift_boundaries": "All tracks: A3-D5, mostly A3-C#5, no high-note climax or drum crescendo. Percussion remains support-only unless explicitly confirmed. Tracks 1-9 English; Track 10 requires language confirmation before output. No jazz accompaniment, swing, walking bass, jazz comping, brushes, horns, scat, or rap verses",
        },
        "structure_plan": plan,
        "tracks": tracks,
    }

    previous_track = ROOT / "exports" / "track-01.md"
    archive_track = ROOT / "history" / "track-01-v1-ko.md"
    if previous_track.exists() and not archive_track.exists():
        archive_track.write_text(previous_track.read_text(encoding="utf-8"), encoding="utf-8")

    previous_track_two = ROOT / "exports" / "track-02.md"
    archive_track_two = ROOT / "history" / "track-02-v1-rejected.md"
    if previous_track_two.exists() and not archive_track_two.exists():
        archive_track_two.write_text(
            previous_track_two.read_text(encoding="utf-8"), encoding="utf-8"
        )

    previous_track_one_english = ROOT / "exports" / "track-01.md"
    archive_track_one_english = ROOT / "history" / "track-01-v2-rejected.md"
    if previous_track_one_english.exists() and not archive_track_one_english.exists():
        archive_track_one_english.write_text(
            previous_track_one_english.read_text(encoding="utf-8"), encoding="utf-8"
        )

    previous_track_three = ROOT / "exports" / "track-03.md"
    archive_track_three = ROOT / "history" / "track-03-v1-dense.md"
    if previous_track_three.exists() and not archive_track_three.exists():
        archive_track_three.write_text(
            previous_track_three.read_text(encoding="utf-8"), encoding="utf-8"
        )

    archive_track_three_spacious = ROOT / "history" / "track-03-v2-spacious-92bpm.md"
    if previous_track_three.exists() and not archive_track_three_spacious.exists():
        archive_track_three_spacious.write_text(
            previous_track_three.read_text(encoding="utf-8"), encoding="utf-8"
        )

    write_json(ROOT / "structure-catalog.json", catalog)
    write_json(ROOT / "structure-plan.json", plan)
    write_json(ROOT / "playlist-spec.json", playlist)
    (ROOT / "exports" / "track-01.md").write_text(
        compile_track(tracks[0], TRACK_ONE_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-02.md").write_text(
        compile_track(tracks[1], TRACK_TWO_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-03.md").write_text(
        compile_track(tracks[2], TRACK_THREE_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-04.md").write_text(
        compile_track(tracks[3], TRACK_FOUR_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-05.md").write_text(
        compile_track(tracks[4], TRACK_FIVE_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-06.md").write_text(
        compile_track(tracks[5], TRACK_SIX_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-07.md").write_text(
        compile_track(tracks[6], TRACK_SEVEN_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-08.md").write_text(
        compile_track(tracks[7], TRACK_EIGHT_LYRICS), encoding="utf-8"
    )
    (ROOT / "exports" / "track-09.md").write_text(
        compile_track(tracks[8], TRACK_NINE_LYRICS), encoding="utf-8"
    )
    detail, index = build_history(tracks)
    (ROOT / "history" / "2026-07-17__rainy-night-drive-kpop-ballad.md").write_text(
        detail, encoding="utf-8"
    )
    (ROOT / "PROJECT_HISTORY.md").write_text(index, encoding="utf-8")


if __name__ == "__main__":
    main()
