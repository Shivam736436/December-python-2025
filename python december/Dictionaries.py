# Dictionaries --> A dictionary is a collection of data stored as key-value pairs.
# Keys must be unique and immutable (string, number, tuple)
# Values can be anything
# Dictionaries are unordered, mutable, and dynamic


# create
# Empty dictionary
d = {}

# With values
student = {
    "name": "John",
    "age": 20,
    "grade": "A"
}


# access
print(student["name"])   # John
print(student.get("age")) # 20


# 💡 get() doesn’t throw error if key missing.

# add student["age"] = 21       # modify
student["city"] = "NY"    # add new key-value

# remove
student.pop("grade")     # remove key-value
del student["age"]       # remove key-value
student.clear()          # removes all




# method
d = {"a": 1, "b": 2}

print(d.keys())     # dict_keys(['a', 'b'])
print(d.values())   # dict_values([1, 2])
print(d.items())    # dict_items([('a', 1), ('b', 2)])




# loop for key in d:
for key in d:
    print(key, d[key])

# or 

for key, value in d.items():
    print(key, value)




# Checking if Key Exists
if "name" in student:
    print("Exists")





# Nested Dictionaries
students = {
    "s1": {"name": "John", "age": 20},
    "s2": {"name": "Mike", "age": 22}
}

print(students["s1"]["name"])  # John





# Dictionary Comprehensions
squares = {x: x*x for x in range(5)}
print(squares)
# {0:0, 1:1, 2:4, 3:9, 4:16}


# 10. Why Use Dictionaries?
# Fast lookups
# Meaningful keys (readable code)
# Organize structured data
# Useful for JSON, APIs, configurations




# 🟢 Summary
# Feature	            Dictionary
# Structure	            Key-value pairs
# Ordered	            Yes (Python 3.7+)
# Mutable	            Yes
# Unique Keys	        Yes
# Values	            Any type


# 🔑 Key Points

# Use keys to access values
# Dictionaries are dynamic & flexible
# Great for structured data
# Supports nesting & comprehension