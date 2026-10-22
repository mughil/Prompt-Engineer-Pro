# Worked Example: Comparing Prompt Variants

## User request
Compare these prompts for summarizing a report:

- **A:** “Summarize this report.”
- **B:** “Summarize the attached report for a nontechnical executive in five bullets, noting key risks and recommended next steps.”

## Comparison

| Criterion | Prompt A | Prompt B |
|---|---|---|
| Goal clarity | Broad | Clear summary task and decision focus |
| Audience | Unspecified | Nontechnical executive |
| Output format | Unspecified | Five bullets |
| Coverage | Open-ended | Key risks and next steps named |
| Flexibility | High, but results may vary | Lower ambiguity, more targeted |

## Recommendation
For an executive decision-support summary, B is better specified because it names the audience, format, and useful content. A may be preferable when the user wants the model to choose the summary style freely. This is a prompt-structure judgment, not empirical proof that B always performs better.

## Optional merged version
```text
Summarize the attached report for a nontechnical executive. Use five concise bullets covering the main findings, key risks, and recommended next steps. Preserve important caveats and do not introduce claims that are not supported by the report. If the report does not support a recommendation, state that clearly.
```

## Validation plan
If actual performance matters, run both prompts on the same representative reports and compare factual accuracy, coverage of important findings, clarity, and usefulness against shared criteria.