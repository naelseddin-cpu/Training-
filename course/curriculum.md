# Curriculum

## Certification 1: Claude Certified Architect – Foundations (CCA-F)

### Domains and weights (owner's assessment, 2026-09; weights are the
### trainer's allocation of hours, not the exam's blueprint)
| Domain | Baseline | Hours planned | Why |
|---|---|---|---|
| Agentic architecture | 9 | quizzes only | protect, do not teach |
| Prompt engineering | 9 | quizzes only | protect, do not teach |
| Claude Code config / hooks | 7 | 5 (Week 1) | 0 hooks, 0 skills, 0 commands |
| Context & decision memory | 6 | 5 (Week 2) | D-056 cited 173×, defined nowhere |
| Tools & MCP integration | 7 | 5 (Week 3) | 15 tools authored, 0 wired |

### Week 0: The words (prerequisite, built 2026-09-11, rebuilt same evening)
`training/app/words-01.html` — twenty-seven terms starting at the true floor.
One at a time. Each has a plain sentence, an Explain more button the owner
presses as often as he likes, and a check. A wrong answer gives a different
explanation and a different question.

Part 1 · Things on a computer: File · Folder · Path · Program · Run ·
Command · Repository
Part 2 · Working with me: Claude Code · Session · Tool · Tool call ·
Edit/Write/Bash
Part 3 · The lock: Hook · Event · PreToolUse · Matcher
Part 4 · How a hook answers: stdin · stdout/stderr · Exit code · exit 2
Part 5 · Where the lock is listed: JSON · permissionDecision ·
settings.json · Merge
Part 6 · How strict the shift is: Permission · Permission mode ·
bypassPermissions

Nothing in Week 1 may use a word this list has not taught.

### Week 1: Locks (Claude Code config / hooks)
Exam vocabulary covered across the week: hook events, matchers, exit codes
and JSON decisions, settings files and precedence (hooks merge, other keys
override), permission modes, `bypassPermissions` vs allow/deny lists.

| # | Lock | Status |
|---|---|---|
| L1 | Hook 1: block master-file edits while the release gate runs | **in progress**: steps 1–3 (hook, idea, name) delivered with S01+S02 artwork; step 4 waits on the owner's Fork 1 |
| L2 | Hook 2: block `git stash` | planned |
| L3 | Hook 3: Stop hook that runs the decisions guard | planned (depends on Week 2's guard existing; L3 may wire a placeholder that fails loudly) |
| L4 | `/lane` skill: open a worktree lane the way Part IV describes | planned |
| L5 | The `bypassPermissions` fix. The 45-entry allow list is NOT in this repo (no `settings.json` anywhere in it). Owner must paste `~/.claude/settings.json` from the Windows machine into the chat or `training/assets/lesson-05/` before L5. Verified fact to teach: under `bypassPermissions` both `permissions.allow` and `permissions.deny` are dead; hooks still fire and a hook deny still blocks. | blocked on the file |

### Week 2: Memory (context & decision memory)
- `decision_refs_guard.py` in the release gate: every `D-NNN` / `D2-NNN`
  cited in code must resolve to a defined decision.
- Recover D-056, D-011, D-072 into `ALRASSAI.md` with rationale.
- Teach: what belongs in `CLAUDE.md` vs generated state; ratchets.

### Week 3: Hands (tools & MCP)
- `.mcp.json` registering `@alrassai/ops` with read-only `gate_status` and
  `wire_read`.
- Teach: transports, server scoping, resources vs prompts vs tools, output
  capping.

### Then
Mock exam → weak-area repair → same structure for Architect Professional.

## Lesson log
- **2026-09-11 · L1 session 1.** Repo evidence re-checked (see progress.md).
  Build stopped at Fork 1 for the owner's choice. Proof harness ready at
  `training/tools/hook_probe.py`, self-tested. Quiz bank drafted, held.
  First visual pass (flat vector, drawn in the canvas) REJECTED by the owner
  as childish — the fault was the prompt, which asked for flat vector and a
  mascot robot. Replaced by `assets/NANO-BANANA-PROMPTS.md`: a cinematic
  style-and-cast block plus all 30 scenes for lessons 1–15, so the owner
  generates the course's art without returning for prompts. The rejected
  panels and renders were deleted, not kept. Canvas
  https://claude.ai/code/artifact/844339df-c4b2-46a7-8236-af5fa4bc6fea still
  holds the old draft and is rebuilt around the real images when they land.

## Next
Owner answers Fork 1 (how the padlock knows the gate is running), then
Forks 2–4. He writes the hook; trainer runs the probe; quiz; scoreboard.

Artwork in hand: cast plate, S01, S02 (composed into Lesson 1's canvas),
S03 and S04 (banked for Lesson 2). Next on the list is S05–S06, Lesson 3's
Stop hook at the turnstile.

**Session 1 ended with Lesson 1's build not started.** The owner spent the
hour on artwork and did not answer Fork 1 (marker file / process check /
always locked). Recorded as fact, not as a complaint: the visual workflow was
settled from scratch in the same session, which was real work. Session 2 opens
by putting Fork 1 first, before any picture is discussed.
