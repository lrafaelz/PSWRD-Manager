def save(file_path, data):
    # Append the data to the specified file path in text mode
    with open(file_path, "w") as file:
        for row in data:
            row_str = ",".join(row)
            file.write(row_str + "\n")

def read(file_path):
    # Read the data from the specified file path in text mode
    with open(file_path, "r") as file:
        data = file.read()

    return data
