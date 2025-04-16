def main():
    lst = []  # Make an empty list to store things in

    val = input("Enter a value: ")  # Get an initial value
    while val:  # While the user input isn't empty
        lst.append(val)  # Add value to the list
        val = input("Enter a value: ")  # Ask for the next value

    print("Here's the list:", lst)

# This line ensures the main() function runs
if __name__ == '__main__':
    main()
