def is_valid(key):
    # Check if the key is a valid AES key (16 bytes)
    print(key)
    data = bytes.fromhex(key)
    return isinstance(data, bytes) and len(key) == 16
