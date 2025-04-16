🧠 Explanation.md: Joke Bot

This program is a simple joke bot that uses basic control flow (if-else) to check the user’s input and respond accordingly.

🎯 Logic Recap

Variable

What It Represents

User Input?

Explanation

PROMPT

Message to prompt the user

❌ No

A string asking the user: "What do you want?"

JOKE

The actual joke to be told

❌ No

A funny programmer-related joke about milk and eggs

SORRY

Fallback message if user doesn't request a joke

❌ No

Tells the user the bot only responds to jokes

user_input

Stores user’s response to the prompt

✅ Yes

Compares this to determine the output

✅ Logic

Ask the user: "What do you want?"

Convert user input to lowercase (to handle variations like "Joke", "joke", etc.)

If the word "joke" is found in the input, display the joke

Otherwise, display the sorry message