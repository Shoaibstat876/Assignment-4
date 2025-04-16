def main():
    # Get the numbers we want to divide
    dividend: int = int(input("Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    # Calculate quotient and remainder
    quotient: int = dividend // divisor  # Integer division
    remainder: int = dividend % divisor  # Modulo (remainder)

    # Print result
    print("The result of this division is " + str(quotient) + " with a remainder of " + str(remainder))


# Run the main function
if __name__ == '__main__':
    main()
