# Work Reports

Claude Code `/퇴근` 명령으로 자동 생성되는 팀 업무보고 저장소.

## 구조

```
work-reports/
├── daily/          # 일일 작업일지 (YYYY-MM-DD-{username}.md)
├── weekly/         # 주간 요약 (YYYY-WNN-{username}.md)
├── monthly/        # 월간 요약 (YYYY-MM-{username}.md)
└── README.md
```

## 빠른 시작 (팀원용)

### 1. 레포 클론 (홈 디렉토리에)
```bash
git clone https://github.com/rircom/work-reports.git ~/work-reports
```

### 2. 퇴근 커맨드 설치
```bash
cp ~/work-reports/setup/퇴근.md ~/.claude/commands/퇴근.md
```

### 3. 사용
Claude Code에서 `/퇴근` 입력하면 자동으로:
- 오늘 작업 내용 정리
- `daily/YYYY-MM-DD-{username}.md` 파일 생성
- git commit & push
- 금요일이면 주간 요약도 생성
- 말일이면 월간 요약도 생성

날짜 지정도 가능:
- `/퇴근 어제` - 어제 날짜로 작성
- `/퇴근 2025-03-04` - 특정 날짜로 작성

## 참고

- 레포가 없으면 `/퇴근` 실행 시 자동 클론됩니다
- 파일명에 git user.name이 포함되어 팀원 구분
- 충돌 방지를 위해 push 전 자동 pull --rebase
