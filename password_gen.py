import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    chars = string.ascii_lowercase
    if use_upper:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No character sets selected."

    return ''.join(random.choice(chars) for _ in range(length))

def main():
    print("🔐 Password Generator")
    length = int(input("Enter password length (e.g. 12): "))
    upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    digits = input("Include digits? (y/n): ").lower() == 'y'
    symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, upper, digits, symbols)
    print(f"\nGenerated password: {password}")

if __name__ == "__main__":
    main()
