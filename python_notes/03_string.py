# -----------------------------------------
# 1. Creating a dictionary
# -----------------------------------------
student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}
print("Original:", student)

# -----------------------------------------
# 2. Accessing values
# -----------------------------------------
print("Name:", student["name"])
print("Age (using get):", student.get("age"))

# -----------------------------------------
# 3. Adding new key-value
# -----------------------------------------
student["city"] = "Delhi"
print("After adding city:", student)

# -----------------------------------------
# 4. Changing value
# -----------------------------------------
student["marks"] = 90
print("After changing marks:", student)

# -----------------------------------------
# 5. Removing items
# -----------------------------------------
student.pop("city")             # remove by key
print("After pop(city):", student)

student.popitem()               # removes last key-value
print("After popitem():", student)

# Using del
del student["age"]
print("After del age:", student)

# clear() – empties dictionary
temp = {"a": 1, "b": 2}
temp.clear()
print("After clear():", temp)

# -----------------------------------------
# 6. keys(), values(), items()
# -----------------------------------------
person = {"name": "John", "age": 25, "job": "Engineer"}

print("Keys:", person.keys())
print("Values:", person.values())
print("Items:", person.items())

# -----------------------------------------
# 7. Looping in dictionary
# -----------------------------------------
print("Loop through keys:")
for k in person:
    print(k)

print("Loop through values:")
for v in person.values():
    print(v)

print("Loop through key & value:")
for k, v in person.items():
    print(k, "=", v)

# -----------------------------------------
# 8. Checking if key exists
# -----------------------------------------
if "name" in person:
    print("Key 'name' exists")

# -----------------------------------------
# 9. Copying dictionary
# -----------------------------------------
new_person = person.copy()
print("Copied dictionary:", new_person)

# -----------------------------------------
# 10. Nested dictionary
# -----------------------------------------
students = {
    "s1": {"name": "Ali", "age": 20},
    "s2": {"name": "Sara", "age": 22}
}

print("Nested dictionary:", students)
print("Sara age:", students["s2"]["age"])

# -----------------------------------------
# 11. update() → merge dictionaries
# -----------------------------------------
info1 = {"a": 1, "b": 2}
info2 = {"b": 100, "c": 200}

info1.update(info2)  # b gets replaced
print("After update:", info1)
