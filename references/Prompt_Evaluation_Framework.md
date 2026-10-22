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