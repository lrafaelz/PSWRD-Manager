import sys
from encryption import generate_key, encrypt
from validation import is_valid
import files

def encrypto(matrix, key=None):
    if key is None:
        raise ValueError("No key provided.")

    if not is_valid(key):
        raise ValueError("Invalid key. The key size should be 16 bytes long.")

    # Encrypt the whole matrix using the key
    encrypted_matrix = []
    for row in matrix:
        encrypted_row = []
        for element in row:
            encrypted_element = encrypt(element, key)
            encrypted_row.append(encrypted_element.hex())
        encrypted_matrix.append(encrypted_row)

    # Save the new file, overwriting the old one
    files.save("pswrd.txt", encrypted_matrix)

if __name__ == "__main__":
    rows = int(input("Enter the number of rows in the matrix: "))
    columns = int(input("Enter the number of columns in the matrix: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            # Prompt the user to enter the matrix elements
            element = input(f"Enter the element at position ({i}, {j}): ")
            row.append(element)
        matrix.append(row)

    # Prompt the user to enter the key (optional)
    key = input("Enter the key (optional): ").encode()

    try:
        # Call the encrypt_matrix function with the provided matrix and key
        encrypted_matrix = encrypto(matrix, key)

    except ValueError as e:
        # Print the error message and exit
        print(str(e))
        sys.exit(1)
