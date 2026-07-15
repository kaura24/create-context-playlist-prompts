# Create Context Playlist Prompts

Codex 전역 스킬 `create-context-playlist-prompts`의 소스 저장소입니다.

이 저장소는 스킬의 작동 규칙을 관리합니다. 실제 플레이리스트, 곡별 프롬프트, 가사, 실패 렌더 분석, 사용자 피드백 같은 작업 기록물은 각 음악 프로젝트 작업공간에 따로 남깁니다.

## Repository Structure

```text
create-context-playlist-prompts/
  README.md
  SKILL.md
  agents/
    openai.yaml
  references/
    audio-reference-protocol.md
    design-rules.md
    output-contract.md
    prompt-reference-protocol.md
    revision-protocol.md
```

- `SKILL.md`: 스킬 진입점과 핵심 운영 규칙
- `agents/openai.yaml`: 스킬 실행에 필요한 agent 힌트
- `references/`: 세부 프로토콜과 출력 계약
- `README.md`: 저장소 운영 방식과 기록물 관리 규칙

## Project Record Structure

실제 작업 기록은 스킬 저장소가 아니라 프로젝트별 작업공간에 둡니다.

```text
playlist-project/
  PROJECT_HISTORY.md
  history/
    2026-07-15__rainy-night-citypop.md
    2026-07-16__summer-drive-playlist.md
  assets/
    references/
    renders/
  exports/
```

- `PROJECT_HISTORY.md`: 프로젝트 인덱스와 현재 상태 요약
- `history/YYYY-MM-DD__topic-slug.md`: 승인 설계, 곡별 버전, 피드백, 실패 원인, 검사 결과를 누적하는 상세 기록
- `assets/references/`: 사용자가 제공한 레퍼런스 음원, 이미지, 메모 등
- `assets/renders/`: 생성 결과물, 실패 렌더, 비교 대상
- `exports/`: 최종 전달용 Prompt, Lyrics, 플레이리스트 문서

`assets/`와 `exports/`는 추천 구조입니다. 스킬의 필수 기록 계약은 `PROJECT_HISTORY.md`와 `history/YYYY-MM-DD__topic-slug.md`입니다.

## Record Rules

1. 기록은 덮어쓰지 않고 새 버전으로 누적합니다.
2. `PROJECT_HISTORY.md`에는 현재 승인 상태, 다음 작업, 주요 결정의 인덱스를 남깁니다.
3. 상세 파일에는 10곡 설계, 사용자 피드백, Prompt 버전, Lyrics 버전, 실패 원인, 검사 결과를 시간순으로 남깁니다.
4. `초기화`, `전체 초기화`, `완전 초기화`, `프로젝트 초기화`, `플레이리스트 리셋` 요청은 활성 상태만 비우고 기존 기록은 `초기화 전 보관` 상태로 남깁니다.
5. 현재 곡 재설계는 프로젝트 초기화가 아닙니다. 해당 곡의 새 버전으로 기록합니다.
6. 공통 수정은 누적 공통 요구사항에 기록하고, 현재 곡과 앞으로 만들 곡에 적용 범위를 명시합니다.
7. 곡별 수정은 해당 곡의 상세 기록에만 반영하고, 다른 곡은 사용자가 요청하지 않는 한 바꾸지 않습니다.

## Recommended History Entry Shape

```md
# 2026-07-15 — rainy-night-citypop

## Current State

- Context:
- Primary reference:
- Supporting references:
- Approved constraints:
- Vocal:
- Active track:

## Approved 10-Track Design

| # | Working title | Vocal | Language | Energy | Harmony references | Hook strategy | Status |
|---|---|---|---|---|---|---|---|

## Track Versions

### Track 1 / v1

- Request:
- Classification: new draft | track revision | common revision | reset archive
- Suno Prompt:
- Lyrics:
- Check result:
- User feedback:

### Track 1 / v2

- Change reason:
- Scope: track-only | common
- Regenerated Prompt:
- Regenerated Lyrics:
- Check result:

## Reset Archive

- Reset date:
- Preserved state:
- Reason:
```

## Git Workflow

이 저장소를 수정할 때는 스킬 동작 규칙의 변경만 커밋합니다.

```bash
git status --short --branch
git add README.md SKILL.md agents references
git commit
git push
```

커밋 메시지는 변경 이유를 첫 줄에 쓰고, 필요한 경우 `Constraint:`, `Directive:`, `Tested:`, `Not-tested:` 같은 trailer를 추가합니다.
