# Starter Code for List Practice and Index Game

def list_practice():
    # TODO: Create a list called fruit_list that contains the following fruits:
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'

    # TODO: Print the length of the list

    # TODO: Add 'mango' at the end of the list

    # TODO: Print the updated list
    pass

def access_element(lst, index):
    # TODO: Return the element at index if valid, else return error message
    pass

def modify_element(lst, index, new_value):
    # TODO: Modify the element at index if valid, else return error message
    pass

def slice_list(lst, start, end):
    # TODO: Return slice from start to end if valid
    pass

def index_game():
    # This function runs a text-based index game
    lst = [1, 2, 3, 4, 5]
    print("Current list:", lst)
    print("Choose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        print(access_element(lst, index))
    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        print(modify_element(lst, index, new_value))
    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        print(slice_list(lst, start, end))
    else:
        print("Invalid operation.")

def main():
    list_practice()
    index_game()

if __name__ == "__main__":
    main()