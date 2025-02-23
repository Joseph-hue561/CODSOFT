import random
import string


def generate_password(length, include_symbols, include_numbers):
    """Generates a secure password based on user preferences."""
    characters = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"

    return ''.join(random.choice(characters) for _ in range(length))


def get_user_choice(prompt):
    """Gets a valid user choice for yes/no questions."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("⚠ Invalid input! Please enter 'y' for yes or 'n' for no.")


def get_password_length():
    """Gets a valid password length from the user."""
    while True:
        try:
            length = int(input("Enter the desired password length (min 4, max 100): "))
            if 4 <= length <= 100:
                return length
            print("⚠ Password length must be between 4 and 100 characters.")
        except ValueError:
            print("⚠ Invalid input! Please enter a number between 4 and 100.")

def save_password(password):
    """Saves the generated password to a file if the user chooses to."""
    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")
    print("💾 Password saved to saved_passwords.txt!")


def main():
    print("=" * 50)
    print("🔒 Welcome to the Secure Password Generator 🔒")
    print("=" * 50)

    while True:
        length = get_password_length()
        include_symbols = get_user_choice("Include symbols? (y/n): ")
        include_numbers = get_user_choice("Include numbers? (y/n): ")

        password = generate_password(length, include_symbols, include_numbers)
        print("\n🔑 Your Secure Password: ", password)

        if get_user_choice("Would you like to save this password? (y/n): "):
            save_password(password)

        if not get_user_choice("\nGenerate another password? (y/n): "):
            print("\n✅ Thank you for using the Password Generator. Stay secure! 🔒")
            break


if __name__ == "__main__":
    main()
