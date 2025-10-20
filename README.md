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

---

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

---

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

