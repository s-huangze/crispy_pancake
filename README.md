# Number Guessing Game

This is a simple Python project where the computer randomly picks a number, and the player tries to guess it in the fewest attempts possible.

---

## Overview
The goal of this project is to practice using:
- Loops
- Conditional statements
- User input
- The `random` module in Python
- ---

## Learning Objectives
By completing this project, you’ll:
- Practice designing loops and conditionals
- Learn to handle user input safely
- Understand how random number generation works
- Improve problem-solving and debugging skills


When the player enters a guess, the program tells them whether the guess is too high, too low, or correct. It also counts how many tries it took to get the right answer.

---

## Features
- Easy to understand and run  
- Validates user input (no crashes if you type letters)  
- Tells you whether your guess is higher or lower  
- Lets you play again without restarting the program  
- Adjustable number range  

## Project Goals

This project was created to:
- Practice using Python loops and conditional statements  
- Learn to handle user input safely and avoid crashes  
- Build confidence with logic-based games  
- Explore simple debugging and testing  
- Create a fun way to learn coding basics   


## Tips for Players
- Start near the middle of the range to narrow your guesses quickly  
- Use the “Very Close” hints to adjust efficiently  
- Try Hard mode for more challenge  
- If you get stuck, use the quit command to see the answer
- Experiment with more advanced computer science strategies like binary search to get better results
---

## Requirements
- **Python 3.11 or newer**

Check your version:
```bash
python --version
```
or on some Windows systems:
```bash
py --version
```

---

## How to Run
1. Download or clone this repository.  
2. Open the folder in **Visual Studio Code** or any code editor.  
3. Run the program in the terminal:
   ```bash
   python guess.py
   ```
   or
   ```bash
   py guess.py
   ```
## How to Play
1. Run the game in your terminal or IDE.
2. The computer will pick a secret number between the given range.
3. Enter your guesses until you find the correct number.
4. The game will give you hints like “Too high!” or “Very close!”.
5. You can type `q` anytime to give up and see the correct answer.---

## Example Output
```
I'm thinking of a number between 1 and 100.
Your guess: 50
Too low!
Your guess: 75
Too high!
Your guess: 63
Correct! You got it in 3 tries.
```

---
## Code Structure
- `guess.py` – main game file  
- `play_once()` – runs a single round of the game  
- `read_int()` – safely reads user input  
- Constants like `LOW`, `HIGH`, and `MAX_TRIES` control game difficulty  
- Optional color helper `c()` adds colorful text output (if available)

## Common Mistakes
Here are a few things to watch out for:
- ❌ Typing letters instead of numbers will cause invalid input messages  
- ⚙️ Make sure your file name is `guess.py` before running  
- 💡 Always press **Enter** after typing a guess  
- 🧮 Remember: the secret number is always within your chosen range!

## How to Change the Range
In the file `guess.py`, you can edit these two variables:
```python
LOW, HIGH = 1, 100
```
Change them to any range you want (for example, 1–1000).

---

## Ideas for Improvement
- Add difficulty levels (Easy, Medium, Hard)
- Save and display a high score
- Show how close the guess is (e.g., "very close" or "way off")
- Limit the number of attempts
- Add sound or color feedback for fun
## Behind the Scenes
- The game uses Python’s built-in `random` module to generate the secret number.  
- A loop keeps asking for guesses until the player wins or runs out of attempts.  
- Conditional statements decide whether each guess is too high, too low, or correct.  
- Extra feedback like “Very close!” is based on how far the guess is from the secret number.
---
## Troubleshooting
If the game doesn’t run correctly:
- Make sure you have **Python 3.11 or newer** installed  
- Check that you are running the command in the correct folder:
  ```bash
  python guess.py

## Example Difficulty Levels
You can modify `MAX_TRIES` to make the game easier or harder:
- **Easy Mode:** `MAX_TRIES = 10`
- **Normal Mode:** `MAX_TRIES = 7`
- **Hard Mode:** `MAX_TRIES = 5`
 
Try adjusting the range too:
```python
LOW, HIGH = 1, 50   # Short range for quick games
LOW, HIGH = 1, 1000 # Long range for challenge
## How to Contribute
If you’d like to make this project better:
1. **Fork** this repository on GitHub  
2. **Clone** your fork:
   ```bash
   git clone https://github.com/<your-username>/number-guess-game.git
   ```
3. **Create a new branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. Make and test your changes  
5. **Commit** and **push** your updates:
   ```bash
   git commit -m "Added difficulty mode"
   git push origin feature/your-feature-name
   ```
6. Open a **Pull Request** describing what you changed

---

## Future Plans
- Add graphical interface using Tkinter
- Add leaderboard
- Port to web using Flask

## Author
Created by **Zelin Huang** for learning and practicing Python basics.

---

