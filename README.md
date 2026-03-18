# ChatGPT Introduction & Debugging

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat&logo=html5&logoColor=white)
![Holberton School](https://img.shields.io/badge/Holberton-School-red)

## Description

This repository is an introduction to using **ChatGPT** (and other AI tools) to aid in the software development process, specifically focusing on **debugging** and code correction. The project challenges involve taking pre-written scripts that contain bugs, logic errors, or missing features, and working with AI to fix and improve them.

---

## File Directory: Debugging Scripts

The `debugging` directory contains several small programs that act as technical exercises for debugging skills. 

| File | Type | Description |
| --- | --- | --- |
| `change_background.html` | HTML/JS | A simple web page designed to change the background color dynamically. |
| `checkbook.py` | Python | A personal checkbook simulator. It allows the user to interactively deposit money, withdraw money, and check their current balance using a `Checkbook` class. |
| `factorial.py` | Python | A script that calculates and prints the factorial of a given number using iterative loops. |
| `factorial_recursive.py` | Python | A script that calculates the factorial of a given number, implemented using a recurring functional approach. |
| `mines.py` | Python | A terminal-based Minesweeper game. Players input coordinates to reveal safe squares and must avoid hitting the mines. |
| `print_arguments.py` | Python | A small utility script designed to iterate through and print the command-line arguments provided to it. |
| `tic.py` | Python | A fully functional, terminal-based Tic-Tac-Toe game playable by two users (`X` and `O`). |

---

## Usage Instructions

To run any of the Python scripts, navigate to the `debugging` directory and execute them using `python3` (or `python`, depending on your environment config).

### Example: Playing Tic-Tac-Toe
```bash
cd debugging
./tic.py
```
*(If the file is not executable, run: `python3 tic.py`)*

### Example: Using the Checkbook
```bash
cd debugging
./checkbook.py
# Follow the interactive prompts to deposit or withdraw funds.
```

### Example: Viewing the HTML Page
Simply open `change_background.html` in any modern web browser to view the interface.
```bash
# On Windows, you can typically use:
start change_background.html

# On macOS:
open change_background.html

# On Linux:
xdg-open change_background.html
```

---

## Author

- **CERQUEIRA Loïc** - *Student at Holberton School*
