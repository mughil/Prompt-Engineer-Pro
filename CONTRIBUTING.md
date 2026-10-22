# Contributing

Thanks for considering a contribution. This project has a specific philosophy worth reading before you dive in: **match scaffolding to what's actually needed, and back changes with evidence rather than intuition.** The skill itself is opinionated about not over-engineering prompts (see `references/Prompt_Rewrite_Rules.md`, Rule 3) — the project holds its own development to the same bar.

## Before you start

- **Check `ROADMAP.md` first.** If what you want to add is already there, the priority tier and rationale are explained — start from that context rather than re-deriving it.
- **Check `MANIFEST.md`'s "Design decisions worth knowing about" section.** Some things that look like gaps (no token estimates, no specific model-version names, no performance-prediction labels) are deliberate, documented omissions, not oversights.

## Types of contribution

### Bug fixes / drift fixes
Things like stale cross-references, inconsistent terminology across files, or an example that no longer matches SKILL.md's current output template — see `CHANGELOG.md`'s v1.1.1 and v1.2.0 entries for examples of exactly this kind of fix. These are welcome with a small PR and a one-line explanation of what drifted from what.

### New reference content or reference-file changes
- Explain the **why**, not just the **what** — reference files in this project consistently justify their rules rather than stating bare MUSTs (see the Writing Style section of the skill-creator methodology this project follows). A PR that adds a rule without a reason will get asked to add one.
- Check for duplication before adding: does an existing file already cover this? Cross-reference rather than repeat (see how `Feasibility_Assessment.md` and SKILL.md's Contradictions section split responsibility instead of both fully explaining the same thing).
- Keep it general, not overfit to one example prompt you had in mind.

### New evals
Always welcome, especially edge cases the current 21 don't cover. Add to `evals/evals.json` with a realistic prompt and a specific `expected_output` (what to check, not an exact string match — outputs here are judgment-based). Add a corresponding row to `evals/EXPECTED_RESULTS.md`.

### New examples
Worth adding when a behavior is easy to state as a rule but easy to get subtly wrong in practice — that's exactly why `Contradiction_And_Impossibility.md` and `Confidence_Calibration.md` exist (rules alone weren't enough; a worked example was). Follow the existing examples' format: original prompt, score/assessment, the tiered output, and an "Improvements Made" section with reasons.

### New features (P0/P1 items from ROADMAP.md)
These are the highest-value, highest-scrutiny contributions. Expect the review to ask:
1. Is there a concrete failure case (a real prompt this project currently mishandles), or is this speculative?
2. Does it duplicate judgment logic that already exists elsewhere in the skill?
3. Will it go stale — does it name specific model versions, specific numbers, or anything else likely to be wrong within months? (See `CHANGELOG.md`'s "Explicitly deferred" items for what got rejected on this basis before.)

## How to test a change

This project follows the [skill-creator](https://github.com/anthropics/skills) methodology:

1. Make your change to `SKILL.md` or a reference file.
2. Run the existing prompts in `evals/evals.json` through the updated skill (manually, or with an agent that has both the skill and subagent access).
3. Check outputs against `evals/EXPECTED_RESULTS.md`'s pass criteria — these are qualitative (judgment-based), not exact-match assertions.
4. If your change is a new capability, add a new eval for it in the same PR — a feature without an eval is much more likely to regress silently later.
5. Run `python scripts/validate_repo.py` locally. GitHub Actions also runs this integrity check on pushes and pull requests.

## Style

- Imperative form in instructions ("Score the prompt," not "The prompt should be scored").
- Explain reasoning, not just rules — avoid heavy-handed ALL-CAPS MUSTs where a sentence explaining *why* would do the same job better and generalize further.
- Keep `SKILL.md` lean — it's the file loaded into context on every trigger. New detail usually belongs in a `references/` file with a pointer from `SKILL.md`, not inline.

## Versioning

This project uses `MAJOR.MINOR.PATCH`:
- **PATCH** — drift fixes, documentation corrections, no behavior change (e.g., v1.1.1).
- **MINOR** — new evals, new examples, new reference content, behavior refinements that don't change the core workflow (e.g., v1.2.0's Step 0 addition).
- **MAJOR** — new workflow modes (e.g., system-prompt mode, comparison mode — see `ROADMAP.md`'s P0/P1 items, which are v2.0-targeted).

Add an entry to `CHANGELOG.md` for every change that ships, and update `MANIFEST.md`'s structure listing if you add or remove a file.
