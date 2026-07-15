---
name: create-context-playlist-prompts
description: Design cohesive 10-track, reference-led playlists and generate one compact Suno style prompt plus synchronized lyrics at a time. Use for situation-specific playlists, prompt-form reference parsing, related-song discovery, reference-song style translation, vocalist consistency, adjacent-genre variation, user-supplied audio target matching, failed-render diagnosis, prompt revision, playlist reset, or project history tracking.
---

# Create Context Playlist Prompts

레퍼런스의 상위 음악 정체성은 유지하되 멜로디·훅·정확한 코드 진행·가사·대표 리프는 새로 설계하라. 전체 10곡 설계를 먼저 승인받고, 실제 Suno Prompt와 Lyrics는 한 곡씩 제공하라.

## 필요한 참조를 읽어라

- 새 플레이리스트·전체 설계: [references/design-rules.md](references/design-rules.md), [references/output-contract.md](references/output-contract.md)
- `Hard constraints`·`Style` 등 프롬프트 형태의 레퍼런스: [references/prompt-reference-protocol.md](references/prompt-reference-protocol.md)
- 오디오 파일·생성 결과물·“이런 느낌” 비교: [references/audio-reference-protocol.md](references/audio-reference-protocol.md)
- 수정·재생성·초기화·공통 요구 전파: [references/revision-protocol.md](references/revision-protocol.md)

## 프롬프트형 레퍼런스를 먼저 시드로 바꿔라

사용자가 `Hard constraints`, `Style`, 템포, 보컬, 악기, 금지 조건이 결합된 프롬프트를 레퍼런스로 주면 완성 Prompt나 승인된 제약으로 바로 사용하지 마라. 명시값과 추론값을 구분한 시드 설계로 먼저 분해하고, 실제 관련 곡 후보를 조사·추천한 다음 원하는 분위기를 한 번에 1~2개씩 인터뷰하라. 추천곡은 사용자가 선택하기 전까지 Primary·Supporting reference로 확정하지 마라. 이 단계에서는 10곡 설계나 단일 곡 Prompt·Lyrics를 출력하지 마라.

레퍼런스 후보와 최종 선택곡은 가사 언어 기준 `영어 팝송`, `일본어곡`, `한국어곡`에서만 고르라. 같은 곡을 여러 분석 축·레퍼런스 역할·플레이리스트 트랙에 중복 사용할 수 있다. 단, 두 트랙의 곡별 화성 레퍼런스 목록은 50% 이상 겹치면 안 된다. 세부 분류와 계산법은 [references/prompt-reference-protocol.md](references/prompt-reference-protocol.md)를 따르라.

## 1. 작업 상태와 근거의 역할을 구분하라

다음을 혼합하지 말고 명시적으로 기록하라.

- `Primary reference`: 스타일과 음악 문법의 중심축
- `Supporting references`: 화성·편곡 판단을 보조하는 곡
- `Target render`: 사용자가 “이 결과처럼”이라고 승인한 출력 음원
- `Rejected render`: 실패 원인만 추출하고 모방하지 않을 결과물
- `Context`: 날씨·시간·장소·행동·감정 등 사용 상황
- `Approved constraints`: 사용자가 확정한 보컬·언어·금지·길이 규칙

최신 명시적 사용자 지시를 최우선으로 하라. Primary reference는 기본 스타일 축으로 유지하되, 사용자가 Target render를 제시하면 논쟁 중인 청감 특성에는 그 음원을 우선 적용하라. 확인할 수 없는 음악적 사실은 추론으로 표시하라.

## 2. 이미 답한 내용은 묻지 마라

국가·지역, 연대, 시장·문화권, 대장르, 하위 장르, 템포·그루브, 언어, 프로덕션 문법을 계층적으로 정리하라. 결과를 크게 바꾸는 빈칸만 한 번에 1~2개 질문하라. 사용자의 자유 서술도 확정 입력으로 인정하라.

다음은 반드시 범위를 분리하라.

- `Energy`: 플레이리스트 안의 상대 추진력 3·4·5
- `Arrangement dynamics`: 섹션별 음량·밀도·드럼 강도·레이어 변화
- `Vocal emotional depth`: 보컬이 전달하는 감정의 깊이
- `Vocal lowest note`: 리드 보컬 멜로디의 최저음

사용자가 다이내믹을 “감정 깊이와 보컬 최저음”으로 정의하면 그 정의만 적용하라. 이를 편곡 평탄화, 후렴 상승 금지, 필인 금지, 레이어 증가 금지로 확대하지 마라. 편곡 다이내믹까지 최소화하라는 명시가 있을 때만 별도로 제한하라.

## 3. 레퍼런스 DNA와 보컬을 승인받아라

레퍼런스에서 장르 문법, 시대감, 템포 범위, 그루브, 보컬 프레이징, 악기 역할, 프로덕션 밀도, 공간감을 추출하라. 보존할 상위 특성과 새로 만들 하위 요소를 나눠 제시하라. 실존 아티스트명과 곡명은 분석 근거에만 쓰고 생성용 프롬프트에는 넣지 마라.

