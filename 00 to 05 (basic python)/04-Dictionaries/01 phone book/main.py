def read_phone_numbers():
    """
    Ask the user for names and numbers to store in a phonebook (dictionary).
    Returns the completed phonebook.
    """
    phonebook = {}
    while True:
        name = input("Name: ")
        if name == "":
            break
        number = input("Number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):
    """
    Prints each name and number from the phonebook.
    """
    for name in phonebook:
        print(str(name) + " -> " + str(phonebook[name]))

def lookup_numbers(phonebook):
    """
    Allow the user to search for a number by name.
    Continues until the user enters a blank input.
    """
    while True:
        name = input("Enter name to lookup: ")
        if name == "":
            break
        if name not in phonebook:
            print(name + " is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_numbers(phonebook)

if __name__ == '__main__':
    main()
