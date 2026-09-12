# Lesson 1 quiz · Locks: the first hook

Status: drafted 2026-09-11, HELD until the owner's hook is built and proven.
Answer key and scoring are added after he answers.

1. Your hook script exits with code 1 and prints "master file locked" to
   stderr. What happens to the Edit call?
   A. It is blocked and Claude reads the message.
   B. It runs; the message is shown to the user as a non-blocking error.
   C. It is blocked silently.
   D. Claude Code asks the user for permission.

2. `.claude/settings.json` defines a PreToolUse hook on `Edit|Write` and
   `~/.claude/settings.json` defines a different PreToolUse hook on `Edit`.
   An Edit call arrives. Which hooks run?
   A. Only the project one; project settings override user settings.
   B. Only the user one; user settings are read last.
   C. Both; hooks from every settings file are merged.
   D. Neither; two hooks on the same event is a configuration error.

3. The session runs in `bypassPermissions`. `permissions.deny` lists
   `Edit(ALRASSAI.md)`. Your PreToolUse hook also denies edits to that file.
   Which one stops the edit?
   A. The deny rule; deny rules always win.
   B. The hook only; deny rules are not enforced in bypassPermissions.
   C. Neither; bypassPermissions skips hooks too.
   D. Both, and the user sees two refusals.

4. Which matcher fires your hook for Edit and Write but not for Bash?
   A. `"matcher": "edit|write"`
   B. `"matcher": "Edit|Write"`
   C. `"matcher": "*"`
   D. `"matcher": "tool_input.file_path"`

5. Your hook wants to refuse with a reason but keep the exit code at 0. Which
   stdout is honoured by a PreToolUse hook?
   A. `{"decision": "block", "reason": "..."}`
   B. `{"hookSpecificOutput": {"hookEventName": "PreToolUse", "permissionDecision": "deny", "permissionDecisionReason": "..."}}`
   C. `{"permission": "deny"}`
   D. Any non-empty stdout is treated as a refusal.

## Owner's answers
(pending)

## Mistakes and pattern
(pending)