리드 보컬은 1~3명의 가상 인물 중 사용자가 선택하게 하라. 사용자가 한 명을 지정하면 전곡에서 정확히 그 한 명만 유지하고 추가 ID나 대체 리드를 만들지 마라. 각 곡의 리드는 단독이며 백그라운드 코러스·하모니는 허용 범위대로 사용하라. 보컬의 음역·최저음, 음색, 성량, 발음, 프레이징, 감정 깊이, 금지 특성을 승인받아라.

## 4. 전체 설계와 실제 출력을 분리하라

정확히 10곡의 전체 설계표를 한 번에 작성하라. 같은 세계관·중심 장르·인접 장르·템포 권역을 유지하면서 곡마다 악기 역할, 전주, 드럼 연주, 화성 장치와 서사를 바꿔라. 훅은 필수가 아니며 [references/design-rules.md](references/design-rules.md)의 무작위 전략 배정 규칙을 적용하라. 각 곡은 따로 꺼내도 완결되어야 한다. 전체 설계 승인 전에는 실제 프롬프트나 가사를 만들지 마라.

승인 후에는 사용자가 선택한 한 곡만 다음 두 블록으로 출력하라.

1. `Suno Prompt`: 영어 중심, 배제 조건 통합, 공백·문장부호 포함 800자 이하
2. `Lyrics`: 확정된 한 언어, 장르 표준 길이 ±20%에 맞는 완성 가사

출력 형식과 검사 게이트는 [references/output-contract.md](references/output-contract.md)를 따르라.

## 5. 프롬프트를 원자적으로 컴파일하라

기존 문장을 이어 붙이지 말고 승인된 설계와 최신 요구사항에서 매번 전체 프롬프트를 새로 작성하라. 순서는 다음과 같다.

1. `Hard constraints:` 결과를 망가뜨리는 핵심 제약만 짧게 배치
2. `Style:` 국가·연대·중심/인접 장르·템포·그루브
3. 단일 리드 보컬의 정체성과 프레이징
4. 네 가지 다이내믹 축 중 확정된 값
5. 악기 역할·전주·드럼·화성·훅·믹싱
6. 필요한 낮은 우선순위 배제만 짧게 보완

긍정어와 부정어가 같은 청감을 동시에 유도하면 부정어를 늘리지 말고 원인이 되는 긍정어를 제거하거나 바꿔라. 사용자가 어떤 개념을 “아예 빼라”고 하면 긍정·부정 양쪽에서 그 개념을 모두 삭제하라. Hard constraints는 가능한 적게 유지하고, 원하는 소리를 긍정적으로 명확히 기술하라.

## 6. 수정은 진단 후 전체 재생성하라

실패 결과가 있으면 프롬프트 추측만으로 고치지 말고 설계 대비 실제 결과의 차이를 먼저 분류하라. 사용자가 이미 원인과 목표를 구체적으로 말했으면 추가 인터뷰 없이 수정하라. 모호할 때만 한 번에 1~2개의 판별 질문을 하라.

수정 시 Prompt와 Lyrics를 모두 처음부터 다시 판단하고 완전한 전체본으로 제공하라. 부분 패치, 추가 문장, diff를 제공하지 마라. 공통 요구는 남은 곡에 전파하고 곡별 요구는 해당 곡에만 적용하라.

## 7. 초기화는 완전 리셋하라

사용자가 `초기화`, `전체 초기화`, `완전 초기화`, `프로젝트 초기화`, `플레이리스트 리셋`을 명시하면 현재 곡 재생성으로 처리하지 마라. 히스토리만 보관하고 활성 상태의 Context, 모든 reference 역할, Target·Rejected render, Approved constraints, 장르·언어·보컬·발성, 공통 규칙, 10곡 설계와 승인, 곡 선택, 곡별 Prompt·Lyrics 진행 상태를 전부 비워라.

초기화 후에는 새 프로젝트의 초기 인터뷰부터 다시 시작하라. 필요한 상위 입력이 모이면 정확히 10곡의 새 전체 설계표를 제시하고 승인을 기다려라. 승인 전에는 단일 곡 Prompt나 Lyrics를 출력하지 마라.

`현재 곡을 처음부터 재설계`는 초기화가 아니라 곡별 전체 재생성이다. 두 요청을 혼동하지 마라. 세부 상태 전환은 [references/revision-protocol.md](references/revision-protocol.md)를 따르라.

## 8. 검사와 기록을 완료하라

검사에서 하나라도 실패하면 결과를 노출하지 말고 내부 재설계 후 전 항목을 다시 검사하라. 한 곡을 출력한 뒤에는 다음 곡을 자동 생성하지 말고 승인 또는 수정 요청을 기다려라.

작업공간이 있으면 `PROJECT_HISTORY.md`를 인덱스로, `history/YYYY-MM-DD__topic-slug.md`를 상세 기록으로 사용하라. 승인된 설계, 사용자 피드백, Prompt 버전, 실패 원인, 검사 결과, 상태를 누적하고 이전 버전을 덮어쓰지 마라.
