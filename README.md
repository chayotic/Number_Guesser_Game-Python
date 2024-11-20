# Number Guessing Game 🎲  
A fun and interactive Python game where the user tries to guess a randomly generated number between 0 and 100. Includes features for tracking average tries, error handling, and a developer mode with special commands.  

---

## Features 🚀  
- **Random Number Generation**: Guess a number between 0 and 100.  
- **Error Handling**: Handles invalid inputs gracefully.  
- **Average Tries Calculation**: Keeps track of average attempts per game.  
- **Developer Mode**: Access debug information and additional commands.  

---

## Developer Options ⚙️  
Developer mode unlocks additional commands:  
- `/updlogs` - Display update logs.  
- `/number` - Reveal the random number for debugging.  
- `/dev` - Enable developer mode.  

To activate developer mode, enter `/dev` during gameplay.  

---

## How to Play 🎮  
1. Run the Python script.  
2. Guess a number between 0 and 100.  
3. Follow hints like **"Try Going Higher"** or **"Try Going Lower"** to reach the correct answer.  
4. Once guessed correctly, you’ll see: **"PERFECT"** 🎉.  

You can choose to start a new game or exit after completing one.  

---

## Requirements 🛠  
- Python 3.x  
- [Termcolor Library](https://pypi.org/project/termcolor/)  
  Install using pip:  
  ```bash
  pip install termcolor

  ---

### Update Log 📖

v0.1: Initial Release.

v0.2: Added range check for user input (0-100).

v0.3: Improved input validation for strings and out-of-range values.

v0.4: Implemented validation to check for 'yes' or 'no' responses with error handling.

v0.5: Added feature to calculate and display the average number of tries across multiple games.

v0.6: Bug Fix.

v0.7: Developer Options Added.

---

### License 📄

This project is licensed under the MIT License.


---
