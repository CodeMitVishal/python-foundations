# Module 0 · Lesson 1: The terminal and VS Code

Programmers type commands into a **terminal** (a text window that runs commands) and
write code in an **editor**. You only need a handful of commands to start.

## Open a terminal

| System | How |
|---|---|
| Windows | Press `Win`, type **PowerShell**, press Enter. Or, in VS Code: **Terminal → New Terminal** |
| macOS | Press `Cmd + Space`, type **Terminal** |
| Linux | `Ctrl + Alt + T` |

## The 10 commands you'll use every day

| Command (Windows PowerShell) | macOS / Linux | What it does |
|---|---|---|
| `pwd` | `pwd` | **Where am I?** (print working directory) |
| `ls` | `ls` | **What's in this folder?** |
| `cd projects` | `cd projects` | **Go into** the folder `projects` |
| `cd ..` | `cd ..` | Go **up** one folder |
| `mkdir python-course` | `mkdir python-course` | **Make** a new folder |
| `code .` | `code .` | Open **this folder** in VS Code |
| `python --version` | `python3 --version` | Check that Python works |
| `python hello.py` | `python3 hello.py` | **Run** a Python file |
| `cls` | `clear` | Clear the screen |
| `↑` arrow key | `↑` arrow key | Repeat a previous command |

Tips:
- Press **Tab** to auto-complete file and folder names: type `cd pyt` then Tab.
- Paths with spaces need quotes: `cd "My Projects"`.
- **Ctrl + C** stops a running program (for example an endless loop).

## VS Code setup (once)

1. Install **VS Code** from [code.visualstudio.com](https://code.visualstudio.com).
2. Open the **Extensions** panel (`Ctrl + Shift + X`) and install **Python** (by Microsoft).
3. Open your course folder: **File → Open Folder…** (or `code .` in the terminal).
4. Pick the interpreter: `Ctrl + Shift + P` → **Python: Select Interpreter** → choose the one with `.venv` if you have one.
5. Run a file with the ▶ button (top right), or in the terminal with `python file.py`.

Useful shortcuts:

| Shortcut | Does |
|---|---|
| `Ctrl + S` | save |
| `Ctrl + /` | comment / uncomment the line |
| `Ctrl + Shift + P` | the command palette: search any action |
| `F5` | run with the **debugger** (Module 7, lesson 6) |
| `Ctrl + `` ` `` | show / hide the terminal |

## Check everything at once

```bash
python 00_setup_git/check_setup.py
```

It tells you what's installed and what's still missing.
