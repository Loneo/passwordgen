import random
import string


def generate_password(length=12, use_digits=True, use_symbols=True):

    letters = string.ascii_letters  # a-z, A-Z
    digits = string.digits if use_digits else ""
    symbols = string.punctuation if use_symbols else ""

    all_characters = letters + digits + symbols

    if not all_characters:
        raise ValueError("No characters available for password generation!")

    # Ensure password has at least one of each type chosen
    password = []
    if use_digits:
        password.append(random.choice(digits))
    if use_symbols:
        password.append(random.choice(symbols))
    password.append(random.choice(letters))

    # Fill the rest randomly
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle to avoid predictable pattern
    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_digits = input("Include digits? (y/n, default y): ").lower() != "n"
        use_symbols = input("Include symbols? (y/n, default y): ").lower() != "n"

        password = generate_password(length, use_digits, use_symbols)
        print(f"\nGenerated password: {password}")

    except Exception as e:
        print("Error:", e)
