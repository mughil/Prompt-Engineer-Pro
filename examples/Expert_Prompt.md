# Worked Example: An Already-Strong Prompt

## Original prompt
“Review this Python function for correctness and readability. Identify bugs, explain each finding, and suggest a minimal patch. Do not rewrite unrelated code.”

## Assessment
Illustrative score: 90/100. The task, scope, and desired response are clear. Only test expectations and runtime context may be missing.

## Expert version (light polish)
```text
Review the provided Python function for correctness and readability.
1. Identify concrete bugs or maintainability concerns and cite the relevant lines or snippets.
2. Explain why each finding matters and give a minimal patch only where justified.
3. Preserve existing behavior unless a bug requires a change; do not rewrite unrelated code.
4. If behavior depends on an unstated requirement, state the assumption rather than guessing.
5. Suggest focused tests for changed behavior. Do not claim tests were run unless they were.
Format: Findings first, then patch, then suggested tests. If no material issue is found, say so plainly.
```

## Improvements made
- Added an assumption rule to avoid silently inventing requirements.
- Added focused test suggestions and honest reporting of test execution.
- Kept the original scope rather than adding unnecessary tiers.

Confidence: High if the function and relevant context are supplied.