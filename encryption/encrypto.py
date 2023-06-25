import sys
import os
from encryption import generate_key, encrypt_password
from validation import is_valid
import files

def encrypt():
    # Check the number of arguments provided
    num_args = len(sys.argv)

    if num_args == 2:
        # Only password argument provided
        password = sys.argv[1]
        key = generate_key()
        print("Generated Key:", key.hex())
    elif num_args == 3:
        # Both password and key arguments provided
        password = sys.argv[1]
        key = sys.argv[2].encode()
    else:
        # Invalid number of arguments
        print("Invalid number of arguments. Please provide a password and an optional key.")
        return

    # Check if the provided key is valid
    if not is_valid(key):
        print("Invalid key. Generating a random key instead.")
        key = generate_key()
        print("Generated Key:", key.hex())

    # Encrypt the password and obtain the IV
    iv, encrypted_password = encrypt_password(password, key)

    # Write the IV and the encrypted password to a file
    files.write("pswrd.txt", iv + encrypted_password)

# Check if the script is being executed as the main entry point
if __name__ == "__main__":
    # If the condition is true, execute the code inside this block

    # Call the main function to start the program
    encrypt()
