def main():
    # Ask the user for a number
    num: float = float(input("Type a number to see its square: "))

    # Calculate and display the square
    print(str(num) + " squared is " + str(num ** 2))

# Required line to call main function
if __name__ == '__main__':
    main()
