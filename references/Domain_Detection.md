# Domain Detection

Infer the domain from the requested task, not from a user's identity or a guess about their profession. Also identify the prompt's *use mode* independently of its topic: one-off task, reusable system/assistant instructions, or comparison of multiple variants. A reusable system prompt may be about writing, coding, support, or another domain; its persistent behavior requirements are a separate design concern. Use a domain template only when it materially improves the result.

- Writing: articles, stories, scripts, editing, tone, audience, or editorial structure.
- Coding: implementation, debugging, architecture, tests, or code review.
- Research: evidence gathering, synthesis, comparison, or source evaluation.
- Marketing: positioning, campaigns, SEO, ads, social content, or conversion.
- General: tasks that do not clearly fit the above.

Report High confidence when the task and expected output clearly identify a single domain; Medium when multiple domains plausibly apply; Low when context is too sparse. Naming more than one domain is itself evidence that several domains plausibly apply: a multi-domain label is always reported at Medium confidence, never High. Do not ask the user to classify a domain if the prompt itself provides enough evidence. Omit the domain line for General or when it adds no useful information. Domain detection is a convenience, not a claim of certainty.
