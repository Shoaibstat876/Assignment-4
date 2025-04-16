"""
Program: Feet to Inches Converter
-------------------------------
Converts feet to inches using a constant.
"""

# Conversion factor: 1 foot = 12 inches
INCHES_IN_FOOT: int = 12

def main():
    # Ask user to enter number of feet
    feet: float = float(input("Enter number of feet: "))

    # Convert feet to inches
    inches: float = feet * INCHES_IN_FOOT

    # Display the result
    print("That is", inches, "inches!")

# Run the main function
if __name__ == '__main__':
    main()
