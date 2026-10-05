# Assorted Tools

This is a library of very small tools created for my personal use. They only exist to solve minor inconveniences I have come across from time to time. This repository exists because if I needed these tools, somebody else probably does too.

As for what each function does, in the absence of full documentation, each function has a docstring explaining it.

# Installation

Requires Python 3.13 or newer.

The ansiText color and style codes require a compatible terminal. If you're using a modern device and operating system, this will likely not be an issue.

## Short Instructions

Install in a venv via pip using
```
python -m pip install https://github.com/Probably-Artemis/assorted-python-tools/archive/refs/heads/main.zip
```
<sup>Outside of a venv, Mac and Linux users may need to use `python3` instead.</sup>

## Long Instructions

(For those who have no clue what the above command does)

### Step 1

You must have Python installed, at least version 3.13 or newer. The installation process varies by operating system.

Download Python from [python.org](https://www.python.org/downloads/).

If you are on Mac, you may already have Python installed, but it is likely too old.

If you are on linux, Python is preinstalled but may not be up to date enough. On Debian and Ubuntu, you'll need to run `sudo apt install python3-venv`.

To check your version, run:
```
python3 --version
```
or on Windows:
```
py --version
```

### Step 2 (VSCode route)

Install VSCode and its Python extension. Open your project's folder in VSCode. **Not just a single .py file, the entire folder.**

Press `Ctrl+Shift+P` to open the Command Palette, type in and run `Python: Create Environment`, choose `Venv`, and select your installed Python instance.

New terminals in VSCode should open in the venv, indicated by `(.venv)` being shown in the prompt. Preexisting terminals won't be in the venv, so close and reopen them.

<sup>This route also works if you're using the CS50 IDE, as that is just a version of VSCode.</sup>

### Step 2 (the other option)

Open your project folder in a terminal. Consult the table below for the commands to run for your given operating system.

| | Windows | Mac / Linux |
|---|---|---|
|Create|`py -m venv .venv`|`python3 -m venv .venv`|
|Activate|`.venv\Scripts\activate`|`source .venv/bin/activate`|

To create your venv, use the Create command for your specific operating system.

Each time you open a terminal to run your code, you must activate your venv, using the Activate command for your specific operating system.

#### A note for Windows users:

Sometimes, activating your venv may fail, as PowerShell will tell you "running scripts is disabled on this system". To fix this, run the following command to enable running scripts.
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 3

With your venv activated, run the installation command.
```
python -m pip install https://github.com/Probably-Artemis/assorted-python-tools/archive/refs/heads/main.zip
```
To update which version you have installed, simply append `--upgrade` to the end of the installation command.

If you use git, add `.venv/` to your .gitignore file.

### Step 4

At this point, you should be all set. Simply import the tools you want, and use them. For example:
```python
from assorted_tools.misc import clear, newsection
```
You may use a wildcard import to import everything a specific module provides, but this is not advised.

# Using these tools

## ansiText

Provides classes `style` and `color`, and function `reset`.

Eases formatting text output by providing more memorable names for ANSI codes.

Example:
```python
from assorted_tools.ansiText import style, color

print(f"{color.BLUE}This text will be blue.{style.RESET}")
```

## centerprint

Provides function `centerprint`.

Prints (or returns) a provided string centered in the terminal, word wrapped and balanced across multiple lines.

Example:
```python
from assorted_tools.centerprint import centerprint

centerprint("Unit 1, assignment 1")

print("Hello world!")
```

## debug

Provides functions `set_debug` and `deprint`.

The deprint function is identical to the built-in print function, but conditional. By default, deprint will do nothing. When set_debug is used to activate it, deprint will behave exactly like the built-in print function.

Example:
```python
from assorted_tools.debug import set_debug, deprint

set_debug(True)

deprint("This will print.")

set_debug(False)

deprint("And this will not.")
```

## input

Provides function `input`. Replaces built-in function `input`.

Behaves like the built-in input, but with some slight added features. By default, the text being typed by the user will display with an underline. A default response may be provided, which will appear faintly *after* the user's cursor. The default response will be returned if the user types nothing.

Example:
```python
from assorted_tools.input import input

name = input("Name: ", default="Anonymous")
```

## misc

Provides functions `clear`, `newsection`, and `slowprint`.

The clear function clears the terminal.

The newsection function is used to organize terminal output into sections for easier reading.

The slowprint function takes a string and prints it out character by character.

<sup>The slowprint function was more of a simple refresher exercise than something I have ever actually needed to use.</sup>

## randomword

Provides functions `randomword` and `randomwords`.

The randomword function returns a randomly selected English word. Randomness uses `secrets`, and is thus viable for use in a password generator.

The randomword**s** function returns a random number of random words. The function takes two integers, which set the range of how many words get returned inclusive. By default it returns a string; set `string=False` to get a list instead.

Example:
```python
from assorted_tools.randomword import randomword

print(randomword())
```

## sanitize

Provides function `sanitize`, and one function for each of its modes.

The sanitize function cleans a string using one or more modes, applied in the order given. A mode is either a name from the table below or your own function that takes a string and returns a string. An unknown mode name raises a `ValueError`. With no mode, `alphanumeric` is used.

| Mode | Function | Use case |
| --- | --- | --- |
| `alphanumeric` | `keep_alphanumeric` | Removes everything except letters and digits. |
| `ansi` | `strip_ansi` | Removes ANSI escape sequences, such as colors and window titles. |
| `ascii` | `to_ascii` | Strips accents and drops anything with no ASCII form. |
| `control` | `strip_control` | Removes control characters, keeping tab and newline. |
| `filename` | `safe_filename` | Makes a name safe for a single file or folder on any system. |
| `invisible` | `strip_invisible` | Removes zero width characters and text direction overrides. |
| `slug` | `slugify` | Makes a lowercase identifier of letters, digits, and hyphens. |
| `terminal` | `terminal_safe` | Runs `ansi`, `control`, and `invisible`, in that order. |
| `whitespace` | `collapse_whitespace` | Collapses runs of whitespace to one space and trims the ends. |

Order matters when combining modes. Use `ansi` before `control`, or use `terminal` for both.

These modes clean text for display, storage, and naming. They do not make text safe to put inside HTML, SQL, or a shell command.

Example:
```python
from assorted_tools.sanitize import sanitize

print(sanitize(untrusted_text, "terminal"))

title = sanitize("  My   Report: Final?  ", "whitespace", "filename")
```

# Contributing
If something is broken or badly written, open an issue! If you know how to fix it yourself, fork the repo, fix it, and open a pull request! If you have tools of your own you'd like to add, open a pull request!