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
VOCAL_KO = (
    "Japanese modern female jazz alto A3-D5, mostly A3-C#5; smoky-clear natural Korean, "
    "small intervals, D5 ceiling, restrained vibrato"
)
VOCAL_EN = (
    "Japanese modern female jazz alto A3-D5, centered A3-C#5; smoky-clear English, "
    "small intervals, restrained vibrato"
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
        "mix": "Close lead, narrow dynamics, long dark reverb, air, soft transients, stable lows",
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
        "mix": "Near-field vocal, narrow dynamics, gentle chorus bloom, tape haze, soft transients, steady drums",
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
        "mix": "Close low lead, dry phrase gaps, intermittent ambience, short dark tails, centered lows, narrow dynamics, soft transients",
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
        "bpm": 86,
        "title": "돌아가지 않는 출구",
        "scene": "같은 길을 맴돌던 마음이 끝내 이별을 받아들인다",
        "differentiator": "두 번째 후렴 뒤 코다에서만 결론을 말한다",
        "feel": "Circling an exit in steady rain; resistance slowly becomes acceptance",
        "instrumentation": "Acoustic piano, fingered bass, muted electric guitar, compact pop drums, restrained cello line",
        "harmony": "A; Verse A-E/G#-F#m-D; Pre D-E-F#m-C#7; Chorus A-D-E-A; coda D-E-C#m-F#m-Bm-E-A",
        "flow": "Short entry; narrative verse and pre-chorus pairs; four-bar instrumental breath; second chorus opens directly into the concluding coda",
        "mix": "Natural lead detail, centered acoustic core, firm kick, restrained stereo lift only in the coda",
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
        "title": "첫 비가 닿는 곳",
        "scene": "차가운 빗속에서 오래 잊은 온기를 다시 발견한다",
        "differentiator": "마지막 후렴의 반음 상승 대신 새로운 전조 축",
        "feel": "Cold rain turning warm; a restrained promise gains harmonic warmth without a loudness peak",
        "instrumentation": "Grand piano, low tom pulse, electric bass, pop strings, clean electric-guitar sustain",
        "harmony": "C#m; Verse F#m-B-E-A-G#7-C#m; Chorus A-B-G#m-C#m-F#m-G#7; bridge A-B-C#sus; final key D#m",
        "flow": "Piano statement; direct first chorus; instrumental breath; second cycle deepens; bridge pivots harmonically into a same-register final chorus",
        "mix": "Intimate opening, restrained orchestral color, soft pop drums, short dark reverb",
        "scope": "Dramatic K-ballad reference; direct chorus and late modulation; selected for one high-energy crest without jazz arranging",
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
        "bpm": 90,
        "title": "늦은 차선의 고백",
        "scene": "뒤늦은 사과가 비어 있는 차선 위에서 비로소 선명해진다",
        "differentiator": "브리지 뒤 프리코러스 재등장으로 마지막 고백을 지연",
        "feel": "A late apology on an empty lane; tension is held until the final confession",
        "instrumentation": "Piano ostinato, low strings, steady pop bass, kick-snare ballad kit, single clean guitar counterline",
        "harmony": "Bb; Verse Bb-F/A-Gm-Eb; Pre Cm-D7-Gm-F; Chorus Eb-F-Dm-Gm-Cm-F-Bb; Bridge Gb-Db-Ebm-F",
        "flow": "Compact verse cycles; each pre-chorus withholds the downbeat; bridge darkens; one more pre-chorus delays the final chorus and short close",
        "mix": "Focused vocal, soft steady drums, dark verses, final string color under the same ceiling, clear low strings",
        "scope": "OST build reference; repeated pre-chorus and delayed final arrival; selected for controlled dramatic pacing",
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
        "title": "잠들지 않는 유리창",
        "scene": "도시에 남은 불빛을 하나씩 놓아주며 밤을 달랜다",
        "differentiator": "마지막 코다에서 후렴의 긴장을 완전히 풀어낸다",
        "feel": "A sleepless windshield gradually releases the city lights one by one",
        "instrumentation": "Soft piano, bowed synth texture, warm bass, minimal straight pulse, distant reverse-guitar breaths",
        "harmony": "Eb; Verse Eb-Fm-Gm-Am7b5-Bb7; Chorus Ab-Bb-Gm-Cm-Fm-Bb; Bridge Cm-Abm-Eb/Bb-Bbsus; coda Abm-Eb",
        "flow": "Two-bar-feel piano entry; paired verse and chorus; bridge suspends the pulse; expanded last chorus dissolves into an eight-bar coda",
        "mix": "Very close lead, dim high end, slow stereo opening, quiet low-frequency pulse, long but dark tail",
        "scope": "Lullaby form reference; delayed harmonic resolution and releasing coda; selected for the playlist's quietest interior point",
    },
    {
        "evidence_id": "E08",
        "artist": "Paul Kim",
        "track": "Every Day, Every Moment",
        "source": "https://www.kpopchords.com/2021/11/paul-kim-every-day-every-moment-chords.html",
        "lane": "central-night-ballad",
        "form_id": "promise-return-ballad",
        "sequence": ["Intro", "Verse", "Pre-Chorus", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Outro"],
        "bars": [4, 12, 8, 12, 12, 12, 8, 12, 4],
        "bpm": 94,
        "title": "모든 밤의 방향",
        "scene": "흔들리는 밤마다 같은 방향으로 가겠다는 약속을 세운다",
        "differentiator": "두 번째 절에서 프리코러스를 생략해 속도를 높인다",
        "feel": "A steady promise through wet intersections; warmer and more forward than the surrounding tracks",
        "instrumentation": "Bright piano, pulsing electric bass, clean guitar eighths, straight pop kit, compact string ensemble",
        "harmony": "Db; Verse Db-Ab/C-Bbm-Ab-Gb; Pre Ebm-Bbm-Gb-Ab; Chorus Db-F7-Bbm-Gb-Ebm-Ab; Bridge Gb-Ab-Bbm-Ab",
        "flow": "Bright four-bar entry; first verse earns a pre-chorus; second verse skips it for momentum; bridge suspends; final chorus lands cleanly",
        "mix": "Present lead, firmer kick, clear stereo guitar, controlled strings, crisp but rain-softened top end",
        "scope": "Promise-ballad reference; familiar verse-pre-chorus-chorus with accelerated second cycle; selected for forward driving motion",
    },
    {
        "evidence_id": "E09",
        "artist": "Yoon Mirae",
        "track": "Always",
        "source": "https://www.kpopchords.com/2021/01/yoon-mirae-always-chords.html",
        "lane": "central-night-ballad",
        "form_id": "chorus-first-memory-ballad",
        "sequence": ["Verse", "Chorus", "Verse", "Chorus", "Bridge", "Chorus", "Coda"],
        "bars": [16, 12, 12, 12, 8, 12, 4],
        "bpm": 88,
        "title": "네가 없는 교차로",
        "scene": "부재를 인정하면서도 함께였던 방향을 잊지 않는다",
        "differentiator": "인트로 없이 곧바로 목소리로 시작한다",
        "feel": "An empty intersection; absence is accepted while the shared direction remains",
        "instrumentation": "Voice-first opening, piano chords, round bass, restrained straight drums, low synth strings",
        "harmony": "A; Verse A-E/G#-F#m-D; Chorus A-C#m-F#m-D-Bm-E; Bridge D-E-C#m-F#m-Bm-E; final D-Dm-A",
        "flow": "Voice begins immediately; chorus arrives without a pre-section; shorter second verse; bridge narrows; final chorus leaves a four-bar coda",
        "mix": "Up-front voice from bar one, small room, stable center, chorus width from pads, gentle road-noise texture",
        "scope": "Direct vocal-entry reference; simple verse-chorus returns and late minor-subdominant shade; selected for immediacy",
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
        "instrumentation": "Piano and synth-string intro, sustained clean guitar, electric bass, soft straight pop drums, low cello support",
        "harmony": "F#; Verse F#-A#m-D#m-B; Hook B-C#-A#m-D#m; Bridge G#m-C#-F#-D#m-B-C#; final F#-C#/E#-D#m-B-Bm-F#",
        "flow": "Short cinematic entry; two verse-hook cycles; bridge turns darker; the only full chorus arrives at the end and resolves into four quiet bars",
        "mix": "Dark verses, diffuse final color under the same ceiling, soft drum transients, warm low mids, intimate vocal",
        "scope": "Hook-led OST reference; repeated compact hook before a final full chorus; selected as the playlist's dawn-facing resolution",
    },
]


