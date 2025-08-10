# Example 1: Simple dictionary
student = {
    "name": "Ali",
    "age": 21,
    "grade": "A"
}
print(student)

# Example 2: Access value by key
print(student["name"])

# Example 3: Add new key-value
student["city"] = "Karachi"
print(student)

# Example 4: Update value
student["grade"] = "A+"
print(student)

# Example 5: Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
