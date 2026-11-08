"""Module 0 · Check your setup

Checks that Python, pip, Git and VS Code are ready, and that Git knows your name.
Fix anything marked MISSING, then run it again.

Run it:  python 00_setup_git/check_setup.py
"""
import shutil
import subprocess
import sys


def run(cmd):
    """Run a command and return its output, or None if it fails."""
    try:
        out = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        return out.stdout.strip() if out.returncode == 0 else None
    except (OSError, subprocess.TimeoutExpired):
        return None


checks = []

version = sys.version_info
checks.append(("Python 3.10 or newer", version >= (3, 10), f"you have {version.major}.{version.minor}"))
checks.append(("pip works", run([sys.executable, "-m", "pip", "--version"]) is not None,
               "reinstall Python and tick 'pip'"))

git = shutil.which("git")
checks.append(("Git installed", git is not None, "install from https://git-scm.com"))
if git:
    name = run(["git", "config", "--global", "user.name"])
    email = run(["git", "config", "--global", "user.email"])
    checks.append(("Git user.name set", bool(name), 'git config --global user.name "Your Name"'))
    checks.append(("Git user.email set", bool(email), 'git config --global user.email "you@example.com"'))

checks.append(("VS Code 'code' command", shutil.which("code") is not None,
               "optional: in VS Code run 'Shell Command: Install code command in PATH'"))
in_venv = sys.prefix != sys.base_prefix
checks.append(("running inside a virtual environment", in_venv,
               "optional for now: python -m venv .venv (Module 4)"))

print(f"Python: {sys.executable}\n")
for label, ok, hint in checks:
    status = "OK     " if ok else ("OPTIONAL" if hint.startswith("optional") else "MISSING")
    print(f"  [{status:<8}] {label}" + ("" if ok else f"  ->  {hint}"))

required = checks[:3]
if all(ok for _, ok, _ in required):
    print("\nYou're ready to start Module 1!")
else:
    print("\nFix the MISSING items above, then run this again.")
