# Python Foundations

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/downloads/)
[![YouTube: CodeMitVishal](https://img.shields.io/badge/YouTube-CodeMitVishal-FF0000?logo=youtube&logoColor=white)](https://www.youtube.com/@CodeMitVishal)
[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-support%20us-FFDD00?logo=buymeacoffee&logoColor=black)](https://buymeacoffee.com/codemitvishal)

**Learn Python from zero, one runnable example at a time.**

This repo holds everything from the *Python Foundations* live session on
[CodeMitVishal](https://www.youtube.com/@CodeMitVishal) YouTube channel:

- **30 runnable demos**, one for every example in the session
- **7 hands-on exercises**, each with a starter file and a worked solution
- **The full slide deck** as a PDF: [`slides/python-foundations-slides.pdf`](slides/python-foundations-slides.pdf)

## Contents

- [Who this is for](#who-this-is-for)
- [Quick start](#quick-start)
- [How to follow along](#how-to-follow-along)
- [Course map](#course-map)
- [Exercises](#exercises)
- [Weather API setup (Module 4)](#weather-api-setup-module-4)
- [Troubleshooting](#troubleshooting)
- [About the host](#about-the-host)
- [Support the channel](#support-the-channel)

## Who this is for

- Complete beginners who have never written a line of code
- Developers from another language who want a quick tour of Python
- Anyone who watched the session and wants the code to practise with

By the end you can store and convert data, make decisions, loop over lists, model data
with dictionaries and JSON, call a web API, write your own functions and classes, and
read, write and organise files safely.

## Quick start

**1. Install Python 3.10 or newer** from [python.org](https://www.python.org/downloads/).
On Windows, tick **"Add python.exe to PATH"** in the installer. Then check it:

```bash
python --version
```

**2. Get the code.** With Git:

```bash
git clone https://github.com/CodeMitVishal/python-foundations.git
```

```bash
cd python-foundations
```

No Git? Click the green **Code** button on this page, choose **Download ZIP** and unzip it.

**3. Run your first program:**

```bash
python hello.py
```

You should see `hello world`. Now try a real demo:

```bash
python 01_data_types_io/02_tax_calculator.py
```

> On macOS and Linux, type `python3` wherever this guide says `python`.

## How to follow along

Folders are numbered by module, and the files inside each folder are numbered in the
order they come up in the session, so you can work through them top to bottom.

1. **Watch** a module in the video, with the [slides](slides/python-foundations-slides.pdf) open.
2. **Run** that module's demos in order, then change the numbers and text to see what happens.
3. **Practise** with the module's exercise in [`exercises/`](exercises/).
4. **Compare** your answer with the matching file in [`solutions/`](solutions/).

## Course map

| # | Module | Code | You build | Exercise |
|---|---|---|---|---|
| 0 | Setup: terminal, VS Code, Git & GitHub | [`00_setup_git`](00_setup_git/) | Your setup check | Your first Pull Request |
| 1 | Data Types and Input and Output | [`01_data_types_io`](01_data_types_io/) | Tax calculator, age calculator | Tip calculator |
| 2 | Conditionals and Imports | [`02_conditionals_imports`](02_conditionals_imports/) | Rock, paper, scissors | Guess the number |
| 3 | Lists and Loops | [`03_lists_loops`](03_lists_loops/) | Expense totals, loan calculator | Grade book |
| 4 | Dictionaries, JSON, and Pip | [`04_dicts_json_pip`](04_dicts_json_pip/) | Movie schedule, contacts, weather app | Word counter |
| 5 | Functions | [`05_functions`](05_functions/) | Dice rolling game | Temperature converter |
| 6 | Classes and Objects | [`06_classes`](06_classes/) | Company payroll | Bank accounts |
| 7 | Working with Files and Exceptions | [`07_files_exceptions`](07_files_exceptions/) | File organizer | Notes app |

<details>
<summary><b>Every lesson and the file that goes with it</b></summary>

**Module 0 · Setup: terminal, VS Code, Git & GitHub**

| Lesson | File |
|---|---|
| The terminal and VS Code | [`01_terminal_and_vscode.md`](00_setup_git/01_terminal_and_vscode.md) |
| Git and GitHub | [`02_git_and_github.md`](00_setup_git/02_git_and_github.md) |
| Check your setup | [`check_setup.py`](00_setup_git/check_setup.py) |

**Module 1 · Data Types and Input and Output**

| Lesson | File |
|---|---|
| Introducing data types | [`01_data_types.py`](01_data_types_io/01_data_types.py) |
| Demo: install Python | [`hello.py`](hello.py) |
| Demo: tax calculator | [`02_tax_calculator.py`](01_data_types_io/02_tax_calculator.py) |
| Strings and input and output | [`03_strings_input_output.py`](01_data_types_io/03_strings_input_output.py) |
| Demo: age calculator | [`04_age_calculator.py`](01_data_types_io/04_age_calculator.py) |

**Module 2 · Conditionals and Imports**

| Lesson | File |
|---|---|
| Conditionals | [`01_conditionals.py`](02_conditionals_imports/01_conditionals.py) |
| Conditional operators and booleans | [`02_operators_booleans.py`](02_conditionals_imports/02_operators_booleans.py) |
| Demo: rock, paper, scissors | [`03_rock_paper_scissors.py`](02_conditionals_imports/03_rock_paper_scissors.py) |
| Importing modules | [`04_imports_demo.py`](02_conditionals_imports/04_imports_demo.py) |
| Demo: randomize the game | [`05_rock_paper_scissors_random.py`](02_conditionals_imports/05_rock_paper_scissors_random.py) |

**Module 3 · Lists and Loops**

| Lesson | File |
|---|---|
| Lists and loops | [`01_lists_loops.py`](03_lists_loops/01_lists_loops.py) |
| Demo: sum expenses | [`02_sum_expenses.py`](03_lists_loops/02_sum_expenses.py) |
| Loops with `range()` | [`03_range_loops.py`](03_lists_loops/03_range_loops.py) |
| Demo: loan payment calculator | [`04_loan_calculator.py`](03_lists_loops/04_loan_calculator.py) |
| Bonus: `while`, `break`, `continue` | [`05_while_break_continue.py`](03_lists_loops/05_while_break_continue.py) |
| Bonus: slicing, tuples, sets | [`06_slicing_tuples_sets.py`](03_lists_loops/06_slicing_tuples_sets.py) |

**Module 4 · Dictionaries, JSON, and Pip**

| Lesson | File |
|---|---|
| Dictionaries | [`01_dictionaries.py`](04_dicts_json_pip/01_dictionaries.py) |
| Demo: movie schedule | [`02_movie_schedule.py`](04_dicts_json_pip/02_movie_schedule.py) |
| Combining lists and dictionaries | [`03_lists_and_dicts.py`](04_dicts_json_pip/03_lists_and_dicts.py) |
| Demo: nested contacts | [`04_nested_contacts.py`](04_dicts_json_pip/04_nested_contacts.py) |
| Reading JSON | [`05_json_basics.py`](04_dicts_json_pip/05_json_basics.py) |
| Demo: virtual environment and pip | [Weather API setup](#weather-api-setup-module-4) |
| Demo: OpenWeatherMap API | [`06_weather_api.py`](04_dicts_json_pip/06_weather_api.py) |

**Module 5 · Functions**

| Lesson | File |
|---|---|
| Functions | [`01_functions.py`](05_functions/01_functions.py) |
| Demo: dice rolling game | [`02_dice_game.py`](05_functions/02_dice_game.py) |

**Module 6 · Classes and Objects**

| Lesson | File |
|---|---|
| Classes | [`01_employee.py`](06_classes/01_employee.py) |
| Demo: company payroll | [`02_payroll.py`](06_classes/02_payroll.py) |
| Class inheritance | [`03_inheritance.py`](06_classes/03_inheritance.py) |
| Demo: payroll with inheritance | [`04_payroll_inheritance.py`](06_classes/04_payroll_inheritance.py) |

**Module 7 · Working with Files and Exceptions**

| Lesson | File |
|---|---|
| Exceptions | [`01_exceptions.py`](07_files_exceptions/01_exceptions.py) |
| Reading files | [`02_reading_files.py`](07_files_exceptions/02_reading_files.py) |
| Demo: writing files | [`03_writing_files.py`](07_files_exceptions/03_writing_files.py) |
| File manipulation | [`04_file_manipulation.py`](07_files_exceptions/04_file_manipulation.py) |
| Demo: file organizer | [`05_file_organizer.py`](07_files_exceptions/05_file_organizer.py) |
| Bonus: debugging | [`06_debugging.py`](07_files_exceptions/06_debugging.py) |

</details>

## Exercises

Each exercise file starts with the task, a sample run and hints, followed by `TODO`
comments where your code goes. Try it yourself first, then check the solution.

| # | Exercise | You practise | Start here | Solution |
|---|---|---|---|---|
| 1 | Tip calculator | `input()`, type conversion, f-strings | [starter](exercises/ex01_tip_calculator.py) | [solution](solutions/ex01_tip_calculator.py) |
| 2 | Guess the number | `random`, `if` / `elif` / `else` | [starter](exercises/ex02_guess_the_number.py) | [solution](solutions/ex02_guess_the_number.py) |
| 3 | Grade book | lists, `range()`, loops | [starter](exercises/ex03_grade_book.py) | [solution](solutions/ex03_grade_book.py) |
| 4 | Word counter | dictionaries, JSON | [starter](exercises/ex04_word_counter.py) | [solution](solutions/ex04_word_counter.py) |
| 5 | Temperature converter | functions, `return`, default values | [starter](exercises/ex05_temperature_converter.py) | [solution](solutions/ex05_temperature_converter.py) |
| 6 | Bank accounts | classes, inheritance, `super()` | [starter](exercises/ex06_bank_account.py) | [solution](solutions/ex06_bank_account.py) |
| 7 | Notes app | files, `try` / `except` | [starter](exercises/ex07_notes_app.py) | [solution](solutions/ex07_notes_app.py) |

## Weather API setup (Module 4)

Every demo runs with plain Python except
[`06_weather_api.py`](04_dicts_json_pip/06_weather_api.py), which needs the `requests`
package and a free API key.

**1. Create a virtual environment**, so packages stay inside this project:

```bash
python -m venv .venv
```

**2. Activate it.** Windows (PowerShell or Command Prompt):

```bash
.venv\Scripts\activate
```

macOS or Linux:

```bash
source .venv/bin/activate
```

Your prompt now starts with `(.venv)`.

**3. Install the packages:**

```bash
pip install -r requirements.txt
```

**4. Add your API key.** Create a free account at
[openweathermap.org](https://openweathermap.org) and copy your key. Set it in the same
terminal window: use `$env:OPENWEATHER_API_KEY = "your-key"` in PowerShell,
`set OPENWEATHER_API_KEY=your-key` in Command Prompt, or
`export OPENWEATHER_API_KEY=your-key` on macOS and Linux.

**5. Run it:**

```bash
python 04_dicts_json_pip/06_weather_api.py
```

> Keep your key out of the code and out of Git. The demo reads it from the environment
> for exactly that reason.

## Troubleshooting

| Problem | Fix |
|---|---|
| `python` is not recognized | Reinstall Python with **"Add python.exe to PATH"** ticked, or use `py` on Windows and `python3` on macOS/Linux. |
| `ModuleNotFoundError: No module named 'requests'` | Activate the virtual environment, then run `pip install -r requirements.txt`. |
| PowerShell won't run `.venv\Scripts\activate` | Open Command Prompt instead and run `.venv\Scripts\activate.bat`. |
| `ValueError: invalid literal for int()` | The program expected a whole number. Type digits only; Module 7 shows how to catch this error. |
| Weather demo returns error 401 | The API key is wrong or still new. Fresh OpenWeatherMap keys can take a couple of hours to start working. |
| A file demo created extra files | That's expected. The demos in `07_files_exceptions` only touch files they create (`list.txt`, `playground/`, `messy_folder/`). Delete them any time. |

Still stuck? [Open an issue](https://github.com/CodeMitVishal/python-foundations/issues)
with the command you ran and the full error message.

## About the host

**Vishal Singh**, Cloud Engineer. 7+ years building cloud platforms on Azure and
Kubernetes, and bringing agentic AI into real products.

Certifications: Azure Solutions Architect Expert · Agentic AI Business Solutions
Architect · Azure AI Apps and Agents Developer Associate · Azure AI Engineer Associate ·
Azure Developer Associate · AI Transformation Leader · Certified ScrumMaster.

## Support the channel

If this session helped you:

- **Subscribe** to [CodeMitVishal](https://www.youtube.com/@CodeMitVishal) on YouTube
- **Star** this repo so others can find it
- **Buy me a coffee** at [buymeacoffee.com/codemitvishal](https://buymeacoffee.com/codemitvishal) ☕
