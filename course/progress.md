# Progress

Scores move only on evidence from the repo. Each row cites what was checked.

## Baseline · 2026-09-11 (trainer re-check of the owner's Sept-2026 self-assessment)

| Domain | Owner claimed | Trainer verified | Score |
|---|---|---|---|
| Agentic architecture | 9 | 24 role-scoped agents in `.claude/agents/`; actions-as-data spine described in `ALRASSAI.md` Part II | 9 (held, not re-examined) |
| Prompt engineering | 9 | not examined | 9 (held) |
| Claude Code config / hooks | 7 | 0 hooks, 0 skills, 0 commands, no `settings.json` or `.mcp.json` anywhere in the repo. The "5,751-line document" does not exist on disk: master is 330 lines, old ledger 2,152 | **7** |
| Tools & MCP integration | 7 | 15 tools in `packages/mcp-server/src/server.ts` + 3 in `drawing-2d`; no `.mcp.json` wires any of them | **7** |
| Context & decision memory | 6 | D-056 cited 173 times (123 in code, 48 in docs), not 526; defined nowhere in `collab/DECISIONS.md` (5 mentions, all references). 97 distinct decision IDs cited in `.py/.ts/.tsx` by a strict regex (owner said 134; counting method differs, the point stands). `CLAUDE.md` names two different files as "the one master" in adjacent paragraphs | **6** |

Weighted: unchanged at the owner's 7.7 until a lesson produces evidence.

## What would move each score (so neither of us moves it on feeling)
- Config/hooks 7 → 8: three working hooks in `.claude/settings.json`, each
  with a probe that shows the deny, and the owner explains exit-code vs JSON
  decision without notes.
- Memory 6 → 7: `decision_refs_guard.py` red on the current tree, green after
  D-056/D-011/D-072 are recovered with rationale.
- MCP 7 → 8: one server in `.mcp.json`, called from a real session, output
  capped, and the owner explains tool vs resource vs prompt.

## Quiz record
(none yet — Lesson 1's quiz is held until its hook is built and proven)

## Session log
- **2026-09-11, session 1.** No score moved, and none should have. Nothing was
  installed in the repo by the owner. What the session did produce: the trainer
  scaffold, a verified baseline, a working proof harness, a browser-based image
  resizer, and a settled visual pipeline (Nano Banana draws, Claude Design
  composes) with four finished pictures and a cast reference that holds across
  generations. Lesson 1 reached step 3 of 7.
