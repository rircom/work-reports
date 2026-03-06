#!/usr/bin/env python3
"""Collect today's work from git commits and Claude session logs."""
import json, os, glob, sys, subprocess, io
from datetime import datetime, timedelta

# Force UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def get_target_date():
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        if arg in ("어제", "yesterday"):
            return (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
        try:
            datetime.strptime(arg, "%Y-%m-%d")
            return arg
        except ValueError:
            pass
    return datetime.now().strftime("%Y-%m-%d")

def decode_project_path(encoded):
    """Decode Claude project dir name back to real filesystem path.

    Claude encodes: F--aiProject-monado-main
    '--' = drive separator (F:/)
    '-' = could be '/' or literal '-' in folder names.
    Try all 2^(n-1) combinations and return the one that exists.
    """
    if "--" not in encoded:
        return None
    parts = encoded.split("--", 1)
    drive = parts[0].upper() + ":/"
    rest = parts[1]

    if not rest:
        return drive.rstrip("/")

    segments = rest.split("-")
    n = len(segments)

    # Each bit in mask decides: 0='/' separator, 1='-' join
    # We have n-1 separators between n segments
    for mask in range(1 << (n - 1)):
        path_parts = [segments[0]]
        for i in range(1, n):
            if mask & (1 << (i - 1)):
                # Join with '-'
                path_parts[-1] = path_parts[-1] + "-" + segments[i]
            else:
                # New path segment
                path_parts.append(segments[i])
        candidate = os.path.join(drive, *path_parts)
        if os.path.isdir(candidate):
            return candidate

    return None


def collect_git_commits(target_date):
    """Scan all known project dirs for git commits on target date."""
    projects_dir = os.path.expanduser("~/.claude/projects")
    results = {}
    if not os.path.isdir(projects_dir):
        return results

    for proj in os.listdir(projects_dir):
        path = decode_project_path(proj)
        if not path or not os.path.isdir(path):
            continue
        if not os.path.isdir(os.path.join(path, ".git")):
            continue
        try:
            r = subprocess.run(
                ["git", "-C", path, "log", "--oneline", "--all",
                 f"--after={target_date} 00:00", f"--before={target_date} 23:59:59",
                 "--format=%h %s"],
                capture_output=True, text=True, encoding="utf-8", timeout=5
            )
            commits = r.stdout.strip()
            if commits:
                results[path] = commits.split("\n")
        except Exception:
            pass

    # Also scan work-reports itself
    wr = os.path.expanduser("~/work-reports")
    if os.path.isdir(os.path.join(wr, ".git")) and wr not in results:
        try:
            r = subprocess.run(
                ["git", "-C", wr, "log", "--oneline", "--all",
                 f"--after={target_date} 00:00", f"--before={target_date} 23:59:59",
                 "--format=%h %s"],
                capture_output=True, text=True, encoding="utf-8", timeout=5
            )
            commits = r.stdout.strip()
            if commits:
                results[wr] = commits.split("\n")
        except Exception:
            pass

    return results

def collect_session_messages(target_date):
    """Extract user messages from Claude session logs for target date."""
    projects_dir = os.path.expanduser("~/.claude/projects")
    results = {}
    if not os.path.isdir(projects_dir):
        return results

    skip_prefixes = ("<", "Base directory", "This session is being", "{", "[")

    for proj in os.listdir(projects_dir):
        proj_path = os.path.join(projects_dir, proj)
        if not os.path.isdir(proj_path):
            continue

        for f in glob.glob(os.path.join(proj_path, "*.jsonl")):
            mtime = os.path.getmtime(f)
            if datetime.fromtimestamp(mtime).strftime("%Y-%m-%d") != target_date:
                continue

            user_msgs = []
            try:
                with open(f, encoding="utf-8") as fh:
                    for line in fh:
                        try:
                            d = json.loads(line)
                            if d.get("type") != "user":
                                continue
                            msg = d.get("message", {})
                            content = msg.get("content", "") if isinstance(msg, dict) else ""
                            texts = []
                            if isinstance(content, list):
                                texts = [c["text"] for c in content
                                         if isinstance(c, dict) and c.get("type") == "text"]
                            elif isinstance(content, str):
                                texts = [content]

                            for txt in texts:
                                txt = txt.strip().replace("\xa0", " ")[:200]
                                if txt and not any(txt.startswith(p) for p in skip_prefixes):
                                    user_msgs.append(txt)
                        except (json.JSONDecodeError, KeyError, TypeError):
                            pass
            except Exception:
                pass

            if user_msgs:
                if proj not in results:
                    results[proj] = []
                results[proj].extend(user_msgs)

    return results

def main():
    target_date = get_target_date()
    print(f"=== 수집 날짜: {target_date} ===\n")

    # Git commits
    commits = collect_git_commits(target_date)
    print("## Git 커밋")
    if commits:
        for path, logs in sorted(commits.items()):
            print(f"\n### {path}")
            for log in logs:
                print(f"  - {log}")
    else:
        print("  (커밋 없음)")

    # Session messages
    print("\n## Claude 세션 대화")
    sessions = collect_session_messages(target_date)
    if sessions:
        for proj, msgs in sorted(sessions.items()):
            readable = decode_project_path(proj) or proj.replace("--", ":/", 1).replace("-", "/")
            print(f"\n### {readable}")
            seen = set()
            count = 0
            for m in msgs:
                if m not in seen and count < 20:
                    seen.add(m)
                    print(f"  - {m}")
                    count += 1
    else:
        print("  (세션 없음)")

if __name__ == "__main__":
    main()
