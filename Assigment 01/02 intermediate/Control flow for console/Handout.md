handout.md

Problem: High Low

We want you to gain more experience working with control flow and Booleans in Python. To do this, we are going to have you develop a game! The game is called High-Low and it works as follows:

Game Description

Two numbers are generated randomly (1-100 inclusive): one for you and one for the computer.

You can see your number, but not the computer's number.

You guess if your number is higher or lower than the computer's.

If you’re correct, you gain a point.

The game plays for a set number of rounds (NUM_ROUNDS).

SAMPLE RUN:
Welcome to the High-Low Game!
--------------------------------
Round 1
Your number is 8
Do you think your number is higher or lower than the computer's?: lower
You were right! The computer's number was 35
Your score is now 1
...etc.

Milestones

✅ Milestone 1: Generate random numbers

Print welcome message

Generate player and computer numbers (1–100)

Print both numbers (for testing only)

✅ Milestone 2: Get the user guess

Ask the user to guess "higher" or "lower"

Accept the string input

✅ Milestone 3: Check game logic

If guess is correct: print positive message + reveal computer’s number

Else: print negative message + reveal computer’s number

✅ Milestone 4: Multiple rounds

Use a for loop to play multiple rounds

Print round number and leave a blank line between rounds

✅ Milestone 5: Score tracker

Keep track of the player’s score and display it after each round

🌟 Extension 1: Input safeguard

If user types something other than "higher" or "lower", re-ask the question

🌟 Extension 2: Endgame evaluation

Perfect game → "Wow! You played perfectly!"

Score >= half rounds → "Good job, you played really well!"

Score < half → "Better luck next time!"

