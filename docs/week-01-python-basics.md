# Week 1 - Python Basics

Current reality at the start of Week 1:

> I was starting from almost zero Python.

So this week was never about building the full monitor immediately. It was about becoming able to read, change, run, explain, and slowly rebuild small Python scripts.

## Week 1 Goal

By the end of this week, I wanted to be able to:

- Run Python scripts from PowerShell
- Use variables, strings, numbers, lists, and basic dictionaries
- Use `if/else`
- Use `for` loops
- Write and call small functions
- Read one command line argument
- Make Git commits and push to GitHub

## Week 1 Result

By the end of Week 1, I completed:

- Day 0 to Day 5 Python basics practice
- Day 6-7 review
- `site_probe.py` real tool practice
- `cert_days_left.py` real TLS tool practice
- `cert_days_left_rebuild.py` rebuild practice

Current result:

- I am no longer at "completely zero Python"
- I can run, modify, and explain beginner scripts
- I can complete a small real tool with step-by-step guidance
- I still need more practice to handwrite everything smoothly without prompts

## Day 0

File:

- `scripts/python_basics_day0.py`

Focus:

- Run a Python file for the first time
- Change variables and rerun
- Understand what a function call like `if is_adult(age):` means

Command:

```powershell
python .\scripts\python_basics_day0.py
```

## Day 1

Practice:

- `print`
- variables
- strings
- numbers
- simple calculations

Output target:

- Print my name, age, current learning goal, and today's task

## Day 2

Practice:

- `if`
- `else`
- comparison operators

Output target:

- Check whether a score is pass or fail

## Day 3

Practice:

- list
- `for` loop

Output target:

- Print a daily task checklist line by line

## Day 4

Practice:

- function
- return value

Output target:

- Write a function that receives a website status code and returns `ok`, `warn`, or `fail`

## Day 5

Practice:

- command line argument with `sys.argv`

Output target:

- Run a script like this:

```powershell
python .\scripts\hello_cli.py lenxuan
```

Expected output:

```text
Hello, lenxuan
```

## Day 6-7

Practice:

- Review all scripts from Day 0 to Day 5
- Add notes to `learning_log.md`
- Connect basic syntax to the first real tools
- Make Git commits

## Real Tool Practice Added In Week 1

### `scripts/site_probe.py`

What this tool practices:

- Read a URL from the command line
- Open a website
- Read the HTTP status code
- Print `OK` or `WARN`
- Handle `HTTPError`

### `scripts/cert_days_left.py`

What this tool practices:

- Read a hostname from the command line
- Connect to port `443`
- Upgrade a socket into a TLS connection
- Read certificate expiry information
- Calculate remaining days
- Print a usable result

### `scripts/cert_days_left_rebuild.py`

Why this file exists:

- It is a rebuild practice file
- The purpose is not perfection
- The purpose is to prove I can reconstruct the core flow step by step

## What I Actually Learned In Week 1

- How to read `sys.argv[1]`
- How to use `return` to pass a result back
- How `if/else` chooses a branch
- How `for task in tasks:` works
- How to read and react to basic error messages
- How to use Git add, commit, and push in a real learning workflow

## What Still Needs Practice

- Handwriting code without looking back too often
- Remembering standard library function names
- Getting more comfortable with slightly longer scripts
- Looking at an error and identifying whether it is syntax, spelling, parameter, or logic related

## Week 1 Exit Standard

Week 1 counts as successful because:

- I finished the basic scripts
- I recorded the learning process in `learning_log.md`
- I built and rebuilt small real tools
- I committed and pushed the results to GitHub

## Suggested Next Step

Week 2 should continue the same style:

- small daily targets
- real runnable output
- core logic written by me first when possible
- AI used as coach, reviewer, and explainer, not as a full replacement
