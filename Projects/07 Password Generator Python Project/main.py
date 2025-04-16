import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    characters = list(string.ascii_letters)  # A-Z, a-z

    if use_digits:
        characters.extend(string.digits)  # 0-9

    if use_specials:
        characters.extend(string.punctuation)  # !@#$%^&*

    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator! 🔐")
    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
        use_specials = input("Include special characters? (yes/no): ").lower() == 'yes'

        password = generate_password(length, use_digits, use_specials)
        print("\nYour generated password is:")
        print(password)
    except ValueError:
        print("Please enter a valid number for password length.")

if __name__ == "__main__":
    main()
