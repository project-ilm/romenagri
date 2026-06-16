# AI_CONTRACT.md — Working Agreement for AI Collaborators on Project ILM

**Copyright © 1993–2026 Abhishek Choudhary. GPL-3.0-or-later.**

Binding on any AI (Claude, GPT, Gemini, Codex, other) working on Project ILM
repos or the maintainer's machine. Read before acting.

## 0. Identity & ownership
- Independent IP of Abhishek Choudhary, © 1993–2026, GPL unless stated.
- Never reference or attribute anything to any employer, past or present.
- Every artifact carries the copyright line.

## 1. Filesystem confinement (HARD RULE)
- All work stays under `~/work/11jun`. Nothing written to `$HOME`, stray `/tmp`,
  or anywhere outside `~/work/11jun`.
- Scripts → `~/work/11jun/scripts/`. Scratch clones → `~/work/11jun/build/`.
- To transform/release a repo, clone fresh into `build/` — never modify a
  working copy in place. Maintainer's working copies are read-only unless told.

## 2. Never silence errors (HARD RULE)
- Do NOT send stderr of a failable step to /dev/null. A blank "build failed"
  with no log is forbidden.
- Show output, or tee to `~/work/11jun/logs/` and print the tail on failure:
  `if ! cmd > "$LOG" 2>&1; then echo FAILED:; tail -30 "$LOG"; exit 1; fi`
- Diagnose before fixing. Never guess when the real error is one un-silenced
  command away.

## 3. Scripts complete & self-contained
- Full script in one paste-ready block. No sed/python patches against prior
  scripts — that corrupts context.
- Single `cat > file <<'EOF'` blocks; robust preflight; `[STATUS]` lines.
- externally-managed Python → `pip install --user --break-system-packages`.
- Idempotent: wipe/recreate scratch dirs so re-runs are safe.

## 4. Honesty (HARD RULE)
- Honest figures only; never claim unshipped as shipped.
- Always name the kernel variant (2003-04 vs chintamani) with measurements.
- Coverage is flagged-not-faked. Report adverse results plainly.
- Verify against real code/repo before building.

## 5. Respect existing architecture
- Review existing work first; never reinvent. Hindawi already has working
  bidirectional transducers (C, C++, BASIC, Java, lex, yacc, x86 asm).
- Localization flows through the Romenagri pipeline. NEVER use `#define`.
- Keep three axes separate: SCRIPT / LANGUAGE / STANDARD. Scope is unbounded;
  current counts are measured state, not ceilings.

## 6. Irreversible actions gated
- DOI minting, PyPI upload, deletion, force-push: never unprompted. Confirm
  inputs; rehearse (dry-run/sandbox); gate behind explicit confirmation.
- Secrets only from the environment. Never hardcode/echo/commit. Flag any
  secret that appears in chat for rotation.

## 7. Communication
- No flattery, grandiosity, or psychologizing. Be direct.
- Maintainer escalation = the work is wrong; engage the correction, don't stall.
- Localize deliverables where asked.
