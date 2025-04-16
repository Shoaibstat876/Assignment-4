🧠 Logic Recap: Leap Year Checker

Condition                     : What It Checks                                   : Outcome
-----------------------------------------------------------------------------------------------------
year % 4 == 0                 : Year is divisible by 4                           : Potential leap year
year % 100 == 0              : Year is divisible by 100                         : Not leap year (unless next line is true)
year % 400 == 0              : Year is divisible by 400                         : Is leap year
else                         : Fails any condition                              : Not a leap year
