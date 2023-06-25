def write(file_path, data):
    # Write the data to the specified file path in binary mode
    with open(file_path, "wb") as file:
        file.write(data)

def read(file_path):
    # Read the data from the specified file path in binary mode
    with open(file_path, "rb") as file:
        data = file.read()

    return data
