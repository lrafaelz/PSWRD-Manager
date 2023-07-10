import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from encryption.decryption import decrypt
from encryption.validation import is_valid
from encryption.files import read

def decrypto(file_path, key):
    # Read the entries from the file
    file_path="pswrd.txt"
    data = read(file_path)

    # Split the lines
    rows = data.splitlines()

    # Fill the matrix with entries from file
    encrypted_matrix = []
    for row in rows:
        elements = row.split(",")
        encrypted_row = [bytes.fromhex(element) for element in elements]
        encrypted_matrix.append(encrypted_row)

    # Check if the provided key is valid
    if not is_valid(key):
        print("Invalid key. The key size should be 16 bytes long.")
        return None

    # Decrypt the whole matrix
    decrypted_matrix = []
    try:
        for encrypted_row in encrypted_matrix:
            decrypted_row = []
            for element in encrypted_row:
                decrypted_element = decrypt(element[12:-16], key.encode(), element[:12], element[-16:])
                decrypted_row.append(decrypted_element)
            decrypted_matrix.append(decrypted_row)
    except ValueError as e:
        print(str(e))
        return None

    # Return the decrypted login and password
    return decrypted_matrix


if __name__ == "__main__":
    # Call the decrypt function with the name and key
    file_path = "pswrd.txt"
    key = input("Enter the key (in hexadecimal format): ").encode()
    decrypted_matrix = decrypto(file_path, key)

    if decrypted_matrix is not None:
        for row in decrypted_matrix:
            print(row)
