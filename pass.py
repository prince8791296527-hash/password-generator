import random
import string

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 PASSWORD GENERATOR 🔐")

    try:
        length = int(input("Enter password length: "))
        
        if length <= 0:
            print("Length must be greater than 0!")
            return

        print("\nInclude in password:")
        use_uppercase = input("Uppercase letters? (y/n): ").lower() == 'y'
        use_numbers = input("Numbers? (y/n): ").lower() == 'y'
        use_symbols = input("Symbols? (y/n): ").lower() == 'y'

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)

        print("\n✅ Generated Password:", password)

    except ValueError:
        print("❌ Please enter a valid number!")


if __name__ == "__main__":
    main()