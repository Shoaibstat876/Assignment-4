def greet(name):
    """
    Returns a greeting message for the given name.
    """
    return "Greetings " + name + "!"

def main():
    name: str = input("What's your name? ")
    print(greet(name))

if __name__ == '__main__':
    main()
