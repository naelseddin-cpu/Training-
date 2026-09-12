#!/usr/bin/env python3
"""Proof harness for PreToolUse hooks: feed a hook the same JSON Claude Code
would, show its exit code, stdout and stderr, and say plainly whether the
tool call would have been blocked.

Usage:
  python3 training/tools/hook_probe.py <hook command...> -- <tool> <file_path>
  python3 training/tools/hook_probe.py python3 .claude/hooks/lock_master.py -- Edit ALRASSAI.md
  python3 training/tools/hook_probe.py python3 .claude/hooks/lock_master.py -- Bash "git stash"

For Bash the last argument is the command, not a path. Set the environment
the hook expects (e.g. a marker file) before running; this script changes
nothing on disk.
"""
import json
import os
import subprocess
import sys


def main(argv):
    if "--" not in argv:
        print(__doc__)
        return 2
    i = argv.index("--")
    cmd, rest = argv[:i], argv[i + 1:]
    if len(rest) != 2 or not cmd:
        print(__doc__)
        return 2
    tool, arg = rest
    cwd = os.getcwd()
    if tool == "Bash":
        tool_input = {"command": arg}
    else:
        tool_input = {"file_path": os.path.abspath(arg)}
    payload = {
        "session_id": "probe",
        "transcript_path": "/dev/null",
        "cwd": cwd,
        "permission_mode": "bypassPermissions",
        "hook_event_name": "PreToolUse",
        "tool_name": tool,
        "tool_input": tool_input,
    }
    proc = subprocess.run(cmd, input=json.dumps(payload), capture_output=True, text=True)
    out, err = proc.stdout.strip(), proc.stderr.strip()

    blocked = False
    why = ""
    if proc.returncode == 2:
        blocked, why = True, "exit code 2"
    elif out:
        try:
            decision = json.loads(out).get("hookSpecificOutput", {}).get("permissionDecision")
            if decision == "deny":
                blocked, why = True, "permissionDecision: deny"
            elif decision == "ask":
                why = "permissionDecision: ask (user would be prompted)"
        except json.JSONDecodeError:
            why = "stdout is not JSON; ignored by Claude Code"

    print(f"tool      : {tool} {tool_input}")
    print(f"exit code : {proc.returncode}")
    print(f"stdout    : {out or '(empty)'}")
    print(f"stderr    : {err or '(empty)'}")
    if blocked:
        print(f"RESULT    : BLOCKED ({why})")
    elif proc.returncode not in (0, 2):
        print(f"RESULT    : NOT blocked. Exit {proc.returncode} is a non-blocking error; the tool runs.")
    else:
        print(f"RESULT    : NOT blocked{(' — ' + why) if why else ''}")
    return 0 if blocked else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
