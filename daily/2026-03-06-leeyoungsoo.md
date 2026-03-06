# 작업일지 2026-03-06 (leeyoungsoo)

## 오늘 한 일

### D:/SDC/svgviewer (sdc_svg) — SVG 에디터 PixiJS 기반 개발
- `import svg` 브랜치 체크아웃 및 작업
- PixiJS를 이용한 SVG import 기능 구현 (Top bar에 import 버튼 추가)
- 허용 확장자 제한: `svg, jpg, jpeg, png` 이외 차단
- SVG import 시 각 객체(선, 텍스트, 도형)를 PixiJS 개체로 변환해 개별 선택·편집 가능하도록 구현
- SVG export 시 배경 black 처리
- button, triangle 등 심볼 export 누락 이슈 파악 및 수정
- 선(line) export 지원 추가
- Playwright로 SVG import/export 테스트 (두 방식 비교: pixijs-architecture.html vs 현재 앱)
- `refactor` 브랜치와 병합 — 라이브러리 교체 후 export/import 영향 없는 부분만 적용
- 프로젝트 전체를 `D:/SDC_SVG` 경로로 복사 후 `https://github.com/HAA02/SDC_SVG.git` 리포지토리와 연결

### D:/SVGEditor — ThreeJS/PixiJS 브랜치 분석
- `threeJS.PixJs` 브랜치 체크아웃 및 PixiJS 폴더 구조 분석
- PixiJS가 기존 SVG DOM 방식 대비 빠른 이유 이해 (DOM 파이프라인 생략 → WebGL 직접 렌더)
- `monitorplan.html` 기반 신규 SVG 에디터에 PixiJS 도입 브레인스토밍
- 무한 캔버스(피그마 스타일) 및 납품용 모듈화 계획 `sdc_plan.md`에 정리
- PixiJS 관련 핵심 내용 `memory.md`에 저장

### D:/pixi/importexport — PixiJS 무한 캔버스 프로토타입
- PixiJS 라이브러리로 무한 캔버스 + SVG import/export 구현 시작
- SVG 업로드, 전체 캔버스 export, 개체 선택(선·텍스트·도형) 기능 작업
- resize 및 텍스트 수정 기능 추가

### D:/weeklyReport — 주간보고 시스템 고도화
- FastAPI 서버 실행 및 원격 브랜치 pull
- 로컬 DB 이름을 서버와 일치시키도록 변경 (`weeklyReports_snapshot_20260304.db`)
- `models.py` 수정
- UI: "고도화 예정" 텍스트 박스 제거
- 제출 현황에서 TI팀 미표시 버그 수정
- 팀 색상 통일 (초록색 → 일반 팀과 동일 스타일)
- 유저 비밀번호 재설정:
  - master: `masterviewer123`
  - ict: `ict*2026^^`
  - rnd: `rnd@2026!!`
- 부서별 이용 매뉴얼 MD 작성 (ict, rnd, master 버전 / 이슈리스트 작성법 포함)

### D:/work-reports — 퇴근 커맨드 세팅
- `setup/퇴근.md` → `~/.claude/commands/퇴근.md` 복사
- README 확인 및 사용법 파악

## 주요 변경사항 (Git)

- `D:/work-reports`: LBC 사용자 작업일지 커밋 3건 (오늘 날짜)
- `D:/SDC_SVG`: SVG import/export 기능 구현 및 refactor 병합 후 push
- `D:/weeklyReport`: DB 동기화, UI 수정, 비밀번호 변경, 매뉴얼 작성

## 해결한 문제

- SVG import 후 캔버스가 텅 비는 문제 → PixiJS 파서 개선으로 해결
- TI팀이 제출 현황에 안 보이는 버그 수정
- button 심볼이 SVG export에 포함 안 되는 문제 수정
- `<use>` 요소 미지원 경고 파악 (`SvgElementConverter.ts`)
- python3 Windows Store 리다이렉트 문제 (실제 Python 경로로 우회)

## 만든 것 / 배운 것

- PixiJS SVG import: `SVGParser → PixiJS 객체 변환 → WebGL 렌더` 흐름 완성
- SVG DOM vs PixiJS 차이: DOM은 CSS 파이프라인 경유, PixiJS는 WebGL 직접 → 객체 많을수록 차이 큼
- PixiJS `<use>` 요소 미지원 → 사전 펼치기(flatten) 필요
- 부서별 매뉴얼 포맷 (ict / rnd / master 분리)
- `/퇴근` 커맨드 구조 및 collect-today.py 동작 원리

## 다음에 이어서 할 일

- `D:/SDC_SVG`: `<use>` 요소 지원 또는 import 전 flatten 처리
- `D:/SVGEditor` monitorplan.html에 PixiJS 무한 캔버스 정식 도입 계획 실행
- `D:/pixi/importexport` 프로토타입 → 실제 납품용 모듈화
- `D:/weeklyReport` 이슈리스트 기능 연동 마무리

## 메모

- `python3` 명령이 Windows Store 리다이렉트에 걸릴 경우 실제 경로 직접 사용:
  `/c/Users/IAAN/AppData/Local/Programs/Python/Python310/python.exe`
- SDC_SVG 리포는 `https://github.com/HAA02/SDC_SVG.git` 연결됨
- Ralph Loop 플러그인: 완성될 때까지 반복 실행하는 Claude Code 플러그인, `--dangerously-skip-permissions`와 함께 사용 검토 중
