import random
import string


def generate_password(length):
    # Ensure password length is at least 4 to include all character types
    if length < 4:
        raise ValueError("Password length should be at least 4 characters.")

    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Ensure the password contains at least one of each character type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special_chars)
    ]

    # Fill the rest of the password length with random characters from all pools
    all_chars = lowercase + uppercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)

    # Shuffle the list to ensure the characters are in random order
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)


if __name__ == "__main__":
    try:
        password_length = int(input("Enter the desired length of the password: "))
        password = generate_password(password_length)
        print(f"Generated Password: {password}")
    except ValueError:
        password_length = int(input("Please enter an integer of > 4."))

