import math  # Import the math library so we can use sqrt()

def main():
    # Ask for the two perpendicular side lengths
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    # Apply Pythagorean Theorem: hypotenuse^2 = ab^2 + ac^2
    bc: float = math.sqrt(ab ** 2 + ac ** 2)

    # Display the hypotenuse
    print("The length of BC (the hypotenuse) is: " + str(bc))

# This runs the main function when executed
if __name__ == '__main__':
    main()
