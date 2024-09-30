import random
import string

def generate_password(length, complexity):
    """
    Generate a random password based on user input.

    Args:
        length (int): Length of the password.
        complexity (str): Level of complexity (e.g., 'low', 'medium', 'high').

    Returns:
        str: Generated password.
    """
    characters = {
        'low': string.ascii_lowercase,
        'medium': string.ascii_letters + string.digits,
        'high': string.ascii_letters + string.digits + string.punctuation,
    }

    if complexity not in characters:
        raise ValueError("Invalid complexity level")

    password = ''.join(random.choice(characters[complexity]) for _ in range(length))
    return password

def main():
    print("Password Generator Application")
    print("--------------------------------")

    length = int(input("Enter password length: "))
    complexity = input("Enter complexity level (low/medium/high): ")

    password = generate_password(length, complexity)
    print("Generated Password : ", password)

if __name__ == "__main__":
    main()