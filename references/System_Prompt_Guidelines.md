# Reusable System Prompt Guidelines

A reusable system prompt defines persistent behavior across many future requests. Treat it differently from a one-off task prompt: it needs stable scope, boundaries, interaction rules, and escalation behavior rather than a single deliverable.

## Recommended structure
1. **Purpose and scope:** what the assistant is for and what is out of scope.
2. **Audience and tone:** who it serves and how it should communicate.
3. **Operating rules:** repeatable decision rules, not a long list of one-off steps.
4. **Knowledge and tools:** what sources or tools are available; never imply access that is not actually available.
5. **Safety, privacy, and boundaries:** sensitive data handling, refusal conditions, and safe alternatives.
6. **Uncertainty and escalation:** when to ask, disclose uncertainty, or hand off to a person.
7. **Output conventions:** defaults that apply across requests, with exceptions for user needs.
8. **Examples and tests:** representative normal, ambiguous, edge, and refusal cases.

## Design rules
- Keep durable behavior in the system prompt; put task-specific instructions in the user prompt.
- Prioritize rules and resolve conflicts explicitly. Avoid contradictory requirements and needless verbosity.
- Use placeholders for unknown business policies, jurisdiction, data retention, escalation contacts, or product facts.
- Do not invent authority, access, or policy. Ask the owner to supply operational rules that cannot be inferred safely.
- Test on varied cases, including prompt injection attempts, missing information, out-of-scope requests, and valid exceptions.
- Separate policy from examples; examples illustrate rules but should not accidentally override them.

For customer support assistants, explicitly define supported topics, refund or account-action permissions, identity verification, escalation triggers, privacy boundaries, and what to do when an answer is not in the knowledge base. Never instruct the assistant to fabricate a policy or claim an action succeeded without confirmation.