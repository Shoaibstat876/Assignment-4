def main():
    numbers: list[int] = [1, 2, 3, 4]  # Create a list of numbers

    for i in range(len(numbers)):  # Loop through each index
        elem_at_index = numbers[i]  # Get the element at index i
        numbers[i] = elem_at_index * 2  # Double the value at that index

    print(numbers)  # Print the modified list

# Required to run main() when file is executed
if __name__ == '__main__':
    main()
