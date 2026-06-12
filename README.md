# lenxuan learning plan

This repository tracks my 2026-2027 programming growth plan.

Main goal: by June 2027, I can independently build, deploy, and deliver small software projects, and complete at least one real paid or semi-real commissioned task.

## Current Focus

Current stage: Week 1, Python basics and Git habits.

I am starting from nearly zero Python, so the first checkpoint is simple:

- Run a Python file from PowerShell.
- Change variables and see output change.
- Understand `print`, variables, `if/else`, lists, loops, and simple functions.
- Commit the first small learning change to Git.

## Repository Map

- `docs/roadmap-2026-2027.md`: the high-level execution roadmap.
- `docs/week-01-python-basics.md`: the current beginner-friendly Week 1 plan.
- `docs/ai-rules.md`: how I should use AI while learning.
- `learning_log.md`: daily learning record.
- `scripts/python_basics_day0.py`: today's Python Day 0 practice.
- `scripts/site_probe.py`: future Week 1 HTTP check exercise.
- `scripts/cert_days_left.py`: future Week 1 certificate check exercise.

## Run Today

```powershell
python .\scripts\python_basics_day0.py
```

Then change `name`, `age`, and the `tasks` list in that file, and run it again.

## Learning Rules

- You write the core logic first.
- Commit small changes to Git.
- Keep notes about what ran, what failed, and what you fixed.
- Do not expand into Rust, Web3, RAG, Raft, or other side quests during the 2026 summer plan.

## First Real Project Target

Project name: `lenxuan-monitor`

Target: a deployable server monitoring and TLS certificate expiry dashboard built with Python, FastAPI, SQLite, Linux, Nginx, HTTPS, and later Docker.
