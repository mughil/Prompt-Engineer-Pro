# Roadmap — v2.0

This is a working list, not a promise — items move, merge, or get dropped as real usage tells us more than speculation can. Priority is based on: how often the gap actually bites (from eval failures and dogfooding), how cheap the fix is to build and maintain, and how likely it is to stay correct over time (a feature that goes stale in a month is worth less than its size suggests).

## How items are prioritized

- **P0** — Known gap with a concrete failure mode already surfaced (an eval exists, or a real review went wrong). Build these first.
- **P1** — Clear value, no urgent forcing function yet. Build after P0s, or sooner if a user hits it.
- **P2** — Plausible value, meaningfully larger scope or maintenance burden. Needs more evidence before committing.
- **Deferred / not planned** — considered and rejected, or genuinely out of scope; kept here so the reasoning doesn't get re-litigated from scratch.

---

## P0 — Completed in v2.0.0

The two previously documented P0 gaps now have dedicated workflows, reference guidance, and regression cases:

- **Reusable/system-prompt mode:** `references/System_Prompt_Guidelines.md` defines persistent scope, operating rules, boundaries, uncertainty, escalation, and test coverage. The skill's mode detection routes reusable assistant instructions to this guide; eval 20 covers the distinction from one-off prompts.
- **Prompt-comparison mode:** `references/Prompt_Comparison_Guidelines.md` defines shared-criteria comparison, evidence-based recommendations, and when empirical testing is required. Eval 21 covers a comparison case.

These are implemented in the source tree. The qualitative suite and repository integrity workflow are in place; model-output evaluation remains a manual review process rather than a claim of automated quality scoring.

---

## P1 — Clear value, not yet urgent

### 3. Prompt library / starter templates by domain
Deferred from v1.1 as "v3-scale scope" — revisit at smaller scope for v2.0: not a full library across Legal/Healthcare/Finance/PM, but 1-2 starter templates per *existing* domain (Writing, Coding, Research, Marketing) as optional starting points a user can point to ("start from the SEO template") rather than always starting from a blank prompt. Meaningfully smaller than the original ask and reuses domains already built out.

### 4. Qualitative complexity label (not a token estimate)
v1.1 explicitly deferred token/context-size estimates as false precision (no real tokenizer, a fabricated-looking number). The honest version — a qualitative label like "short / moderate / long" based on structure (single ask vs. multi-stage workflow, presence of examples/context blocks) — was flagged as the right version if revisited. Low cost, low risk of going stale, since it's relative rather than numeric.

### 5. Batch mode for multiple unrelated prompts in one message
If a user pastes 3 unrelated prompts and asks to improve all of them, the current skill doesn't specify how to structure that (three full reviews back to back gets long fast). Worth a lightweight convention — e.g., condensed per-prompt output (score + top 2-3 changes) unless the user asks for full depth on all of them.

---

## P2 — Plausible value, needs more evidence first

### 6. Multi-agent / sub-agent decomposition framing
Deferred from v1.1 as "mostly a relabeling of existing decomposition/multi-step handling." Revisit only if a concrete case shows explicit "Agent 1 does X, Agent 2 does Y" framing produces a meaningfully different (not just differently-labeled) rewrite than the existing Decomposition pattern already produces.

### 7. Additional domain templates (Legal, Data/Analytics, Academic)
More domains than the current four could plausibly benefit from dedicated templates. Held at P2 rather than P1 because each new template is ongoing maintenance surface (drift risk, like the AIM_Framework staleness this release fixed) — only add one where General-principle reviews are demonstrably falling short, not speculatively.

### 8. Structured/JSON output mode for programmatic use
An optional machine-readable output (score breakdown, tiers, confidence as JSON) alongside the human-readable review, for users piping this into other tooling. Real but currently hypothetical demand — build if a user asks, not preemptively.

---

## Deferred / not planned (kept from v1.1, still correct not to build)

- **Token/context-size estimates as exact numbers.** Would require a real tokenizer; a fabricated-looking number is false precision. See P1 #4 for the honest qualitative version instead.
- **Model-version-specific recommendations** (naming a specific numbered release in a static file). Goes stale immediately; this is correctly a live-search task, not a reference-file task, and `Model_Optimization.md` already says so.
- **Performance prediction** ("Expected Result: High"). Redundant with score + radar + anti-patterns + feasibility + confidence once those exist — it would be a label, not new information.

---

## Not on this list on purpose

Anything that would turn this into a general-purpose writing or coding assistant rather than a prompt-engineering reviewer is out of scope regardless of priority tier — e.g., actually *executing* the improved prompt and returning its output, rather than returning the improved prompt itself. That's a different tool with a different safety and quality surface; conflating the two would blur what this skill is for.
