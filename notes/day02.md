\# Day 2 — 2026-04-22 (수) / 실제 Day 3 (외부 blocker로 순연)



\## 오늘 한 것

\- Day 1 retrieval v2 (blank-page recall): \[Block 1\~6 중 tier 3 몇 개 / blank 몇 개]

\- `requests` 라이브러리 기초

\- HTTP method 5종 + GET/POST 의 가시성 경계

\- `requests` 보안 4 hook 실습 (User-Agent, Authorization, timeout, verify)



\## 핵심 개념 (본인 말)



\### HTTP Method 의 보안 의미

\- GET vs POST: \[URL 로 갈 것 vs Body 로 갈 것의 구분이 가시성 경계인 이유 한 줄]

GET: 모두가 볼 수 있음, POST: 서버만 볼 수 있음.

\### requests 보안 4 Hook

1\. User-Agent: \[왜 바꿔야 하는지]

2\. Authorization: \[왜 URL 이 아닌 header 로]

3\. timeout: \[빠뜨리면 어떻게 되는지]

4\. verify: \[끄면 어떤 공격에 무방비인지]



\## 사고·실수·관찰



\### verify=False 실수 실행

\- 상황: \[무슨 일 있었는지 한 줄]

\- 관찰: \[무반응이 의미하는 것 한 줄]

\- 교훈: \[defensive coding 어떻게 할 건지]



\## Day 1 연결

\- Day 1 의 secret boundary · defense in depth 가 오늘 어떻게 재등장했나:

&#x20; - \[2-2 Authorization 실습에서 가짜 bearer 가 파일·history 에 남음 → .env 분리 원칙 재확인]

&#x20; - \[4 hook 이 각각 어느 경계 방어에 대응하는지 1-2줄]



\## 내일 (Day 4, 2026-04-23) 앵커 복구 계획

\- 06:00 기상 anchor 복구 실험

\- Cue: \[본인이 정할 것 — 알람? 커피 세팅?]

\- Reward: \[출석체크 완료 후 즉시 얻을 보상 1개]



\## Tier 자가진단

\- Day 1 개념: \[tier X]

\- `requests` 기초: \[tier X]

\- `requests` 4 hook: \[tier X]

