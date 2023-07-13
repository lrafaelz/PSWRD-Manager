from cryptography.hazmat.primitives import padding

def apply(data):
    # Apply PKCS7 padding to the data
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data.encode()) + padder.finalize()
    return padded_data

def remove(data):
    # Remove PKCS7 padding from the data
    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(data) + unpadder.finalize()
    return unpadded_data
