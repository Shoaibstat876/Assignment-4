# 🧠 Logic Recap: Choosing Returns (is_adult function)

Variable / Function   : What It Does                           : User Input? : Explanation
--------------------------------------------------------------------------------------------
ADULT_AGE             : Legal age threshold (18)               : ❌ No        : Constant used for comparison
age                   : Person’s age entered by user           : ✅ Yes       : Passed to `is_adult(age)`
is_adult(age)         : Returns True or False                  : ❌ No        : Based on whether age >= ADULT_AGE
return True           : Executes if person is 18 or older      : ❌ No        : Confirms they are an adult
return False          : Executes if age is less than 18        : ❌ No        : They are not considered an adult
