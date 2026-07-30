# 🎯 Number Guessing Game

A professionally structured command-line Number Guessing Game built with Python as part of my journey toward becoming a software developer and systems engineer.

This project focuses on applying fundamental Python concepts to build a complete, interactive application rather than simply writing isolated scripts. Throughout its development, the project evolved from a basic guessing game into a well-structured program featuring modular functions, input validation, game state management, replay functionality, and clean program architecture.

---

# 📌 Project Overview

The Number Guessing Game challenges the player to guess a randomly generated number within a limited number of attempts.

Rather than simply telling the player whether they are right or wrong, the application provides intelligent hints based on how close each guess is to the correct number.

The project was designed with software engineering principles in mind, emphasizing readability, maintainability, modularity, and separation of responsibilities.

---

# ✨ Features

* Random number generation between configurable limits
* Robust input validation
* Handles invalid text input without crashing
* Validates numeric range
* Intelligent proximity hints
* Tracks every guess made
* Limits the number of attempts
* Replay functionality
* Modular function-based architecture
* Easy-to-read and maintain codebase

---

# 🛠 Technologies Used

* Python 3
* Python Standard Library

  * `random`

No external libraries are required.

---

# 📂 Project Structure

```text
Number-Guessing-Game/
│
├── main.py
├── README.md
├── LICENSE
└── .gitignore
```

---

# 🎮 How the Game Works

1. The program generates a random number.
2. The player attempts to guess the number.
3. Every guess is validated before being accepted.
4. Invalid inputs do not crash the program.
5. The program provides hints after every incorrect guess.
6. Every valid guess is stored.
7. The player has a limited number of attempts.
8. The game ends when:

   * the correct number is guessed, or
   * the attempt limit is reached.
9. The player may choose to play another game.

---

# 🧠 Hint System

Instead of only saying "Too High" or "Too Low", the game evaluates how close the guess is.

Examples include:

* Very close
* Getting closer
* Too high
* Too low

This makes the gameplay more engaging while demonstrating conditional logic and decision making.

---

# ✅ Input Validation

The program safely handles several invalid situations.

### Invalid text

```text
abc
hello
@
```

### Numbers outside the valid range

```text
0
101
-25
```

The application continues asking until a valid number is entered.

---

# 🔁 Replay System

After each game the player is asked whether they would like to continue.

Supported responses include:

```text
yes
y
no
n
```

Whitespace and capitalization are ignored using:

```python
.strip().lower()
```

---

# 📊 Game State Management

During each game the application maintains several pieces of information:

* Secret number
* Player guesses
* Guess history
* Current attempt count
* Maximum attempts

Each new game starts with a completely fresh game state.

---

# 🏗 Software Design

One of the main objectives of this project was learning how to decompose a larger problem into smaller, reusable functions.

Each function performs one primary responsibility.

Examples include:

* Displaying the welcome message
* Generating the random number
* Collecting player input
* Validating guesses
* Providing hints
* Recording guess history
* Displaying the win message
* Checking attempt limits
* Handling replay logic

This modular design makes the application significantly easier to understand, debug, test, and extend.

---

# 💡 Python Concepts Practiced

This project provided practical experience with:

* Functions
* Parameters
* Return values
* Variables
* Constants
* Loops
* Nested logic
* Conditional statements
* Lists
* Exception handling
* User input
* Program flow
* State management
* Modular programming
* Separation of responsibilities

---

# 🧩 Challenges Solved

During development several software engineering problems were identified and corrected.

These included:

* Preventing invalid input from crashing the program
* Separating validation from user input
* Designing reusable functions
* Avoiding duplicated code
* Managing application state
* Correctly counting player attempts
* Recording complete guess history
* Ensuring a correct final guess is still considered a win
* Structuring the application using a clean game loop

Each challenge helped reinforce real-world debugging and problem-solving skills.

---

# 🚀 Possible Future Improvements

Future versions of the application may include:

* Multiple difficulty levels
* High score tracking
* Save scores to a file
* Statistics dashboard
* Hot and Cold hint system
* Timed game mode
* Multiplayer mode
* Colorized terminal interface
* Configurable game settings
* Sound effects
* Object-Oriented Programming (OOP) redesign
* Unit testing with `pytest`
* Configuration file support
* GUI version using Tkinter or PyQt
* Web version using Flask or FastAPI

---

# ▶️ Running the Project

Clone the repository:

```bash
git clone https://github.com/yourusername/number-guessing-game.git
```

Navigate into the project:

```bash
cd number-guessing-game
```

Run the program:

```bash
python main.py
```

---

# 📚 Learning Objectives

The purpose of this project was not only to build a game but also to develop stronger software engineering habits.

Particular emphasis was placed on:

* Writing readable code
* Designing reusable functions
* Understanding execution flow
* Breaking problems into manageable pieces
* Thinking about program architecture before implementation
* Debugging through logical reasoning rather than trial and error

---

# 📈 Skills Demonstrated

* Python Programming
* Software Design
* Problem Solving
* Modular Programming
* Defensive Programming
* Input Validation
* Control Flow
* State Management
* Command-Line Application Development
* Debugging
* Clean Code Principles

---

# 👨‍💻 About This Project

This project is part of my personal Python learning roadmap, where I am progressively building increasingly complex applications to strengthen my understanding of programming and software engineering.

Each project focuses on applying new concepts while reinforcing previous knowledge through practical implementation and iterative improvement.

---

# 📄 License

This project is intended for learning and portfolio use.

---

# ⭐ Acknowledgements


Though the skills are already there, this project was developed as part of my ongoing software engineering learning reinforcement journey, with an emphasis on understanding not just *how* to write code, but *why* certain design decisions lead to cleaner, more maintainable software.

Every iteration of the project focused on improving code quality, architecture, and problem-solving skills rather than simply adding new features.
