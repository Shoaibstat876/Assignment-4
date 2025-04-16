import random

DONE_LIKELIHOOD: float = 0.2  # 20% chance to stop each round

def chaotic_counting():
    for i in range(10):
        curr_num = i + 1
        if done():
            return  # Exit early if done() says so
        print(curr_num)

# Simulates the "random stopping" behavior
def done():
    """Returns True with a probability defined by DONE_LIKELIHOOD"""
    return random.random() < DONE_LIKELIHOOD

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("I'm done")

if __name__ == "__main__":
    main()
