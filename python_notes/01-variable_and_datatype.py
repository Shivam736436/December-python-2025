"""
=========================================
PYTHON VARIABLES & DATA TYPES – FULL GUIDE
=========================================
"""

# ----------------------------------------
# 1. VARIABLES
# ----------------------------------------
# A variable is a name that stores a value in memory

x = 10              # integer variable
y = 3.14            # float variable
name = "Python"     # string variable
is_valid = True     # boolean variable

print(x, y, name, is_valid)

# ----------------------------------------
# 2. RULES FOR NAMING VARIABLES
# ----------------------------------------
# ✔ Must start with a letter or underscore
# ✔ Can contain letters, numbers, underscore
# ❌ Cannot start with a number
# ❌ Cannot use keywords

my_var = 10
_var = 20
myVar123 = 30

# 1var = 10   # ❌ invalid
# for = 5     # ❌ invalid

# ----------------------------------------
# 3. MULTIPLE ASSIGNMENT
# ----------------------------------------
a, b, c = 1, 2, 3
print(a, b, c)

x = y = z = 100
print(x, y, z)

# ----------------------------------------
# 4. DYNAMIC TYPING
# ----------------------------------------
# Python allows changing type at runtime

value = 10
print(value, type(value))

value = "Ten"
print(value, type(value))

# ----------------------------------------
# 5. TYPE() FUNCTION
# ----------------------------------------
num = 5
print(type(num))

# ----------------------------------------
# 6. BUILT-IN DATA TYPES
# ----------------------------------------

# Numeric Types
i = 10          # int
f = 2.5         # float
c = 3 + 4j      # complex

print(i, f, c)
print(type(c))

# ----------------------------------------
# 7. BOOLEAN TYPE
# ----------------------------------------
is_python_easy = True
is_java_easy = False

print(is_python_easy)
print(type(is_python_easy))

# ----------------------------------------
# 8. STRING TYPE
# ----------------------------------------
text = "Hello Python"
print(text)
print(text[0])      # indexing
print(len(text))    # length

# ----------------------------------------
# 9. LIST (Mutable)
# ----------------------------------------
numbers = [1, 2, 3, 4]
numbers.append(5)
numbers[0] = 100

print(numbers)
print(type(numbers))

# ----------------------------------------
# 10. TUPLE (Immutable)
# ----------------------------------------
point = (10, 20, 30)
print(point)
print(type(point))

# point[0] = 5  # ❌ Error

# ----------------------------------------
# 11. SET (Unique values)
# ----------------------------------------
unique_numbers = {1, 2, 3, 3, 4}
unique_numbers.add(5)

print(unique_numbers)
print(type(unique_numbers))

# ----------------------------------------
# 12. DICTIONARY (Key-Value Pair)
# ----------------------------------------
student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}

print(student)
print(student["name"])
print(type(student))

# ----------------------------------------
# 13. NONE TYPE
# ----------------------------------------
result = None
print(result)
print(type(result))

# ----------------------------------------
# 14. TYPE CASTING
# ----------------------------------------
x = "100"
y = int(x)
z = float(x)

print(y, type(y))
print(z, type(z))

# ----------------------------------------
# 15. TYPE CONVERSION FUNCTIONS
# ----------------------------------------
print(int(3.5))
print(float(5))
print(str(10))
print(list("Python"))
print(tuple([1, 2, 3]))
print(set([1, 2, 2, 3]))

# ----------------------------------------
# 16. MUTABLE vs IMMUTABLE
# ----------------------------------------
# Mutable ( which can be change): list, set, dict
# Immutable ( which can not be change): int, float, str, tuple

a = 10
b = a
b = 20
print(a)  # a remains unchanged

lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1)  # list is changed

# ----------------------------------------
# 17. MEMORY REFERENCE (id)
# ----------------------------------------
x = 10
y = 10
print(id(x), id(y))  # same memory for immutable objects

# ----------------------------------------
# 18. DELETING VARIABLES
# ----------------------------------------
temp = 100
del temp
# print(temp)  # ❌ NameError

# ----------------------------------------
# 19. CHECK VARIABLE TYPE

# isinstance() is used to check whether a variable (object) belongs to a specific data type or class.
# ----------------------------------------
value = 10
print(isinstance(value, int))
print(isinstance(value, str))

# ----------------------------------------
# 20. CONSTANTS (By Convention)
# ----------------------------------------
PI = 3.14159
GRAVITY = 9.8

print(PI, GRAVITY)

# ----------------------------------------
# END OF VARIABLES & DATA TYPES
# ----------------------------------------
