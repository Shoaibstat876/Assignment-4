def main():
    # Get the 3 side lengths of the triangle from user input
    side1: float = float(input("What is the length of side 1? "))
    side2: float = float(input("What is the length of side 2? "))
    side3: float = float(input("What is the length of side 3? "))

    # Calculate and display the perimeter
    perimeter: float = side1 + side2 + side3
    print("The perimeter of the triangle is " + str(perimeter))

# Required for executing main function
if __name__ == '__main__':
    main()
