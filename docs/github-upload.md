# GitHub Upload Workflow

Use this whenever I finish a small learning checkpoint and want to upload it to GitHub.

## Before Upload

Check what changed:

```powershell
git status --short
git diff -- README.md docs learning_log.md scripts
```

Run the current practice script:

```powershell
python .\scripts\python_basics_day0.py
```

## Commit

Stage files:

```powershell
git add README.md docs learning_log.md scripts .gitignore .gitmodules
```

Commit:

```powershell
git commit -m "Update learning plan"
```

## Upload

Push to GitHub:

```powershell
git push
```

If the branch has not been connected yet:

```powershell
git push -u origin main
```

## How To Ask Codex

Useful prompt:

```text
按 GitHub 上传流程检查、提交并推送当前学习计划仓库。
```

Codex should:

- Check `git status`.
- Explain what will be committed.
- Run the simple local validation.
- Commit with a clear message.
- Push to GitHub.

## Installed GitHub Skills

The following GitHub-related Codex skills are already installed locally:

- `gh-address-comments`: helps address GitHub PR review or issue comments.
- `gh-fix-ci`: helps inspect and fix failing GitHub Actions checks.

They are useful later when this learning repo grows into project repos with PRs and CI.

Note:

- Normal upload only needs `git push`.
- The `gh` command line tool is not required for simple upload.
- Install GitHub CLI later when I start using pull requests, review comments, and GitHub Actions seriously.
