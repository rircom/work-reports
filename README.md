# Work Reports

Claude Code `/퇴근` 명령으로 자동 생성되는 팀 업무보고 저장소.

## 구조

```
work-reports/
├── daily/          # 일일 작업일지 (YYYY-MM-DD.md)
├── weekly/         # 주간 요약 (YYYY-WNN.md)
├── monthly/        # 월간 요약 (YYYY-MM.md)
└── README.md
```

## 사용법

### 1. 이 레포 클론
```bash
git clone https://github.com/rircom/work-reports.git H:\Claude\work-reports
```

### 2. `/퇴근` 커맨드 파일 복사
아래 내용을 `~/.claude/commands/퇴근.md`에 저장:

> 이 파일은 레포의 `setup/퇴근.md`에 포함되어 있습니다.

### 3. 사용
Claude Code에서 `/퇴근` 입력하면 자동으로:
- 오늘 작업 내용 정리
- `daily/YYYY-MM-DD.md` 파일 생성
- git commit & push
- 금요일이면 주간 요약도 생성
- 말일이면 월간 요약도 생성

## 팀원 설정

각 팀원이 아래 작업을 수행:

1. 이 레포의 collaborator로 추가 (또는 fork)
2. 레포 클론: `git clone https://github.com/rircom/work-reports.git H:\Claude\work-reports`
3. `setup/퇴근.md` 파일을 자신의 `~/.claude/commands/퇴근.md`로 복사
4. Claude Code에서 `/퇴근` 사용

## 파일 네이밍

팀원 구분을 위해 파일명에 작성자가 포함됩니다:
- `daily/YYYY-MM-DD-{username}.md`
- `weekly/YYYY-WNN-{username}.md`
- `monthly/YYYY-MM-{username}.md`
