"""
=========================
PYTHON STRING TUTORIAL
=========================

A string is a sequence of characters.
In Python, strings are IMMUTABLE (cannot be changed after creation).
"""

# --------------------------------------------------
# 1. CREATING STRINGS
# --------------------------------------------------

s1 = "Hello"
s2 = 'World'
s3 = """This is
a multi-line
string"""

print(s1)
print(s2)
print(s3)

# --------------------------------------------------
# 2. STRING DATA TYPE
# --------------------------------------------------

print(type(s1))  # <class 'str'>

# --------------------------------------------------
# 3. STRING LENGTH
# --------------------------------------------------

print(len(s1))  # Number of characters

# --------------------------------------------------
# 4. STRING INDEXING
# --------------------------------------------------
# Index starts from 0
# Negative index starts from -1 (end)

s = "Python"

print(s[0])    # P
print(s[3])    # h
print(s[-1])   # n
print(s[-2])   # o

# --------------------------------------------------
# 5. STRING SLICING
# --------------------------------------------------

print(s[0:4])   # Pyth
print(s[:3])    # Pyt
print(s[2:])    # thon
print(s[::-1])  # Reverse string

# --------------------------------------------------
# 6. STRING IMMUTABILITY
# --------------------------------------------------

# s[0] = "J"   ❌ ERROR: Strings cannot be modified

# Correct way:
s = "J" + s[1:]
print(s)

# --------------------------------------------------
# 7. STRING CONCATENATION
# --------------------------------------------------

a = "Hello"
b = "Python"

print(a + " " + b)
print(a * 3)  # Repetition

# --------------------------------------------------
# 8. STRING MEMBERSHIP
# --------------------------------------------------

print("Py" in s)
print("Java" not in s)

# --------------------------------------------------
# 9. COMMON STRING METHODS
# --------------------------------------------------

text = "  hello python  "

print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.strip())
print(text.replace("python", "world"))
print(text.find("python"))
print(text.count("o"))

# --------------------------------------------------
# 10. CHECK STRING CONTENT
# --------------------------------------------------

s = "Python123"

print(s.isalpha())   # False
print(s.isdigit())   # False
print(s.isalnum())   # True
print(s.startswith("Py"))
print(s.endswith("123"))

# --------------------------------------------------
# 11. STRING SPLIT & JOIN
# --------------------------------------------------

sentence = "Python is very powerful"

words = sentence.split()
print(words)

new_sentence = "-".join(words)
print(new_sentence)

# --------------------------------------------------
# 12. STRING FORMATTING
# --------------------------------------------------

name = "Alice"
age = 25

# Old style
print("Name: %s Age: %d" % (name, age))

# format() method
print("Name: {} Age: {}".format(name, age))

# f-string (BEST)
print(f"Name: {name} Age: {age}")

# --------------------------------------------------
# 13. ESCAPE CHARACTERS
# --------------------------------------------------

print("Hello\nWorld")   # New line
print("Hello\tWorld")   # Tab
print("He said \"Hi\"")

# --------------------------------------------------
# 14. RAW STRINGS
# --------------------------------------------------

path = r"C:\new\folder\test"
print(path)

# --------------------------------------------------
# 15. STRING COMPARISON
# --------------------------------------------------

print("apple" == "apple")
print("apple" < "banana")

# --------------------------------------------------
# 16. LOOPING THROUGH STRING
# --------------------------------------------------

for char in "Python":
    print(char)

# --------------------------------------------------
# 17. STRING ENCODING & DECODING
# --------------------------------------------------

text = "hello"

encoded = text.encode("utf-8")
print(encoded)

decoded = encoded.decode("utf-8")
print(decoded)

# --------------------------------------------------
# 18. PERFORMANCE TIP (JOIN VS +)
# --------------------------------------------------

words = ["Python", "is", "fast"]

# ❌ Slow
result = ""
for w in words:
    result += w + " "
print(result)

# ✅ Fast
print(" ".join(words))

# --------------------------------------------------
# 19. STRING CONSTANTS
# --------------------------------------------------

import string

print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

# --------------------------------------------------
# 20. IMPORTANT TAKEAWAYS
# --------------------------------------------------
"""
✔ Strings are immutable
✔ Indexing & slicing are powerful
✔ Use f-strings for formatting
✔ Use join() for performance
✔ Many built-in methods available
"""
