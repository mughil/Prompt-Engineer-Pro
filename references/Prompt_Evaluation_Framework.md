# Prompt Evaluation Framework

Score prompts from 0–100 across five equally weighted dimensions. Each dimension receives 0–20 points. Use evidence from the actual prompt, not assumptions about the user's skill.

- Clarity (0–20): goal and instructions are understandable.
- Context (0–20): relevant background, audience, and inputs are present.
- Constraints (0–20): boundaries and requirements are useful and compatible.
- Structure (0–20): task sequence and priorities are organized when needed.
- Output Definition (0–20): deliverable format and success criteria are clear.

Suggested anchors per dimension: 0–4 absent or actively confusing; 5–9 major gaps; 10–14 usable but incomplete; 15–18 strong with minor gaps; 19–20 exceptionally clear for the task. These are judgment anchors, not scientific measurements.

Interpretation: 0–60 Poor; 61–85 Average; 86–100 Excellent. Use judgment when one critical omission materially undermines the prompt; explain any score that seems surprising. Do not imply scores predict model performance or are objectively measured.

A text breakdown is the default. A radar chart is optional only when visualization is supported and useful; never let a chart replace the written explanation.

## Qualitative size label (optional)

Alongside the score you may add a one-word structural size label:

- **short**: a single ask with little or no provided context
- **moderate**: several asks, or one ask with substantial context such as examples or source material
- **long**: a multi-stage workflow or extensive context blocks

Judge the structure, not the word count: a two-sentence prompt describing a five-stage workflow is long; a page of context feeding one question is moderate. Never convert this label into token counts or other exact numbers. A static review cannot measure those, and a fabricated figure is worse than none (see `ROADMAP.md`).

Use the label only when it changes the advice. For example, when a long prompt needs decomposition rather than polish, or a short one needs gaps filled rather than restructuring. Omit it when it adds nothing.
