def append(file_path, data):
    # Append the data to the specified file path in text mode
    with open(file_path, "a") as file:
        file.write(data)

def read(file_path):
    # Read the data from the specified file path in text mode
    with open(file_path, "r") as file:
        data = file.read()

    return data
