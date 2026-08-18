# ==========================================
# Python Dictionary - Student Record Management
# ==========================================

# ------------------------------------------
# Part 1 - Create Dictionary
# ------------------------------------------

student = {
    "name": "Ali",
    "age": 20,
    "course": "Python",
    "marks": 75
}

# ------------------------------------------
# Part 1 - Access Items
# ------------------------------------------

print("----- Part 1: Access Items -----")

print("Student Name:", student["name"])
print("Student Age:", student["age"])
print("Student Course:", student["course"])
print("Student Marks:", student["marks"])

# Using get()
print("Course using get():", student.get("course"))


# ------------------------------------------
# Part 2 - Change Items
# ------------------------------------------

print("\n----- Part 2: Change Items -----")

student["age"] = 21
student["course"] = "Machine Learning"
student["marks"] = 85

print("After changing items:")
print(student)


# ------------------------------------------
# Part 3 - Add Items
# ------------------------------------------

print("\n----- Part 3: Add Items -----")

student["city"] = "Islamabad"
student["attendance"] = 90
student["grade"] = "A"

print("After adding items:")
print(student)


# ------------------------------------------
# Part 4 - Remove Items
# ------------------------------------------

print("\n----- Part 4: Remove Items -----")

# Remove grade using del
del student["grade"]

print("After removing grade:")
print(student)

# Remove attendance using del
del student["attendance"]

print("After removing attendance:")
print(student)

# Remove city using pop()
student.pop("city")

print("After removing city:")
print(student)


# ------------------------------------------
# Part 5 - Final Student Record
# ------------------------------------------

print("\n----- Part 5: Final Student Record -----")

print("Final Dictionary:")
print(student)

print("\nKey and Value separately:")

for key, value in student.items():
    print(key, ":", value)


# ==========================================
# Challenge Task - Student 2
# ==========================================

print("\n==========================================")
print("Challenge Task - Student 2")
print("==========================================")

student2 = {
    "name": "Sara",
    "age": 19,
    "course": "Data Science",
    "marks": 92
}

# 1. Access name and marks
print("\nStudent 2 Name:", student2["name"])
print("Student 2 Marks:", student2["marks"])

# 2. Change marks
student2["marks"] = 95

print("\nAfter changing marks:")
print(student2)

# 3. Add city
student2["city"] = "Lahore"

# 4. Add attendance
student2["attendance"] = 96

print("\nAfter adding city and attendance:")
print(student2)

# 5. Remove city
student2.pop("city")

print("\nAfter removing city:")
print(student2)

# 6. Final dictionary
print("\nFinal Student 2 Dictionary:")
print(student2)