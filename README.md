---

# Number Guessing Game

## Overview

This is a simple command-line-based number guessing game implemented in Python. The program generates a random number between 1 and 100, and the user has to guess the correct number. After each guess, the program will guide the user by telling them if their guess is too high, too low, or correct. The game continues until the user guesses the correct number.

## How to Run

1. Make sure you have Python installed on your machine.
2. Copy the Python code from `number_guessing_game.py` (or whichever name you choose for the file).
3. Open a terminal or command prompt and navigate to the folder where the script is saved.
4. Run the script using the following command:

    ```
    python number_guessing_game.py
    ```

5. The program will prompt you to guess a number between 1 and 100.
6. Keep guessing until you find the correct number. The game will provide hints about whether your guess is too high or too low.
7. Once the correct number is guessed, the game will print "Congratulations!" and the game will end.

## Features

- Generates a random number between 1 and 100.
- Guides the player with feedback on whether their guess is too high or too low.
- Input validation to ensure the player enters a valid number between 1 and 100.
- Handles invalid inputs (e.g., non-numeric entries) without crashing the game.

## Example Run

```
Enter a number between 1 to 100 to guess the target: 50
Oh no! Your choice is smaller than the target. Try again!

Enter a number between 1 to 100 to guess the target: 75
Oh no! Your choice is greater than the target. Try again!

Enter a number between 1 to 100 to guess the target: 63
Congratulations! Your choice matches the target.
63
-----GAME OVER!!!-----

```

## Requirements

- Python 3.x

## Notes

- The program includes input validation to ensure the user enters a valid integer between 1 and 100. If an invalid input is entered (such as a string or a number outside the range), the game will prompt the user to try again.
- The game will loop until the correct number is guessed.

Contact Information
For any questions, issues, or suggestions, feel free to contact me on LinkedIn:

Abhinav Raj's LinkedIn Profile :- https://www.linkedin.com/in/abhinav-raj-337092307/
