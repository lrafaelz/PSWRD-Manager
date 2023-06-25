def is_valid(key):
    # Check if the key is a valid AES key (32 bytes)
    return isinstance(key, bytes) and len(key) == 32
