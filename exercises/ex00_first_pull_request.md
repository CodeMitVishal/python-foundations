# Exercise 0 · Your first Pull Request

Goal: practise the real workflow every developer uses, from fork to branch, commit, push and Pull Request.

1. Run `python 00_setup_git/check_setup.py` and fix anything MISSING.
2. On GitHub, **Fork** [CodeMitVishal/python-foundations](https://github.com/CodeMitVishal/python-foundations).
3. Clone your fork and create a branch:
   ```bash
   git clone https://github.com/<your-github-name>/python-foundations.git
   ```
   ```bash
   cd python-foundations
   ```
   ```bash
   git switch -c hello-<your-github-name>
   ```
4. Create `submissions/<your-github-name>/hello.py` that prints your name and why you're learning Python:
   ```python
   print("Hi, I'm Vishal and I'm learning Python to build AI apps!")
   ```
5. Run it (`python submissions/<your-github-name>/hello.py`), then commit and push:
   ```bash
   git add submissions
   ```
   ```bash
   git commit -m "Add hello from <your-github-name>"
   ```
   ```bash
   git push -u origin hello-<your-github-name>
   ```
6. On GitHub, click **Compare & pull request**, write one sentence about yourself, and click **Create pull request**.

✅ Done when your Pull Request appears in the repo's **Pull requests** tab. Use the same steps for every exercise from now on.
