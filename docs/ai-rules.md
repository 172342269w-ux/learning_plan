# AI Learning Rules

AI can help me learn, review, and debug, but it should not replace my core practice.

## Good Uses

- Explain an error message.
- Review my code.
- Explain syntax.
- Suggest test cases.
- Check deployment steps.
- Point out edge cases.

## Bad Uses

- Asking AI to write all core logic before I try.
- Copying code I cannot explain.
- Expanding the plan whenever I feel bored.
- Switching stacks before finishing the current project.

## Core Rule For This Repo

- For learning exercises, I write the first version myself.
- Codex should help by breaking the task down, explaining concepts, reviewing my code, pointing out mistakes, and verifying results.
- Codex should not write the core answer for me unless I explicitly say `你来写` or `直接帮我实现`.
- If Codex accidentally starts moving too fast, it should stop and return the task to me instead of finishing the exercise on my behalf.

## What Codex May Draft

- Learning skeletons and starter files.
- README structure.
- Logs and review notes.
- Repetitive boilerplate that is not the learning target.

## What I Should Handwrite First

- Core functions in real tools.
- Database models and core business logic.
- Authentication logic.
- Error handling paths I need to understand.
- Anything I plan to explain in a review or demo.

## How We Work

- I try first.
- Codex gives the smallest useful hint.
- I rewrite the key part in my own words or code.
- Codex checks for mistakes and edge cases.
- If the code is for a real project, the core part must be mine before it counts as learned.

## Required Prompt Format

When asking AI for help, I should say:

```text
I expected:
I actually got:
I already tried:
Please review from this angle:
```

Useful review angles:

- beginner syntax mistakes
- edge cases
- readability
- error handling
- deployment risk
