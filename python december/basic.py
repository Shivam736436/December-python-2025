# -----------------------------
# PYTHON BASICS — FULL EXAMPLE
# -----------------------------

# This is a comment.
# Python ignores comments. They are for humans.

# ---------
# PRINTING
# ---------
print("Hello, Python!")  
# print() shows output on the screen


# ----------
# VARIABLES
# ----------
# Variables store data in memory

name = "Alex"      # string (text)
age = 20           # integer (number)
height = 5.9       # float (decimal)
is_student = True  # boolean (True / False)

print(name)
print(age)


# ----------------
# USER INPUT
# ----------------
# input() always returns a STRING

user_name = input("Enter your name: ")
print("Hello", user_name)


# ----------------
# TYPE CONVERSION
# ----------------
# Convert string to integer using int()

user_age = int(input("Enter your age: "))
print("Next year you will be", user_age + 1)


# ----------------
# IF / ELSE
# ----------------
# Used for decision making

if user_age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Indentation (spaces) is VERY important in Python


# ----------------
# LOOPS
# ----------------

# FOR LOOP
for i in range(5):   # range(5) means 0 to 4
    print("For loop value:", i)

# WHILE LOOP
count = 0
while count < 3:
    print("While loop value:", count)
    count += 1      # same as count = count + 1


# ----------------
# FUNCTIONS
# ----------------
# Functions are reusable blocks of code

def greet(person):
    # This function takes one parameter: person
    return "Hello " + person

# Call the function
message = greet("Alex")
print(message)


# ----------------
# FUNCTION WITH MATH
# ----------------
def add(a, b):
    return a + b

result = add(10, 5)
print("Sum is:", result)


# ----------------
# LISTS
# ----------------
# Lists store multiple values

numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])   # first element (index starts at 0)

# Loop through a list
for num in numbers:
    print("Number:", num)


# ----------------
# DICTIONARIES
# ----------------
# Key-value pairs

student = {
    "name": "Alex",
    "age": 20,
    "is_student": True
}

print(student["name"])
print(student["age"])


# ----------------
# FINAL MESSAGE
# ----------------
print("You just learned the core of Python 🎉")
