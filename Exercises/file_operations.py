import os
import glob
import json
from os import listdir

from django.db.models.expressions import result


# 5.1 Reading and Writing Text Files
def write_and_read_file():
    # TODO: Write "Hello, Python Students!" to sample.txt
    # TODO: Then read it and print the contents
    with open("sample.txt", "w") as file:
        file.write("Hello, Python Students!")

    with open("sample.txt", "r") as file:
        content = file.read()
        print(content)


# 5.2 Creating and Listing Directory Structure
def create_and_list_directory():
    # TODO: Create a new folder called "practice_folder"
    # TODO: List all files/folders in the current directory
    # TODO: List contents of "practice_folder"
    os.makedirs("practice_folder", exist_ok=True)
    print(listdir("."))
    print(os.listdir("practice_folder"))


# 5.3 Globbing (Pattern Matching for File Names)
def list_files_with_glob():
    # TODO: List all .txt files in current folder
    # TODO: List all .py files in current folder
    txt_files = glob.glob("*.txt")
    print(txt_files)


# 5.4 open() Modes for Different Scenarios
def open_file_modes():
    # TODO: Append "This is an appended line.\n" to log.txt
    # TODO: Write binary data to a file (e.g. bytes of 0, 1, 2)
    # TODO: Read that binary file and print the content
    with open("log.txt", "a") as f:
        f.write("This is an appended line .\n")
    with open("log.txt", "wb") as f:
        f.write(b'\x00\x01\x02')
    with open("log.txt", "rb") as f:
        data = f.read()


def append_to_file():
    print("\n--- append_to_file() ---")
    # TODO: Append "This is an appended line.\n" to log.txt
    with open("log.txt", "a") as f:
        f.write("This is an appended line.\n")
    print("Successfully appended to log.txt.")

# 5.4.2 Binary Write and Read
def binary_write_and_read():
    print("\n--- binary_write_and_read() ---")
    # TODO: Write binary data to a file
    binary_data = b'\x00\x01\x02'
    with open("binary_output.bin", "wb") as f:
        f.write(binary_data)
    print("Wrote binary data to binary_output.bin")

    # TODO: Read that binary file and print the content
    with open("binary_output.bin", "rb") as f:
        data = f.read()
    print("Binary file contents:")
    print(data)

# 5.5 Streaming Large Files (Line by Line)
def stream_large_file():
    # TODO: Create a large file with 10 lines ( you can copy large_file.txt below)
    # TODO: Read and print each line using a for loop
    with open("large_file.txt", "r") as file:
        for line in file:
            print(line.strip())


# 5.6 Read File as String or Parse as JSON
def read_and_write_json():
    # TODO: Write a dictionary {"course": "Python", "students": 20} to output.json
    # TODO: Read it back and print the result
    data = {"course": "Python", "students": 20}
    with open("output.json", "w") as f:
        json.dump(data, f)
    with open("output.json", "r") as f:
        result = json.load(f)
        print(result)

    with open("output.json", "w") as file:
        json.dump({"course": "Python", "students": 20}, file)
    with open("output.json", "r") as file:
        data = json.load(file)
        print(data)
    with open("output.txt", "r") as file:
        text = file.read()
        print(text)


# Run all exercises
if __name__ == "__main__":
    write_and_read_file()
    create_and_list_directory()
    list_files_with_glob()
    open_file_modes()
    append_to_file()
    binary_write_and_read()
    stream_large_file()
    read_and_write_json()