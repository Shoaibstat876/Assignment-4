# 🧠 Logic Recap: Print Multiple

Function / Variable     : What It Represents                       : User Input? : Explanation
-----------------------------------------------------------------------------------------------
print_multiple(...)      : Prints a message multiple times          : ❌ No        : Called by `main()` with user inputs
message                 : The text to print                        : ✅ Yes       : Captured via `input()`
repeats                 : Number of repetitions                    : ✅ Yes       : Converted to integer from input
for i in range(repeats) : Loop runs `repeats` times                : ❌ No        : Controls how many times to print
print(message)          : Prints one message on each loop cycle    : ❌ No        : Output shown to user
