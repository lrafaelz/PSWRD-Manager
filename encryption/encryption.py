from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
from cryptography.hazmat.primitives import padding

def generate_key():
    # Generate a random 16-byte key
    key = os.urandom(16)
    return key

def encrypt(password, key):
    # Generate a random nonce
    nonce = os.urandom(12)

    # Create a cipher object using AES algorithm, GCM mode, and the generated nonce
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce))

    # Create an encryptor object using the cipher
    encryptor = cipher.encryptor()

    # Apply PKCS7 padding to the password
    padder = padding.PKCS7(128).padder()
    padded_password = padder.update(password.encode()) + padder.finalize()

    # Encrypt the padded password
    cipher_text = encryptor.update(padded_password) + encryptor.finalize()

    # Retrieve the tag
    tag = encryptor.tag

    # Return the combined nonce and the encrypted password
    return nonce + cipher_text + tag
