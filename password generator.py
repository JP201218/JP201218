import random
import string

def get_password_criteria():
    length = int(input("Enter the desired length of the password: "))
    has_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
    has_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
    has_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'
    
    return length, has_uppercase, has_numbers, has_special_chars

def generate_password(length, has_uppercase, has_numbers, has_special_chars):
    characters = string.ascii_lowercase
    if has_uppercase:
        characters += string.ascii_uppercase
    if has_numbers:
        characters += string.digits
    if has_special_chars:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    length, has_uppercase, has_numbers, has_special_chars = get_password_criteria()
    password = generate_password(length, has_uppercase, has_numbers, has_special_chars)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
