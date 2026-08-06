# Roadmap — v2.0

This is a working list, not a promise — items move, merge, or get dropped as real usage tells us more than speculation can. Priority is based on: how often the gap actually bites (from eval failures and dogfooding), how cheap the fix is to build and maintain, and how likely it is to stay correct over time (a feature that goes stale in a month is worth less than its size suggests).

## How items are prioritized

- **P0** — Known gap with a concrete failure mode already surfaced (an eval exists, or a real review went wrong). Build these first.
- **P1** — Clear value, no urgent forcing function yet. Build after P0s, or sooner if a user hits it.
- **P2** — Plausible value, meaningfully larger scope or maintenance burden. Needs more evidence before committing.
- **Deferred / not planned** — considered and rejected, or genuinely out of scope; kept here so the reasoning doesn't get re-litigated from scratch.

---

## P0 — Known gaps with a concrete failure mode

### 1. Reusable / system-prompt mode
**The gap:** Eval 20 (v1.2) exposes this directly — the skill has no dedicated handling for prompts that aren't one-off tasks but persistent instructions governing many future, unknown inputs (system prompts, agent instructions, bot personas). Right now it applies one-off-task heuristics (audience, single success criterion, one desired output) to something that actually needs robustness across a distribution of future inputs it can't see.
**What "done" looks like:** A `references/System_Prompt_Guidelines.md` covering what changes: scope boundaries (what's explicitly out of scope, not just what's in scope), behavior under adversarial or off-topic input, consistency across many invocations rather than one, and how "success" for a reusable prompt is closer to Prompt_Quality_Heuristics #10 (edge cases) than to a single deliverable's success criteria. `Domain_Detection.md` should be able to flag "this reads like a system prompt" as a signal independent of topic domain.
**Why P0, not P1:** It's the one gap this release's own eval suite documents as unaddressed rather than fixed — shipping v2.0 without it means the eval stays red on purpose.

### 2. Prompt-comparison mode ("which of these is better")
**The gap:** The entire skill assumes one prompt in, one (tiered) prompt out. A user handing over two or three prompt variants and asking which to use, or how they differ, doesn't fit the AIM workflow — it would currently either get analyzed as if only one mattered, or handled ad hoc with no consistent format.
**What "done" looks like:** A lightweight comparison path: score each variant independently using the existing rubric, then a short head-to-head on the dimensions that actually differ (don't repeat identical scores), plus a recommendation. Reuses `Prompt_Evaluation_Framework.md` rather than inventing new scoring — this is a new *output shape*, not new judgment criteria.
**Why P0:** It's a natural, likely-common request ("I wrote it two ways, which is better?") that the skill's own description doesn't currently claim to handle, so it's either silently mishandled or silently out of scope — worth resolving one way or the other.

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
