# Assignment 4: Module 5 - Files, Exceptions, and Errors in Python

## Overview

This assignment focuses on file handling operations and exception handling in Python. It covers reading files with error handling and writing/appending data to files, which are fundamental skills for robust file-based applications.

## Tasks

### Task 1: Read File and Handle Errors

**File:** `read_file_handle_errors.py`

**Description:**
This program demonstrates how to read a file line by line while properly handling exceptions. It reads from `sample.txt` and prints each line to the console. If the file is not found, it catches the `FileNotFoundError` exception and displays an appropriate error message.

**Functionality:**
- Opens and reads a file named `sample.txt`
- Iterates through each line in the file
- Prints each line to the console
- Handles `FileNotFoundError` exception gracefully
- Displays error message if file is not found

**How to Run:**
```
python read_file_handle_errors.py
```

**Expected Output:**
```
Line 1: Sample content
Line 2: More sample data
Line 3: Additional content
```

**Key Concepts:**
- File I/O operations
- Exception handling with try-except blocks
- FileNotFoundError exception
- Reading files line by line

---

### Task 2: Write and Append Data to File

**File:** `write_append_file.py`

**Description:**
This program demonstrates file writing and appending operations. It writes initial data to `output.txt`, then appends additional data, and finally reads the file to display all content.

**Functionality:**
- Creates or overwrites `output.txt` with initial data
- Appends additional content to the file
- Reads and displays the complete file content
- Demonstrates different file modes (write and append)

**How to Run:**
```
python write_append_file.py
```

**Expected Output:**
```
File content:
Initial data written to file
Appended data
```

**Key Concepts:**
- File writing with 'w' mode
- File appending with 'a' mode
- File reading with 'r' mode
- File operations and context management

---

## File Structure

- `read_file_handle_errors.py` - Task 1 implementation
- `write_append_file.py` - Task 2 implementation
- `sample.txt` - Sample input file for Task 1
- `output.txt` - Output file for Task 2
- `README.md` - This documentation file

## Supporting Files

### sample.txt
Contains sample data that is read by `read_file_handle_errors.py`. This file is used to demonstrate file reading operations with error handling.

### output.txt
Used by `write_append_file.py` to demonstrate writing and appending operations. The program creates or overwrites this file with test data.

## Key Concepts Covered

1. **File I/O Operations**
   - Reading files
   - Writing to files
   - Appending to files
   - File modes: 'r', 'w', 'a'

2. **Exception Handling**
   - Try-except blocks
   - FileNotFoundError exception
   - Graceful error handling
   - Error messages

3. **Python File Handling**
   - Opening and closing files
   - Reading file contents
   - Iterating through file lines
   - File operations best practices

## Instructions for Execution

1. Ensure Python 3.x is installed on your system
2. Navigate to the Assignment 4 directory
3. Run Task 1: `python read_file_handle_errors.py`
4. Run Task 2: `python write_append_file.py`
5. Check the generated `output.txt` file for Task 2 results

## Repository Structure

```
Adit-python-assignment/
└── Assignment 4/
    ├── read_file_handle_errors.py
    ├── write_append_file.py
    ├── sample.txt
    ├── output.txt
    └── README.md
```

## Notes

- Both programs follow standard Python conventions for file handling
- Error handling is implemented to make programs robust
- File paths are relative and work when running from the Assignment 4 directory
- The programs demonstrate fundamental file I/O concepts essential for Python development
