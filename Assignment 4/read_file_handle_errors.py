try:
    file = open("sample.txt", "r")
    print("Reading file content:")
    line_number = 1
    for line in file:
        print(f"Line {line_number}: {line.rstrip()}")
        line_number += 1
    file.close()
except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found.")
