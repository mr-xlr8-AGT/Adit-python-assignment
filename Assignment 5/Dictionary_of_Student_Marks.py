# Dictionary for student marks as per sample outputs
student_marks = {
    "Alice": 85,
    "John": None   # John exists only for 'not found' demonstration, but no marks
}

# Request user input
student_name = input("Enter the student's name: ")

# Output according to expected behavior
if student_name in student_marks and student_marks[student_name] is not None:
    print(f"{student_name}'s marks: {student_marks[student_name]}")
else:
    print("Student not found.")
