🧠 Logic Recap: Whole Some Machine (Affirmation Checker)

Variable / Logic       : What It Represents                                     : User Input? : Explanation
---------------------------------------------------------------------------------------------------------------
AFFIRMATION            : The fixed sentence we expect user to type             : ❌ No        : Stored as a constant string
user_feedback          : User's current input                                   : ✅ Yes       : Collected using input()
while feedback != ...  : Loop until correct affirmation is typed                : ❌ No        : Keeps prompting if incorrect
print(... retry msg)   : Encouraging message for incorrect attempts             : ❌ No        : Guides user kindly
