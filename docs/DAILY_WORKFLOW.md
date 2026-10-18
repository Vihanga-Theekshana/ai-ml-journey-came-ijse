# Daily update workflow

1. Create the next folder, such as `days/day-19/`. Keep day numbers in order; do not invent past calendar dates.
2. Add a notebook with a descriptive filename and a README using [the day template](../templates/DAY_README.md).
3. Write what you learned, what you personally changed, one difficulty, and what you will try next. Explain results in your own words.
4. Keep datasets and model files local. Record data sources and setup instructions in `docs/DATASETS.md`.
5. Run the relevant cells yourself, fix unexpected errors, and clear bulky/private outputs. Record any remaining limitations.
6. Add the new day to the main README table.
7. Review and commit the actual work:

```powershell
git status --short
git add days/day-19 README.md docs/DATASETS.md
git diff --cached --stat
git diff --cached
git commit -m "docs: add day 19 learning notes and exercises"
git push
```

Use the real topic in your commit message. One honest import commit is appropriate for older course work; do not backdate commits to simulate daily activity. Commit future updates when you actually complete them.

Before publishing, inspect staged filenames and content. `.gitignore` ignores file patterns, not arbitrary file sizes, and does not untrack files already committed.
