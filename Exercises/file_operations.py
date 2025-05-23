"""
File Operations Exercises
Fill in each section with appropriate code based on what you learned in class.
"""

import os
import glob
import json

# 5.1 Reading and Writing Text Files
def write_and_read_file():
    # Write "Hello, Python Students!" to sample.txt
    with open("sample.txt", "w") as f:
        f.write("Hello, Python Students!")
    # Then read it and print the contents
    with open("sample.txt", "r") as f:
        content = f.read()
    print("\n--- write_and_read_file() ---")
    print(content)

# 5.2 Creating and Listing Directory Structure
def create_and_list_directory():
    # Create a new folder called "practice_folder"
    folder = "practice_folder"
    if not os.path.exists(folder):
        os.mkdir(folder)
    # List all files/folders in the current directory
    print("\n--- create_and_list_directory() ---")
    print("Current directory contents:", os.listdir("."))
    # List contents of "practice_folder"
    print("practice_folder contents:", os.listdir(folder))

# 5.3 Globbing (Pattern Matching for File Names)
def list_files_with_glob():
    # List all .txt files in current folder
    txt_files = glob.glob("*.txt")
    # List all .py files in current folder
    py_files = glob.glob("*.py")
    print("\n--- list_files_with_glob() ---")
    print("TXT files:", txt_files)
    print("PY files:", py_files)

# 5.4 open() Modes for Different Scenarios
def open_file_modes():
    # Append "This is an appended line.\n" to log.txt
    with open("log.txt", "a") as f:
        f.write("This is an appended line.\n")
    # Write binary data to a file (e.g. bytes of 0, 1, 2)
    binary_data = b'\x00\x01\x02'
    with open("binary_output.bin", "wb") as f:
        f.write(binary_data)
    # Read that binary file and print the content
    with open("binary_output.bin", "rb") as f:
        data = f.read()
    print("\n--- open_file_modes() ---")
    print("Binary file contents:", data)
# 5.4.2 Binary Write and Read
def append_to_file():
    print("\n--- append_to_file() ---")
    # Append "This is an appended line.\n" to log.txt
    with open("log.txt", "a") as f:
        f.write("This is an appended line.\n")
    print("Successfully appended to log.txt.")

# 5.4.2 Binary Write and Read
def binary_write_and_read():
    print("\n--- binary_write_and_read() ---")
    # Write binary data to a file
    binary_data = b'\x00\x01\x02'
    with open("binary_output.bin", "wb") as f:
        f.write(binary_data)
    print("Wrote binary data to binary_output.bin")

    # Read that binary file and print the content
    with open("binary_output.bin", "rb") as f:
        data = f.read()
    print("Binary file contents:")
    print(data)

# 5.5 Streaming Large Files (Line by Line)
def stream_large_file():
    # Read and print each line using a for loop
    print("\n--- stream_large_file() ---")
    with open("large_data.txt", "r") as f:
        for line in f:
            print(line.strip())

# 5.6 Read File as String or Parse as JSON
def read_and_write_json():
    # Write a dictionary {"course": "Python", "students": 20} to output.json
    print("\n--- read_and_write_json() ---")
    data = {"course": "Python", "students": 20}
    print(f"Wrote JSON {data} to output.json")
    with open("output.json", "w") as f:
        json.dump(data, f)
    # Read it back and print the result
    with open("output.json", "r") as f:
        loaded = json.load(f)

    print(loaded)

# Run all exercises
if __name__ == "__main__":
    write_and_read_file()
    binary_write_and_read()
    append_to_file()
    create_and_list_directory()
    list_files_with_glob()
    open_file_modes()
    stream_large_file()
    read_and_write_json()
