🧠 Logic Recap: Flowing With Data (Mutability)

Variable         : What It Represents                         : User Input? : Explanation
-----------------------------------------------------------------------------------------------
my_list          : Empty list that will store 3 copies         : ❌ No        : Starts empty, mutated inside function
data             : Message input from the user                 : ✅ Yes       : Collected using input()
add_three_copies : Function to add data three times            : ❌ No        : Uses a loop with .append()
.append(...)     : Adds data to the list (in-place)            : ❌ No        : Mutates the original list (not a copy)
print(...)       : Displays list before and after function     : ❌ No        : Used to show effect of mutability
