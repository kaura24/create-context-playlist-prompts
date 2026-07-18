# Rainy Night Drive K-pop Ballad

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
| 1 | Voice Beyond the Wipers | 심야 라디오가 고독을 조용한 동행으로 바꾼다 | 88 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Pre-Chorus–Chorus–Bridge–Chorus–Outro, 218.2초 | 피아노 모티프와 하행 베이스의 라디오형 빌드 | draft-validated |
| 2 | While the Light Stays Red | 보내지 못한 말이 붉은 신호 아래 편지처럼 머문다 | 78 BPM | Intro–Verse–Chorus–Verse–Chorus–Coda, 209.2초 | 기타 아르페지오와 짧은 두 번의 후렴 | draft-validated |
| 3 | Past Your Exit | 돌려줄 열쇠를 들고 옛집으로 가다가 직접 만나지 않고 우편으로 보내기로 결정한다 | 76 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Pre-Chorus–Chorus–Bridge–Refrain–Outro, 227.4초 | 신스 펄스와 마지막 독립 리프레인 | draft-validated |
| 4 | 돌아가지 않는 출구 | 같은 길을 맴돌던 마음이 끝내 이별을 받아들인다 | 86 BPM | Intro–Verse–Pre-Chorus–Chorus–Break–Verse–Pre-Chorus–Chorus–Coda, 223.3초 | 두 번째 후렴 뒤 코다에서만 결론을 말한다 | planned |
| 5 | 첫 비가 닿는 곳 | 차가운 빗속에서 오래 잊은 온기를 다시 발견한다 | 84 BPM | Intro–Verse–Chorus–Break–Verse–Chorus–Bridge–Chorus–Outro, 205.7초 | 마지막 후렴의 반음 상승 대신 새로운 전조 축 | planned |
| 6 | 늦은 차선의 고백 | 뒤늦은 사과가 비어 있는 차선 위에서 비로소 선명해진다 | 90 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Pre-Chorus–Chorus–Bridge–Pre-Chorus–Chorus–Outro, 213.3초 | 브리지 뒤 프리코러스 재등장으로 마지막 고백을 지연 | planned |
| 7 | 잠들지 않는 유리창 | 도시에 남은 불빛을 하나씩 놓아주며 밤을 달랜다 | 80 BPM | Intro–Verse–Chorus–Verse–Chorus–Bridge–Chorus–Coda, 216.0초 | 마지막 코다에서 후렴의 긴장을 완전히 풀어낸다 | planned |
| 8 | 모든 밤의 방향 | 흔들리는 밤마다 같은 방향으로 가겠다는 약속을 세운다 | 94 BPM | Intro–Verse–Pre-Chorus–Chorus–Verse–Chorus–Bridge–Chorus–Outro, 214.5초 | 두 번째 절에서 프리코러스를 생략해 속도를 높인다 | planned |
| 9 | 네가 없는 교차로 | 부재를 인정하면서도 함께였던 방향을 잊지 않는다 | 88 BPM | Verse–Chorus–Verse–Chorus–Bridge–Chorus–Coda, 207.3초 | 인트로 없이 곧바로 목소리로 시작한다 | planned |
| 10 | 비가 멎기 전까지 | 새벽이 가까워질수록 상실을 놓고 앞으로 달려간다 | 82 BPM | Intro–Verse–Hook–Verse–Hook–Bridge–Chorus–Outro, 210.7초 | 짧은 훅은 두 번만, 완전한 코러스는 마지막에만 등장 | planned |

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
