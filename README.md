# Simple Quiz Game

## Overview

Welcome to the "Simple Quiz Game" Python project! This interactive quiz game is designed to test your computer knowledge with 20 to 25 engaging questions.

## Getting Started

- Run the program to start the quiz.
- The user is welcomed with "Welcome to my Simple Computer Quiz."
- Prompted with the question, "Do you want to play the quiz (Yes/No)?"
- If the user chooses 'No', the program exits with a farewell message.
- If the user chooses 'Yes', the quiz begins with a cheerful "Let's go."

## Quiz Mechanics

- Questions and their corresponding correct answers are stored in a dictionary.
- Multiple-choice options for each question are stored in lists.
- The new_game() function displays questions, and the user selects an option (A, B, C, D).
- The check_answer() function verifies if the user's choice is correct.
- After completing the quiz, the display_score() function calculates the score and determines if the user passed or failed.

## Score and Completion

- The score is calculated as a percentage: score = int((correct_guesses/len(questions))*100).
- If the user scores 40% or above, they receive a "You passed the quiz" message; otherwise, "You failed the quiz" is displayed.

## Play Again

- The play_again() function prompts the user to play again.
- If the user chooses 'Yes', a new game begins.
- If the user chooses 'No', the program ends with a gratitude message: "Thank you for attending the Quiz."

Enjoy the quiz, and good luck testing your computer knowledge!
