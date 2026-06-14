# Week 1 Review

Date: 2026-06-15

## Completed

- Day 0: ran a Python file, changed a list, and observed output changes.
- Day 1: used variables, strings, numbers, and simple calculations.
- Day 2: used `if`, `else`, and comparison expressions.
- Day 3: used lists and `for` loops to print a checklist.
- Day 4: wrote a function that returns `ok`, `warn`, or `fail`.
- Day 5: used `sys.argv` to read a command line argument.

## What I Can Explain Now

- `print(...)` sends text to the terminal.
- A variable stores a value for later use.
- `if` runs code only when a condition is true.
- A list stores multiple values.
- A `for` loop takes values from a list one by one.
- A function groups logic under a name.
- `return` sends a function result back to the caller.
- `sys.argv[1]` is the first useful command line argument after the script name.

## Important Mistakes

- In Day 3, `"add a new task"` and `"add one new task"` did not match because strings must be exactly the same.
- In Day 5, `len(sys.argv)` is not 0 when no extra argument is given, because the script name is always included.

## Next Step

Start `scripts/site_probe.py`.

This is the first real tool in the roadmap. It connects the Week 1 basics:

- `sys.argv`: receive the URL from the command line.
- function: implement `probe_url(url)`.
- `return`: return the HTTP status code.
- `if`: decide whether the site is OK or warning.

Do not start `cert_days_left.py` yet. Certificate checking uses SSL and dates, so it should wait until `site_probe.py` is understood.

