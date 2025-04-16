import random

N_NUMBERS: int = 10       # Number of random numbers to generate
MIN_VALUE: int = 1        # Minimum value (inclusive)
MAX_VALUE: int = 100      # Maximum value (inclusive)

def main():
    for _ in range(N_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value, end=" ")  # Print all numbers on one line with a space

# Required line to run the program
if __name__ == '__main__':
    main()
