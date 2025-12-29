"""
===============================
PYTHON STRINGS – COMPLETE GUIDE
===============================

A string is a sequence of characters enclosed in quotes.
Strings are IMMUTABLE (cannot be changed in place).
"""

# -----------------------------
# 1. Creating Strings
# -----------------------------
s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line
string"""

print(s1, s2)
print(s3)

# -----------------------------
# 2. String with Quotes Inside
# -----------------------------
s4 = "It's Python"
s5 = 'He said "Hello"'
s6 = "He said \"Hello\""   # Escape character

print(s4)
print(s5)
print(s6)

# -----------------------------
# 3. Indexing (0-based)
# -----------------------------
text = "Python"

print(text[0])    # P
print(text[1])    # y
print(text[-1])   # n (last character)

# -----------------------------
# 4. Slicing [start:end:step]
# -----------------------------
print(text[0:4])    # Pyth
print(text[:3])     # Pyt
print(text[2:])     # thon
print(text[::2])    # Pto
print(text[::-1])   # Reverse string

# -----------------------------
# 5. Strings are Immutable
# -----------------------------
# text[0] = "J"   # ❌ ERROR
text = "J" + text[1:]  # ✔ Correct way
print(text)

# -----------------------------
# 6. String Length
# -----------------------------
print(len(text))

# -----------------------------
# 7. String Concatenation
# -----------------------------
a = "Hello"
b = "Python"
print(a + " " + b)

# -----------------------------
# 8. Repetition
# -----------------------------
print("Hi! " * 3)

# -----------------------------
# 9. Membership Operators
# -----------------------------
print("Py" in "Python")     # True
print("Java" not in "Python")  # True

# -----------------------------
# 10. String Methods (Common)
# -----------------------------
msg = "  hello python  "

print(msg.upper())
print(msg.lower())
print(msg.title())
print(msg.capitalize())
print(msg.strip())      # removes spaces
print(msg.lstrip())
print(msg.rstrip())

# -----------------------------
# 11. Searching in Strings
# -----------------------------
text = "python programming"

print(text.find("program"))    # index
print(text.find("Java"))       # -1
print(text.count("o"))

# -----------------------------
# 12. Replace
# -----------------------------
print(text.replace("python", "java"))

# -----------------------------
# 13. Split and Join
# -----------------------------
data = "apple,banana,orange"
fruits = data.split(",")
print(fruits)

joined = "-".join(fruits)
print(joined)

# -----------------------------
# 14. Checking String Content
# -----------------------------
num = "123"
alpha = "abc"
alnum = "abc123"

print(num.isdigit())
print(alpha.isalpha())
print(alnum.isalnum())
print("   ".isspace())

# -----------------------------
# 15. String Formatting
# -----------------------------
name = "Alice"
age = 25

# Old style
print("Name: %s, Age: %d" % (name, age))

# format() method
print("Name: {}, Age: {}".format(name, age))

# f-strings (BEST & MODERN)
print(f"Name: {name}, Age: {age}")

# -----------------------------
# 16. Escape Characters
# -----------------------------
print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab
print("C:\\Users\\Admin")

# -----------------------------
# 17. Raw Strings
# -----------------------------
path = r"C:\Users\Admin\Desktop"
print(path)

# -----------------------------
# 18. Encoding & Decoding
# -----------------------------
text = "Python"
encoded = text.encode("utf-8")
print(encoded)

decoded = encoded.decode("utf-8")
print(decoded)

# -----------------------------
# 19. Comparing Strings
# -----------------------------
print("apple" == "apple")
print("apple" > "banana")  # Lexicographical comparison

# -----------------------------
# 20. Iterating Through a String
# -----------------------------
for char in "ABC":
    print(char)

# -----------------------------
# 21. String as Sequence
# -----------------------------
print(list("Python"))
print(tuple("Python"))

# -----------------------------
# 22. Useful Built-in Functions
# -----------------------------
print(min("Python"))
print(max("Python"))
print(sorted("Python"))

# -----------------------------
# END OF STRING GUIDE
# -----------------------------
