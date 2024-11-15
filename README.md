# 12 Great Number Game


## Overview

The **Great Number Game** is a simple guessing game where players try to guess a random number between 1 and 100. The player selects a difficulty level (easy or hard), which determines how many attempts they have to guess correctly. Each guess provides feedback on whether it was too high, too low, or correct. This is the Day 12 Challenge from Dr. Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp**. This game is designed to practice Python fundamentals and scope.


## Table of Contents

- [Features](#features)
- [How the Program Works](#how-the-program-works)
- [Running the Game](#running-the-game)


## Features

- **Difficulty Levels**: Adjusts the number of attempts based on chosen difficulty.
- **Random Number Generation**: Each game generates a new number to guess.
- **User Feedback**: Provides hints on whether the guess is too high or too low.


## How the Program Works

1. **Logo Display**: The game displays a stylized logo for The Great Number Game, created using ASCII art.

2. **Game Flow**:
   - The game picks a random number between 1 and 100.
   - Players are prompted to choose a difficulty level:
     - **Easy**: 10 attempts
     - **Hard**: 5 attempts
   - If the input is invalid, the game exits.
   - Players enter their guesses, and the game tells them if their guess is too high, too low, or correct.
   - If the player runs out of attempts, the game informs them that they lost.

3. **End of Game**:
   - The game ends when the player guesses correctly or exhausts all attempts.


## Running the Game

1. Clone the repository:
   ```bash
   git clone https://github.com/coderbri/12_great_number_game.git
   cd 12_great_number_game
   ```
2. Run the main program:
   ```bash
   python main.py
   ```

3. Follow the on-screen instructions to start playing!


---
<section align="center">
  <code>coderBri © 2024</code>
</section>
