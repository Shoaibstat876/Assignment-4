# Constants for time conversion
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate total seconds in a year
    seconds_in_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN

    # Display result
    print("There are " + str(seconds_in_year) + " seconds in a year!")

# Run the main function
if __name__ == '__main__':
    main()
