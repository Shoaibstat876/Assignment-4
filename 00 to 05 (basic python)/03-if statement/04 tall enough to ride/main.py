MINIMUM_HEIGHT: int = 50  # Minimum required height to ride 🎢

def main():
    height = float(input("How tall are you? "))  # Get height from user
    if height >= MINIMUM_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# Required to run main
if __name__ == '__main__':
    main()
