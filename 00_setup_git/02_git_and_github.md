# Module 0 · Lesson 2: Git and GitHub

**Git** saves snapshots ("commits") of your project, so you can see what changed,
undo mistakes and work with other people. **GitHub** hosts Git projects online.
Every professional developer uses both every day.

```
 your folder ──git add──► staging area ──git commit──► local history ──git push──► GitHub
     ▲                                                                                │
     └──────────────────────────────────── git pull ◄─────────────────────────────────┘
```

## One-time setup

Install Git from [git-scm.com](https://git-scm.com), then tell it who you are:

```bash
git config --global user.name "Your Name"
```

```bash
git config --global user.email "you@example.com"
```

## The everyday loop

| Step | Command | Meaning |
|---|---|---|
| 1 | `git status` | What changed? (run this all the time) |
| 2 | `git add hello.py` (or `git add .`) | Put changes into the next snapshot |
| 3 | `git commit -m "Add greeting"` | Save the snapshot with a message |
| 4 | `git push` | Upload your commits to GitHub |
| 5 | `git pull` | Download other people's commits |
| – | `git log --oneline` | Show the history |
| – | `git diff` | Show exactly what changed |

Good commit messages say **what** and **why** in a few words: `Fix tax rounding for 0 EUR orders`, not `update`.

## Branches: work without breaking `main`

```bash
git switch -c my-feature
```

…edit, add and commit as usual…

```bash
git push -u origin my-feature
```

Then open a **Pull Request (PR)** on GitHub: "please review my changes and merge them into `main`".

## Contributing to this course (fork → branch → PR)

1. On GitHub, click **Fork** on `CodeMitVishal/python-foundations` (your own copy).
2. Clone YOUR fork: `git clone https://github.com/<you>/python-foundations.git`
3. `cd python-foundations`, then `git switch -c ex03-grade-book`
4. Add your solution in `submissions/<your-github-name>/`
5. `git add .`, `git commit -m "Add grade book solution"`, `git push -u origin ex03-grade-book`
6. On GitHub, click **Compare & pull request** → describe what you did → **Create pull request**.
7. I review it, you push fixes to the same branch (the PR updates by itself), and then it gets merged. 🎉

## Merge conflicts (don't panic)

When two people change the same lines, Git can't decide and marks the file:

```
<<<<<<< HEAD
print("Hello")
=======
print("Hi there")
>>>>>>> my-feature
```

Edit the file to the version you want, **delete the three marker lines**, then
`git add <file>` and `git commit`. VS Code shows **Accept Current / Incoming / Both** buttons to help.

## Never commit

- passwords, API keys, `.env` files → list them in `.gitignore`
- `.venv/` and `__pycache__/` folders
- huge data files

If a secret slips into a commit, **change the secret**. Deleting the file later doesn't remove it from the history.
