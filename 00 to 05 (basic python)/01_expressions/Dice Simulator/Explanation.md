🧠 Logic Recap: Dice Simulator

Variable     : What It Represents                   : User Input? : Explanation
---------------------------------------------------------------------------------------
NUM_SIDES    : Total sides on each die              : ❌ No        : Constant = 6
die1         : Local die value (inside main)        : ❌ No        : Starts as 10 in main()
die1, die2   : Random values between 1 and 6        : ❌ No        : Inside roll_dice(), new scope
total        : Sum of die1 + die2 in roll_dice()    : ❌ No        : Printed after each roll
roll_dice()  : Function that rolls 2 dice randomly  : ❌ No        : Called 3 times from main()
print(...)   : Show values before & after rolls     : ❌ No        : Demonstrates scope
