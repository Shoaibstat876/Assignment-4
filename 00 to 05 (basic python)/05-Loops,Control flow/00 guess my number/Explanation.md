🧠 Logic Recap: Guess My Number

Variable            : What It Represents                                : User Input? : Explanation
---------------------------------------------------------------------------------------------------------
secret_number       : Randomly selected target number (1 to 99)         : ❌ No        : Set by `random.randint()`
guess               : User’s current guess                              : ✅ Yes       : Collected with `input()`
while guess != ...  : Loop until the guess matches the secret           : ❌ No        : Controls the game flow
if guess < secret   : Check if the guess is too low                     : ❌ No        : Gives feedback
else                : If not lower, guess must be too high              : ❌ No        : More feedback
print(... success)  : Ends the game with a congratulatory message       : ❌ No        : Triggered when guess is correct
