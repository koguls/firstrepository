import os

def find_file_path(file_name):
    for root, dirs, files in os.walk('/'):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

# Example usage
filename = 'myfile.txt'
file_path = find_file_path(filename)

if file_path:
    print(f"The file '{filename}' was found at: {file_path}")
else:
    print(f"The file '{filename}' was not found.")
