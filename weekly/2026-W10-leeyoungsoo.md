# 주간 요약 2026-W10 (leeyoungsoo)

> 기간: 2026-03-02 ~ 2026-03-06

## 이번 주 핵심 작업

### SVG 에디터 PixiJS 전환 (D:/SDC/svgviewer, D:/SVGEditor, D:/pixi/importexport)
- PixiJS 기반 SVG import/export 기능 구현 완료
- SVG 파일의 각 객체(선, 텍스트, 도형, 버튼 심볼 등)를 PixiJS 개체로 변환 → 개별 선택·편집 가능
- SVG export 시 black 배경 처리, 모든 심볼 타입 포함
- `refactor` 브랜치와 병합, 프로젝트를 `HAA02/SDC_SVG` 리포로 이전
- PixiJS 무한 캔버스 프로토타입 제작 (`D:/pixi/importexport`)
- ThreeJS 브랜치의 PixiJS 폴더 분석 → SVG DOM 대비 WebGL 직접 렌더 방식의 성능 우위 파악

### 주간보고 시스템 고도화 (D:/weeklyReport)
- FastAPI 서버 + DB 이름 동기화
- TI팀 제출 현황 미표시 버그 수정, UI 통일
- 팀별 비밀번호 정책 수립 및 적용
- ict / rnd / master 버전별 이용 매뉴얼 MD 작성

### 개발 환경 / 툴 세팅
- `/퇴근` Claude Code 커맨드 설치 완료
- collect-today.py Windows python3 경로 이슈 파악

## 주요 성과

- PixiJS SVG 에디터: import → 개체 편집 → export 전체 흐름 동작
- 주간보고 시스템 팀별 매뉴얼 완성, 비밀번호 재설정

## 다음 주 계획

- SVG `<use>` 요소 지원 처리 (flatten 또는 파서 확장)
- monitorplan.html PixiJS 무한 캔버스 정식 도입
- 프로토타입 → 납품용 모듈화 로드맵 실행
- 주간보고 시스템 이슈리스트 기능 연동
