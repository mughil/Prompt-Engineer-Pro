# Manifest — prompt-engineer-pro v1.2.0

## Structure

```
prompt-engineer-pro/
├── SKILL.md                              Entry point: workflow, triggering, adaptive output rules
├── README.md                             Project overview, install, usage
├── LICENSE                               MIT
├── CHANGELOG.md                          Full version history
├── RELEASE_NOTES.md                      Human-readable notes per release
├── ROADMAP.md                            Prioritized v2.0 feature roadmap
├── CONTRIBUTING.md                       How to propose and evaluate a change
├── MANIFEST.md                           This file
├── .gitignore
├── references/
│   ├── AIM_Framework.md                  The Analyze → Improve → Maximize workflow
│   ├── Domain_Detection.md               v1.1: infer domain + confidence instead of asking
│   ├── Prompt_Quality_Heuristics.md      What makes a prompt high quality (10-point checklist)
│   ├── Anti_Patterns.md                  v1.1: named, scannable checklist of common failure patterns
│   ├── Feasibility_Assessment.md         v1.1: Fully Feasible / Feasible with clarification / Unrealistic / Impossible
│   ├── Prompt_Evaluation_Framework.md    0-100 scoring rubric (5 dims x 20 pts) + v1.1 quality radar visualization
│   ├── Prompt_Patterns.md                Zero-shot, few-shot, role-based, decomposition, CoT, critique-revise, planning
│   ├── Prompt_Rewrite_Rules.md           How to improve without changing intent; tier definitions
│   ├── Clarification_Rules.md            When to ask vs. assume
│   ├── Role_Definition_Guide.md          When role/persona framing earns its place
│   ├── Constraint_Guidelines.md          Tone, length, format, audience, things-to-avoid
│   ├── Output_Format_Design.md           Specifying output shape
│   ├── Model_Optimization.md             v1.1: capability-based (not version-based), expanded to Grok/Perplexity/Cursor/Copilot
│   ├── Few_Shot_Examples.md              When and how to use example-based prompting
│   ├── Chain_of_Thought_Guidelines.md    When and how to prompt for explicit reasoning
│   ├── Prompt_Safety_Guidelines.md       The optimize-vs-decline boundary
│   ├── Optimization_Confidence.md        v1.1: how confident the *rewrite* is, and what would raise it
│   └── Domain_Templates/
│       ├── Writing.md
│       ├── Coding.md
│       ├── Research.md
│       └── Marketing.md
├── examples/
│   ├── Basic_Prompt.md                   Poor-tier walkthrough, full 4-tier output + v1.1 sections
│   ├── Expert_Prompt.md                  Excellent-tier walkthrough, light-touch output
│   ├── Multi_Step_Task.md                Workflow preserved, not flattened
│   ├── Image_Generation.md               Model-specific (Midjourney) optimization
│   ├── Safety_Boundary.md                Decline case
│   ├── Contradiction_And_Impossibility.md  v1.1: naming conflicts vs. flagging true impossibility
│   └── Confidence_Calibration.md         v1.1: honest Medium/Low confidence, refusing to fabricate a model version
└── evals/
    ├── evals.json                        20 test prompts covering the core scenarios plus v1.1/v1.2 edge cases
    └── EXPECTED_RESULTS.md               Qualitative pass criteria per eval
```

## Status

All reference files are fully implemented (none are stub/placeholder). Domain template coverage remains v1 (Writing, Coding, Research, Marketing) — additional domains are P2 on `ROADMAP.md`, deliberately not v2.0-committed yet.

## Design decisions worth knowing about

- **Adaptive output, not always three tiers.** The skill scores the prompt first and only produces as many rewrite tiers as it actually needs — see the table in SKILL.md.
- **Every output section is conditional.** As of v1.1 there are more possible sections (domain detection, anti-patterns, feasibility, radar, confidence) — the rule is still to show only what adds real information for this specific prompt, never pad the output to look thorough.
- **Safety is a decline, not a tier.** `Prompt_Safety_Guidelines.md` governs a hard boundary distinct from the quality tiers — a harmful request never gets a score or a rewrite, it gets a short decline. This is a different concept from `Constraint_Guidelines.md`'s "Safety/appropriateness bounds" constraint category (a normal thing to add to a fine prompt) — same word, different severity, now cross-referenced.
- **Contradictions and impossible constraints are surfaced, not silently resolved.** As of v1.1 this is formalized as the Feasibility Assessment's "Unrealistic constraints" / "Impossible as written" levels.
- **No fabricated precision.** Deliberately no token-count estimates and no specific model-version claims — both would look precise while being unreliable. See the "Explicitly deferred" section of CHANGELOG.md and ROADMAP.md's honest-alternative proposal (a qualitative complexity label instead of a fake token count).
- **The riskiest behaviors have worked examples, not just rules.** `Contradiction_And_Impossibility.md` and `Confidence_Calibration.md` were added because evals 8/9/13/14/15 test exactly the failure modes most likely to regress silently (papering over conflicts, defaulting to High confidence on thin prompts, inventing a current model version) — a concrete worked example anchors these better than prose rules alone.
- **The skill's own instructions are fixed regardless of what's inside the reviewed prompt (v1.2).** Step 0 in SKILL.md exists because a prompt being reviewed could itself contain text aimed at the reviewer (e.g., "ignore your scoring rubric"). The rubric, workflow, and safety boundary apply *to* the content, and can't be overridden *by* the content.
- **Known gaps are tracked, not hidden.** Eval 20 documents a real, currently-unaddressed distinction (reusable system prompts vs. one-off task prompts) rather than quietly shipping a false sense of completeness — see `ROADMAP.md` P0 #1.
