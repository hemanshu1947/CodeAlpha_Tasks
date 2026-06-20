# Hangman Console Game

A Python console-based Hangman game with multiple word categories, ASCII hangman stages, scoring, attempts, and input validation.

## Features

- Multiple categories: Programming, Technology, Animals, Countries, and Space
- Random word selection
- ASCII hangman progress display
- Score tracking for correct guesses
- Validation for repeated or invalid guesses

## Tech Stack

- Python 3
- Standard Python libraries only

## Project Structure

```text
hangman-console-game/
├── hangman_console.py
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
└── assets/
    └── output-screenshot.png
```

## How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/hangman-console-game.git
cd hangman-console-game
```

2. Run the Python file:

```bash
python hangman_console.py
```

## Sample Output

```text
🎮 WELCOME TO HANGMAN 🎮

Choose a Category:

1. Programming
2. Technology
3. Animals
4. Countries
5. Space

Enter category number: 1

📂 Category: Programming
Word: _ _ _ _ _ _
Attempts Left: 6
```

## Screenshot

Add your output screenshot inside the `assets` folder and name it:

```text
output-screenshot.png
```

Then it will appear here:

![Output Screenshot](assets/output-screenshot.png)

## What I Learned

- Taking user input in Python
- Using conditional statements and loops
- Working with dictionaries/lists
- Displaying formatted console output

## Author

Created as a Python beginner project.
