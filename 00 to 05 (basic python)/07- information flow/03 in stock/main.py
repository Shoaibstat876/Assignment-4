def main():
    fruit: str = input("Enter a fruit: ")
    stock = num_in_stock(fruit)

    if stock == 0:
        print("This fruit is not in stock.")
    else:
        print("This fruit is in stock! Here is how many:")
        print(stock)

# --- Helper function below ---
def num_in_stock(fruit):
    """
    Returns the number of the given fruit in Sophia's inventory.
    """
    if fruit == 'apple':
        return 2
    if fruit == 'durian':
        return 4
    if fruit == 'pear':
        return 1000
    else:
        return 0  # fruit not found

if __name__ == '__main__':
    main()
