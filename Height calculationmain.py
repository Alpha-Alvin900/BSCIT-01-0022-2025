# Heights of the students
students = {
    "John": 170,
    "Alice": 172,
    "Bob": 150
}

# Find the tallest student
tallest_student = max(students, key=students.get)
tallest_height = students[tallest_student]

# Print the result
print(f"{tallest_student} is the tallest with {tallest_height}cm.")
