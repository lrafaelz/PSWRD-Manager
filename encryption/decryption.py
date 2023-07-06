from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import padding

def decrypt_password(encrypted_password, key, nonce, tag):
    # Create a cipher object using AES algorithm and GCM mode
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag))

    # Create a decryptor object using the cipher
    decryptor = cipher.decryptor()

    # Decrypt the encrypted password
    decrypted_password = decryptor.update(encrypted_password) + decryptor.finalize()

    # Remove PKCS7 padding from the decrypted password
    password = padding.remove(decrypted_password)

    # Return the decrypted password
    return password.decode()
