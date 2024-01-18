import random
import string

def generate_password(length=15,include_digit=True, include_special_char=True):
    letters = string.ascii_letters
    digits = string.digits if include_digit else ''
    special_chars = string.punctuation if include_special_char else ''
    all_chars = letters + digits + special_chars

    #password length is valid
    if length < 1:
        raise ValueError("Password length should be of  at least 1")

    # Generate the password
    password = ''.join(random.choice(all_chars) for i in range(length))

    return password

if __name__ == "__main__":
    # Example usage
    password_length = int(input("Enter the password length: "))
    include_digit = input("Include digits? (y/n): ").lower() == 'y'
    include_special_char = input("Include special characters? (y/n): ").lower() == 'y'

    generated_password = generate_password(
        length=password_length,
        include_digit=include_digit,
        include_special_char=include_special_char
    )

    print("Generated Password:", generated_password)
