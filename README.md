# Prompt Engineer Pro

A Claude [Skill](https://docs.claude.com/en/docs/agents-and-tools/agent-skills) that turns rough prompts into well-specified, high-performing ones — with a consistent process, an honest scoring rubric, and an explanation of *why* each change helps, not just a rewrite.

Prompt Engineer Pro treats prompt engineering as a discipline, not a one-off polish pass: **Analyze → Improve → Maximize**.

- **Analyze** — score the prompt (0-100, five weighted dimensions), detect its domain, name contradictions or impossible constraints, flag recognizable anti-patterns.
- **Improve** — apply the right structural pattern (zero-shot, few-shot, role-based, decomposition, chain-of-thought, critique-and-revise, planning), fill genuine gaps with clearly labeled assumptions, never silently change what you were actually asking for.
- **Maximize** — tailor the result to the target model (Claude, ChatGPT, Gemini, Grok, Perplexity, Cursor/Copilot, Midjourney/image models), and scale output to how much the prompt actually needs — an already-excellent prompt gets light polish, not three redundant rewrites.

## Why

A prompt is a specification. Vague specifications produce inconsistent output not because the model is weak, but because it had to guess at intent, context, constraints, and success criteria that were obvious to the person writing the prompt and invisible to the model reading it. This skill's job is making that implicit knowledge explicit.

## What you get back

A structured review — score, breakdown, detected domain, feasibility rating, anti-patterns, strengths, weaknesses, missing information — followed by one to three tiers of rewritten prompt (only as many as the original actually needs), each improvement paired with a one-line reason, and an honest confidence rating on the rewrite itself.

Every section of the output is conditional: a short, clean prompt that's already solid gets a short, clean review, not padded-out sections that don't apply.

## Install

**Important:** Prompt Engineer Pro is packaged as a Claude Skill. Its ability to optimize prompts for ChatGPT, Gemini, or other models does **not** mean the skill package can be installed natively in those products. Choose the setup that matches the environment where you want to run the instructions.

### Option A — Install as a Claude Skill

1. Open the project's [GitHub Releases](https://github.com/mughil/Prompt-Engineer-Pro/releases) page.
2. Open the latest stable release and download the `prompt-engineer-pro-vX.Y.Z.skill` asset. Download the source ZIP only if you need the development files.
3. Use the `.skill` package only in a Claude environment that supports importing skill packages. Follow that environment's current skill-installation instructions.
4. If your Claude environment expects a skills folder instead, extract the package and place the `prompt-engineer-pro/` folder in that environment's configured skills directory. The folder should contain `SKILL.md`, `references/`, and `examples/`.
5. Enable the skill if the host environment requires it, then start a new conversation and try the test prompt below.

The exact installation UI and supported import methods can vary by Claude product and account. If your environment does not offer skill import or a configured skills directory, do not assume the package can be installed there.

**Maintainers:** pushing a version tag such as `v2.0.1` builds version-named packages and publishes them as assets on a GitHub Release. Pull-request and branch builds remain temporary workflow artifacts for validation; they are not stable download links.

### Option B — Use the instructions in ChatGPT manually

The `.skill` package is **not** a native ChatGPT Skill import. If Skills are unavailable on your ChatGPT account, you can use the project as a manual reference instead:

1. Create or open a ChatGPT Project.
2. Copy the core operating instructions from `SKILL.md` into the project's **Instructions** field.
3. Upload `SKILL.md` and any relevant files from `references/` as project files, subject to your account's file limits.
4. Start a chat inside that project and ask it to analyze, improve, or compare a prompt using the project instructions.

This manual setup is a workaround, not a native installation. ChatGPT will follow the supplied instructions as context; behavior may differ from a supported skill runtime.

### Quick installation check

After setting up the skill or manual workflow, try:

> Use Prompt Engineer Pro to improve this prompt for ChatGPT: "Write about the best running shoes."

A working setup should identify missing context such as audience, purpose, and output format, then provide an improved prompt. This is a smoke test of the basic workflow, not a full quality evaluation.

### Validation and evaluation: what each check proves

These checks serve different purposes; passing one does not imply the others passed.

1. **Repository and package validation (automated CI):** GitHub Actions checks repository integrity and builds the `.skill` and source ZIP archives, then checks that the archives are readable and contain expected files. This validates structure and packaging only. It does **not** install the skill into a live host, run prompts through a model, or measure response quality.
2. **Installation smoke test (manual):** Install or configure the skill using one of the methods above, start a fresh conversation, and run the quick-check prompt. Confirm that the setup is available and produces a relevant rewrite. Record the host product and whether this test passed; do not treat one successful prompt as proof of broad quality.
3. **Qualitative evaluation (manual):** Run the prompts in `evals/evals.json` through the skill in the intended host environment. Compare each response with the corresponding behavior criteria in `evals/EXPECTED_RESULTS.md`, mark **Pass / Partial / Fail**, and add a short evidence note. For failures, revise the smallest relevant rule and rerun the failed case plus adjacent cases.

The evaluation suite uses human judgment, not exact-output matching. Unless a repeatable model-running harness and recorded results are added, describe results as qualitative review—not automated, statistical, or benchmark validation.

### Legacy archive warning

**Do not use `files.zip` as the current release package.** It is a legacy archive and has not been regenerated to match the repaired source tree. Use the package built by the **Build skill packages** workflow instead. The tracked source tree is canonical.

Stable downloads are published as versioned assets on the [GitHub Releases page](https://github.com/mughil/Prompt-Engineer-Pro/releases) when a `v*` tag is pushed. Pull-request and branch builds use versioned workflow artifacts that expire after 30 days; use those artifacts for build verification, not as permanent release downloads.

The installed skill should have this structure:

```
prompt-engineer-pro/
├── SKILL.md
├── references/
└── examples/
```

The `evals/` folder is development-only and should be excluded from the installed skill package.

## Use

Once installed, it triggers automatically when you ask to improve, rewrite, optimize, score, or critique a prompt — including "engineer this prompt," "make this better for [model]," or pasting a rough prompt and asking how to sharpen it. See the `description` field in `SKILL.md` for the exact trigger conditions, including what it deliberately does *not* trigger on (e.g., "write me a prompt for X" is a content request, not a prompt-engineering request).

**Example:**

> Use Prompt Engineer Pro on: "write about the best running shoes"

Returns a score (likely Poor-tier — no audience, angle, or format specified), the specific gaps that caused it, and a tiered rewrite with a concrete angle and audience baked in.

## What it won't do

If the underlying request is for something that shouldn't be fulfilled regardless of phrasing — help with wrongdoing, generating harmful content, bypassing safety measures — the skill declines to optimize it rather than producing a more polished, more effective version of a harmful request. See `references/Prompt_Safety_Guidelines.md` and `examples/Safety_Boundary.md` for exactly where that line sits (it's narrower than you might expect — most sensitive-topic prompts, from security research to dark fiction, are completely fine to optimize; the line is about what's being asked *for*, not the topic's sensitivity).

## Repository structure

```
prompt-engineer-pro/
├── SKILL.md                    Entry point — workflow, triggers, output template
├── references/                 23 reference files, loaded as needed (progressive disclosure)
│   └── Domain_Templates/       Writing, Coding, Research, Marketing
├── examples/                   9 worked walkthroughs, including the trickiest edge cases
├── evals/                      21 test prompts + qualitative pass criteria (dev-only)
├── MANIFEST.md                 Full file listing + key design decisions
├── CHANGELOG.md                Version history
├── ROADMAP.md                  Prioritized v2.0 feature roadmap
├── RELEASE_NOTES.md             Human-readable notes for the current release
├── CONTRIBUTING.md              How to propose a change and how it gets evaluated
└── LICENSE                     MIT
```

Reusable system-prompt design and prompt-variant comparison have dedicated workflows. See `MANIFEST.md` for the full file-by-file breakdown and the design decisions behind them (adaptive output, conditional output sections, no fabricated precision).

## Contributing

See `CONTRIBUTING.md`. Short version: this project follows the [skill-creator](https://github.com/anthropics/skills) iteration loop — draft, test against `evals/evals.json`, get qualitative review against `evals/EXPECTED_RESULTS.md`, revise. PRs that add scaffolding without an eval or a concrete failure case behind them are likely to get pushback — see Rule 3 in `references/Prompt_Rewrite_Rules.md` for why the skill itself is opinionated about over-scaffolding, and the project holds itself to the same standard.

## License

MIT — see `LICENSE`.
