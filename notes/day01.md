# Day 1 — 2026-04-18

AI 보안 공부 첫날. 계획은 "환경 셋업 3시간". 실제로는 Git/Auth/Secret hygiene 실전 크래시 코스 5시간. 명목상 overrun, 실질적으로 이득이라고 본다.

## 성과

- Python 3 + venv + pip 세팅 (Windows)
- Anthropic API 키 발급, `.env`로 분리
- `hello.py`로 Claude API 첫 호출 성공
- GitHub 계정 + public 레포 (`udefed/udefed-llmsec`) 생성
- Git 한 사이클 완주 (`init` → `add` → `commit` → `push`)
- 사고 3건 모두 복구 (아래 상세)

## 오늘 배운 개념

### 환경
- **가상환경 (venv)**: 프로젝트별 라이브러리 격리 공간. 프로젝트끼리 안 섞이게.
- **`.env`**: 비밀 값(API 키 등)을 코드와 분리 보관하는 파일.
- **`.gitignore`**: Git에게 "이 파일들은 레포에 넣지 마" 쪽지. **반드시 레포 루트**에 있어야 전체 적용.

### Git
- **커밋**: 프로젝트의 한 시점을 사진처럼 박제. 고유 ID를 가짐.
- **`git commit --amend`**: 방금 찍은 마지막 커밋을 새 커밋으로 교체. push 전에만 안전.
- **Initial commit은 parent가 없다**: `HEAD~1` 참조 불가. reset 대신 amend로 해결.

### 인증 & 비밀
- **PAT (Personal Access Token)**: 비밀번호 대체 임시 토큰. scope(권한 범위)를 직접 지정.
- **Credential Manager 캐시**: Windows가 과거 GitHub 로그인을 기억. 계정 바뀔 때 수동 정리 필요.
- **키 노출 시 첫 행동**: 항상 **재발급**. 코드 수정·이력 정리는 그 다음.

### Security mindset — first seeds
오늘 하루에 "경계(boundary)" 사례 4종 접함. 이게 LLM 보안 공부의 밑돌.

1. **인증 경계** — 인증된 주체 ≠ 리소스 소유자일 때 시스템이 거부 (403)
2. **비밀 경계** — 코드와 secret은 같은 파일에 있으면 안 됨
3. **설정 적용 범위 경계** — `.gitignore`는 놓인 위치에 따라 효력 범위가 달라짐
4. **가시성 경계** — local commit vs pushed commit vs reachable vs orphaned

Defense in depth도 실물로 체험: 내 실수(.gitignore 누락)를 GitHub Push Protection이 잡음.

## 시행착오 기록

### 사고 1: `git push` 403

```
remote: Permission to udefed/udefed-llmsec.git denied to handsmaple.
```

- 원인: Windows Credential Manager에 옛 GitHub 계정(`handsmaple`) 자격증명 잔류.
- 해결: Credential Manager에서 `git:https://github.com` 항목 제거 → `udefed` 계정으로 PAT 발급 → 재인증.

### 사고 2: `.env`가 commit에 포함됨

- 원인: `.gitignore`가 실제로는 `.gitignore.txt`로 저장됨 (Notepad 기본 동작). Git은 "무시 쪽지 없음"으로 인식 → `.env`가 staging에 포함 → commit → push 시도.
- 차단: GitHub Push Protection이 "Anthropic API Key 감지" 거부.
- 해결: API 키 즉시 재발급 → PowerShell `Set-Content`로 `.gitignore` 제대로 생성 → `git rm --cached .env` → `git commit --amend` → 재푸시 성공.

### 사고 3: `git reset --soft HEAD~1` 실패

```
fatal: ambiguous argument 'HEAD~1': unknown revision or path not in the working tree.
```

- 원인: 첫 커밋(initial commit)은 parent가 없음 → `HEAD~1` 참조 대상 없음.
- 해결: reset 대신 `--amend`로 커밋 자체를 교체. Git의 DAG 구조 첫 감각 획득.

## Rules of thumb (오늘 건진 것들)

1. API 키는 `.env`에, `.env`는 `.gitignore`에
2. `.gitignore`는 레포 루트(최상단)에 — 하위 폴더에 넣으면 scope 좁아짐
3. 키가 Git에 한 번 들어간 순간 → 무조건 재발급부터
4. Windows에서 dotfile 만들 땐 PowerShell `Set-Content` 사용. Notepad는 자동으로 `.txt` 붙임
5. Push 전에 `git status` + `git log --stat`로 반드시 확인
6. `git commit --amend`는 push 전에만 안전
7. GitHub 인증은 PAT. 비밀번호 auth는 2021년부터 막힘
8. `venv/`, `.env`, `__pycache__/` — `.gitignore` 단골 세 가지

## 메타 관찰

명목상 오늘은 "환경 셋업"이었다. 실질은 개발 보안 위생 크래시 코스였다.
시간 더 썼지만 Phase 2에서 공부할 Prompt Injection·Jailbreak의 본질이 **경계 인식**이라는 점을 생각하면, 오늘의 삽질이 가장 실전적인 기초 훈련이었다고 본다.

처음부터 매끈하게 끝났으면 놓쳤을 감각을 사고 3건으로 얻었음.

## 다음

- **Day 2**: `requests` 라이브러리 실험, API 호출 확장
- **Day 3-4**: LLM 8개 핵심 개념 (token, context window, system prompt, temperature, tools, embedding, RAG 기본, agent loop)
- **Day 7**: Feynman 3단계로 Week 1 전체 재구성 + 회고

---

*공부 파트너: Claude (Anthropic). 이 로그는 build in public의 원재료.*
