# Program: add2numbers
# --------------------
# This program asks the user for two integers and prints their sum.

def main():
    print("This program adds two numbers.")
    
    num1: str = input("Enter first number: ")
    num1: int = int(num1)
    
    num2: str = input("Enter second number: ")
    num2: int = int(num2)
    
    total: int = num1 + num2
    
    print("The total is " + str(total) + ".")

# This line calls the main() function when the script is run directly
if __name__ == '__main__':
    main()
