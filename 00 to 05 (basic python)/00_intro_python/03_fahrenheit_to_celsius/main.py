def main():
    # Ask the user for temperature in Fahrenheit
    fahrenheit = input("Enter temperature in Fahrenheit: ")
    
    # Convert input to float (in case of decimals)
    fahrenheit = float(fahrenheit)

    # Convert to Celsius using formula
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Print result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

# Required line to run main function
if __name__ == '__main__':
    main()
