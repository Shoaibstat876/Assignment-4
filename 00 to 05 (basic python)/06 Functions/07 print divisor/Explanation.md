# 🧠 Logic Recap: Print Divisors

Function / Variable   : What It Represents                          : User Input? : Explanation
-----------------------------------------------------------------------------------------------
print_divisors(num)   : Prints all numbers that divide `num`        : ✅ Yes       : Helper function to loop from 1 to num
range(num)            : Generates values 0 to num-1                 : ❌ No        : We add 1 to reach inclusive `num`
curr_divisor          : The current number being tested             : ❌ No        : `i + 1` to start from 1 instead of 0
num % curr_divisor    : Modulus to check clean division             : ❌ No        : No remainder = divisor
input("Enter...")     : Gets number from user                       : ✅ Yes       : Converted to int before use
