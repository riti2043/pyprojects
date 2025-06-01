import random
import string

def generate_password(length=12, use_symbols=True, use_numbers=True, use_upper=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "No character types selected!"

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Random Password Generator")

    length = int(input("Enter password length (default 12): ") or 12)
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_upper = input("Include uppercase? (y/n): ").lower() == 'y'

    password = generate_password(length, use_symbols, use_numbers, use_upper)
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
