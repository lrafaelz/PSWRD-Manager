import sys
import os
from encryption import generate_key, encrypt_password
from validation import is_valid
import files

def encrypt(name, login, password, key=None):
    # Encrypt function takes name, login, password, and optional key as parameters

    if key is None:
        # If key is not provided, raise an error
        raise ValueError("No key provided.")

    if not is_valid(key):
        # Check if the provided key is valid
        raise ValueError("Invalid key. The key size should be 16 bytes long.")

    # Encrypt the login and password separately using the key
    encrypted_login = encrypt_password(login, key)
    encrypted_password = encrypt_password(password, key)

    # Concatenate name, login, and password separated by commas
    encrypted_data = f"{name},{encrypted_login.hex()},{encrypted_password.hex()}\n"

    # Append the encrypted data to the file
    files.append("pswrd.txt", encrypted_data)

if __name__ == "__main__":
    # If the script is executed as the main entry point

    # Prompt the user to enter the name
    name = input("Enter the name: ")

    # Prompt the user to enter the login
    login = input("Enter the login: ")

    # Prompt the user to enter the password
    password = input("Enter the password: ")

    # Prompt the user to enter the key (optional)
    key = input("Enter the key (optional): ").encode()

    try:
        # Call the encrypt function with the provided name, login, password, and key
        encrypt(name, login, password, key)

    except ValueError as e:
        # Print the error message and exit
        print(str(e))
        sys.exit(1)
