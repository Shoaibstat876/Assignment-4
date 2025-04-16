🧠 Logic Recap: Fibonacci Sequence (up to 10,000)

Variable             : What It Represents                               : User Input? : Explanation
------------------------------------------------------------------------------------------------------------
MAX_TERM_VALUE       : Maximum value allowed in the sequence            : ❌ No        : Set as a constant
curr_term            : Current number in the sequence                   : ❌ No        : Starts at 0 (Fib(0))
next_term            : Next number in the sequence                      : ❌ No        : Starts at 1 (Fib(1))
term_after_next      : Sum of current and next → future term            : ❌ No        : Fib(n+2) = Fib(n) + Fib(n+1)
while curr_term <=.. : Loop until values exceed the limit               : ❌ No        : Stops at 10,000
print(..., end=" ")  : Prints all values in a single line               : ❌ No        : Clean format
