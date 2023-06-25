from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import padding

def generate_key():
    # Generate a random 32-byte key using a secure random number generator
    key = os.urandom(32)
    return key

def generate_iv():
    # Generate a random 16-byte initialization vector (IV)
    iv = os.urandom(16)
    return iv

def encrypt_password(password, key):
    # Generate a random IV
    iv = generate_iv()

    # Create a cipher object using AES algorithm, CBC mode, and the generated IV
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

    # Create an encryptor object using the cipher
    encryptor = cipher.encryptor()

    # Apply PKCS7 padding to the password
    padded_password = padding.apply(password)

    # Encrypt the padded password
    cipher_text = encryptor.update(padded_password) + encryptor.finalize()

    # Return the IV and the encrypted password
    return iv, cipher_text
