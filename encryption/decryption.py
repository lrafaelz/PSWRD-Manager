from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from encryption.padding import remove

def decrypt(encrypted_element, key, nonce, tag):
    # Create a cipher object using AES algorithm and GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))

    # Create a decryptor object using the cipher
    decryptor = cipher.decryptor()

    # Decrypt the encrypted password
    decrypted_password = decryptor.update(encrypted_element) + decryptor.finalize()

    # Remove PKCS7 padding from the decrypted password
    password = remove(decrypted_password)

    # Return the decrypted password
    return password.decode()
