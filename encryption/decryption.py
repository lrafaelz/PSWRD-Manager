from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import padding

def decrypt_password(encrypted_password, key, iv):
    # Create a cipher object using AES algorithm, CBC mode, and the IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())

    # Create a decryptor object using the cipher
    decryptor = cipher.decryptor()

    # Decrypt the encrypted password
    decrypted_password = decryptor.update(encrypted_password) + decryptor.finalize()

    # Remove PKCS7 padding from the decrypted password
    password = padding.remove(decrypted_password)

    # Return the decrypted password
    return password.decode()
