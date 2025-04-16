import random

def main():
    # Generate a secret number between 1 and 99
    secret_number = random.randint(1, 99)

    print("I am thinking of a number between 1 and 99...")

    # First guess
    guess = int(input("Enter a guess: "))

    # Loop until the guess is correct
    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low")
        else:
            print("Your guess is too high")

        print()  # Empty line for spacing
        guess = int(input("Enter a new guess: "))

    # Congratulate the user
    print("Congrats! The number was: " + str(secret_number))

if __name__ == '__main__':
    main()
