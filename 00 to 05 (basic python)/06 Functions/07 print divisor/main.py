def print_divisors(num: int):
    """
    Prints all divisors of the given number.
    A divisor is any number that divides `num` with no remainder.
    """
    print("Here are the divisors of", num)
    for i in range(num):
        curr_divisor = i + 1  # We want to check from 1 to num
        if num % curr_divisor == 0:
            print(curr_divisor)

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