BASE_BEHAVIORS = [
    {
        "recurrence": "two full chorus returns followed by a lyrically varied final return",
        "entry": "four bars of felt piano fragments and a deep ambient bed before the voice",
        "contrast_peak": "the bridge changes spectral color while the voice stays below D5 and the final return keeps the same narrow loudness ceiling",
        "transition_interlude": "each pre-chorus adds harmonic color while holding drum density, loudness, and the low vocal register steady",
        "ending": "four ambient instrumental bars dissolve the piano fragments into rain",
        "hook_return": "Varied return",
    },
    {
        "recurrence": "two compact chorus returns carry the same central confession",
        "entry": "quiet guitar arpeggio opens before a long first verse",
        "contrast_peak": "the second chorus is the emotional ceiling rather than a large climax",
        "transition_interlude": "verse endings thin before each direct chorus arrival",
        "ending": "an eight-bar instrumental coda releases the suspended light",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "two choruses lead to a separate late refrain",
        "entry": "soft synth pulse and piano establish motion before the voice",
        "contrast_peak": "the standalone refrain becomes the peak after a drumless bridge",
        "transition_interlude": "pre-choruses tighten the pulse and lift the inner line",
        "ending": "a short pulse-and-piano outro closes the reflected image",
        "hook_return": "Final-only callback",
    },
    {
        "recurrence": "two chorus statements defer the final conclusion to the coda",
        "entry": "piano and muted guitar present the narrative tone",
        "contrast_peak": "the second chorus opens into the coda instead of another peak",
        "transition_interlude": "a four-bar instrumental break separates the two narrative halves",
        "ending": "the coda states the acceptance and resolves the deceptive motion",
        "hook_return": "Varied return",
    },
    {
        "recurrence": "two restrained choruses prepare one transposed final chorus",
        "entry": "grand piano states the minor tonal center",
        "contrast_peak": "the bridge changes harmonic color before a same-register final chorus under the same loudness ceiling",
        "transition_interlude": "a short instrumental break resets the dynamic floor",
        "ending": "four bars sustain the new key after the final lyric",
        "hook_return": "Final-only callback",
    },
    {
        "recurrence": "three chorus arrivals are each delayed by a pre-chorus",
        "entry": "piano ostinato and low strings establish the apology",
        "contrast_peak": "the bridge darkens before a third pre-chorus withholds the final downbeat",
        "transition_interlude": "pre-choruses use dominant tension as the recurring hinge",
        "ending": "a short firm close follows the final confession",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "two chorus returns expand into one longer final chorus",
        "entry": "soft piano and bowed texture enter at the lowest energy",
        "contrast_peak": "the bridge suspends the pulse rather than increasing loudness",
        "transition_interlude": "chromatic bass motion connects each verse to its chorus",
        "ending": "the coda resolves the open dominant and lets the city lights fade",
        "hook_return": "Varied return",
    },
    {
        "recurrence": "the second cycle skips its pre-chorus before the final return",
        "entry": "bright piano begins with a steady driving pulse",
        "contrast_peak": "the bridge suspends harmony before a clean final chorus landing",
        "transition_interlude": "the missing second pre-chorus creates forward acceleration",
        "ending": "four bars hold the tonic-add-six color after the promise",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "three direct chorus returns arrive without pre-choruses",
        "entry": "the lead voice begins immediately with no instrumental intro",
        "contrast_peak": "the bridge narrows before the final chorus adds the minor-subdominant shade",
        "transition_interlude": "short verse endings turn directly into the chorus downbeat",
        "ending": "a four-bar coda keeps the final direction unresolved but calm",
        "hook_return": "Repeated hook",
    },
    {
        "recurrence": "two compact hooks prepare a single full final chorus",
        "entry": "piano and synth strings frame the last rainy miles",
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
This time I breathe before I read your message
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
                "evidence_ids": [reference["evidence_id"]],
                "section_sequence": sequence,
                "recurrence": base_behavior["recurrence"] if variant == 0 else f"slot-{slot:02d}-variant-{variant}-return-logic",
                "entry": base_behavior["entry"] if variant == 0 else f"slot-{slot:02d}-variant-{variant}-entry-gesture",
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
                "evidence_ids": [reference["evidence_id"]],
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
                    ref["evidence_id"] for ref in REFERENCES if ref["lane"] == lane_id
                ],
            }
        )

    return {
        "catalog_revision": "rainy-night-kpop-ballad-web-v1",
        "genre_coordinate": "K-pop ballad for rainy night driving; Japanese modern female jazz vocal character; non-jazz accompaniment; narrow arrangement dynamics and low vocal register",
        "evidence": [
            {
                "id": ref["evidence_id"],
                "source": ref["source"],
                "scope": f"{ref['artist']} — {ref['track']}; {ref['scope']}",
            }
            for ref in REFERENCES
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
        selections.append(
            {
                "track": slot,
                "slot_id": f"S{slot:02d}",
                "candidate_id": candidate["candidate_id"],
                "reference_evidence_id": reference["evidence_id"],
                "locked_fingerprint": projection(candidate),
                "open_axes": ["bar allocation", "new chord progression", "instrument roles", "lyric narrative", "hook prominence"],
                "state": "finalized" if slot in {1, 2} else "active" if slot == 3 else "consumed-by-design",
                "main_prompt_form_flow": low_dynamic_flow(reference, hook_level),
            }
        )

    return {
        "catalog_revision": "rainy-night-kpop-ballad-web-v1",
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
        sections = [
            {"tag": tag, "bars": bars, "vocal": tag not in INSTRUMENTAL_TAGS}
            for tag, bars in zip(reference["sequence"], reference["bars"], strict=True)
        ]
        planned = round(sum(reference["bars"]) * 4 * 60 / reference["bpm"], 1)
        shared_flow = low_dynamic_flow(reference, hook_level)
        shared_mix = (
            reference["mix"]
            if slot in {1, 2, 3}
            else f"{reference['mix']}; narrow dynamics, soft transients, steady drums"
        )
        prompt_values = (
            "Nocturnal K-pop ambient ballad" if slot == 1 else "Nocturnal K-pop ballad" if slot == 2 else "Rainy nocturnal K-pop ballad" if slot == 3 else "Korean nocturnal K-pop ballad; cinematic pop",
            reference["feel"],
            f"{reference['bpm']} BPM, 4/4; slow half-time ballad; full-bar drum gaps" if slot == 3 else f"{reference['bpm']} BPM, 4/4; restrained straight ballad pulse",
            "Japanese modern female jazz alto A3-C5, mostly A3-B4; smoky-clear English, C5 ceiling, low phrases, audible rests" if slot == 3 else VOCAL_EN if slot in {1, 2} else VOCAL_KO,
            reference["instrumentation"],
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
                    "language": "en" if slot in {1, 2, 3} else "ko",
                    "target_duration_seconds": planned,
                    "bpm": reference["bpm"],
                    "metrical_pulses_per_bar": 4,
                    "sections": sections,
                    "prompt_fields": prompt_fields,
                    "exclusion_prompt": TRACK_ONE_EXCLUSION if slot == 1 else TRACK_THREE_EXCLUSION if slot == 3 else EXCLUSION,
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
        status = "draft-validated" if track["track_id"] in {1, 2, 3} else "planned"
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
| Track 1-3은 영어, Track 4-10은 임시 한국어 값 | Track 2-3 영어는 사용자 확정; 나머지는 출력 전 언어 확인 필요 | high | 각 트랙 생성 직전 명시 언어로 교체 |
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
"""

    index = """# Rainy Night Drive K-pop Ballad

- Date: 2026-07-17
- State: PRODUCE (Tracks 1-3 draft-validated)
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
            "common_sound": "K-pop 발라드 반주, 좁은 편곡 다이내믹, A3-D5 저음 중심의 일본 모던 여성 재즈 보컬 음색·프레이징",
            "variation_pool": "10개 웹 레퍼런스별 구조·화성 변환; hook seed rainy-night-drive-hook-v1로 3 subtle, 4 moderate, 3 strong 균형 셔플",
            "drift_boundaries": "All tracks: A3-D5, mostly A3-C#5, no high-note climax or drum crescendo. Tracks 1-3 English; Tracks 4-10 require language confirmation before output. No jazz accompaniment, swing, walking bass, jazz comping, brushes, horns, scat, or rap verses",
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
    detail, index = build_history(tracks)
    (ROOT / "history" / "2026-07-17__rainy-night-drive-kpop-ballad.md").write_text(
        detail, encoding="utf-8"
    )
    (ROOT / "PROJECT_HISTORY.md").write_text(index, encoding="utf-8")


if __name__ == "__main__":
    main()
