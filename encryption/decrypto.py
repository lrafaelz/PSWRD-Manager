import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from decryption import decrypt_password
from validation import is_valid
import files

def decrypt(name, key):
    # Read the entries from the file
    file_path = "pswrd.txt"
    data = files.read(file_path)

    # Split the lines
    entries = data.splitlines()

    # Search for a matching entry based on the name
    for entry in entries:
        parts = entry.split(",")
        if len(parts) == 3 and parts[0] == name:
            encrypted_login = bytes.fromhex(parts[1])
            encrypted_password = bytes.fromhex(parts[2])
            break
    else:
        print("No entry found for the provided name.")
        return None, None

    # Check if the provided key is valid
    if not is_valid(key):
        print("Invalid key. The key size should be 16 bytes long.")
        return None, None

    # Decrypt the login and password
    try:
        decrypted_login = decrypt_password(encrypted_login[12:-16], key, encrypted_login[:12], encrypted_login[-16:])
        decrypted_password = decrypt_password(encrypted_password[12:-16], key, encrypted_password[:12], encrypted_password[-16:])
    except ValueError as e:
        print(str(e))
        return None, None

    # Return the decrypted login and password
    return decrypted_login, decrypted_password


# Call the decrypt function with the name and key
name = input("Enter the name to search: ")
key = input("Enter the key (in hexadecimal format): ").encode()
login, password = decrypt(name, key)

if login is not None and password is not None:
    print("Decrypted Login:", login)
    print("Decrypted Password:", password)
