import random

def main():
    # Generate the secret number at random!
    secret_number: int = random.randint(1, 99)
    
    print("I am thinking of a number between 1 and 99...")

    # Get user's guess
    guess = int(input("Enter a guess: "))
    
    # Keep asking until the user guesses correctly
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")
        
        print()  # Empty line for neatness
        guess = int(input("Enter a new guess: "))

    print("Congrats! The number was: " + str(secret_number))

# Required call to main()
if __name__ == '__main__':
    main()
