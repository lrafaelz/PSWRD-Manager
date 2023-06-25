import sys
import binascii
from decryption import decrypt_password
from validation import is_valid
import files

def decrypt():
    # Read the encrypted password and IV from the file
    file_path = "pswrd.txt"
    data = files.read(file_path)

    if len(data) < 32:
        print("Invalid data in the file. Expected at least 32 bytes (IV + encrypted password).")
        return

    # Extract the IV and encrypted password from the data
    iv = data[:16]
    encrypted_password = data[16:]

    # Get the key from the command-line argument
    if len(sys.argv) < 2:
        print("Error: Key argument is missing.")
        return

    # Convert the key from hexadecimal string to bytes
    try:
        key = binascii.unhexlify(sys.argv[1])
    except binascii.Error:
        print("Error: Invalid key. The key must be a valid hexadecimal string.")
        return

    # Check if the provided key is valid
    if not is_valid(key):
        print("Invalid key. The key size should be 32 bytes long.")
        return

    # Decrypt the password
    try:
        password = decrypt_password(encrypted_password, key, iv)
    except ValueError as e:
        print(str(e))
        return

    # Print the decrypted password
    print("Decrypted Password:", password)

# Check if the script is being executed as the main entry point
if __name__ == "__main__":
    # If the condition is true, execute the code inside this block

    # Call the main function to start the program
    decrypt()
