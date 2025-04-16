"""
Simulate rolling two dice, and prints results of each
roll as well as the total.
"""

import random  # To generate random numbers

# Number of sides on each die
NUM_SIDES: int = 6

def main():
    # Roll both dice
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)

    # Calculate total
    total: int = die1 + die2

    # Print the results
    print("Dice have", NUM_SIDES, "sides each.")
    print("First die:", die1)
    print("Second die:", die2)
    print("Total of two dice:", total)

# Run the main function
if __name__ == '__main__':
    main()
