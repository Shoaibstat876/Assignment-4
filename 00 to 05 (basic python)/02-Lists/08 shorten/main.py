MAX_LENGTH = 3  # You can tweak this value for testing

def shorten(lst):
    """
    Removes items from the end of the list until its length is MAX_LENGTH.
    Prints each removed item.
    """
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Remove the last item
        print("Removed:", removed)

# No need to edit below this line

def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

def main():
    lst = get_lst()
    shorten(lst)
    print("Shortened list:", lst)

if __name__ == '__main__':
    main()
