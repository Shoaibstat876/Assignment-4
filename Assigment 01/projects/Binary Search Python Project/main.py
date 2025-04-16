def binary_search(arr, target):
    """
    Performs binary search on a sorted list 'arr' to find the target.
    Returns the index if found, otherwise returns -1.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    print("🔍 Binary Search Demo 🔍")
    sorted_list = list(range(1, 101))  # Sorted list from 1 to 100
    print("List:", sorted_list)

    try:
        target = int(input("Enter the number to search for (1-100): "))
        index = binary_search(sorted_list, target)

        if index != -1:
            print(f"✅ Found {target} at index {index}.")
        else:
            print(f"❌ {target} not found in the list.")
    except ValueError:
        print("⚠️ Please enter a valid integer!")


if __name__ == "__main__":
    main()
