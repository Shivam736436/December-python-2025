# string --> A string is a sequence of characters enclosed in quotes.Strings are immutable — you cannot change characters directly.

#  create string
s1 = "Hello"
s2 = 'Hello'
s3 = """Hello
World"""   # multi-line string



# . Accessing Characters
text = "Python"
print(text[0])   # P
print(text[-1])  # n




# slicing string
text = "Python"
print(text[1:4])  # yth
print(text[:3])   # Pyt
print(text[3:])   # hon



# concatenation 
a = "Hello"
b = "World"
print(a + " " + b)  # Hello World



# repeating string 
print("Hi" * 3)  # HiHiHi




# string methode
s = "  python programming  "

print(s.upper())       # PYTHON PROGRAMMING
print(s.lower())       # python programming
print(s.title())       # Python Programming
print(s.strip())       # python programming
print(s.replace("python", "java"))  # java programming
print(s.split())       # ['python', 'programming']


    # Method              	Purpose
    # upper()             	Uppercase
    # lower()             	Lowercase
    # strip()             	Remove spaces
    # replace()           	Replace text
    # split()             	Split into list
    # join()                 	Join items
    # find()              	Find index
    # count()                 Count occurrences



# string formating
name = "John"
age = 25
print(f"My name is {name}, I am {age}")


# check content
text = "Hello123"

print(text.isalpha())  # False (letters only?)
print(text.isdigit())  # False (digits only?)
print(text.isalnum())  # True (letters + digits)




# . Iterating Over Strings
for ch in "abc":
    print(ch)



# . Immutability --> You cannot change characters directly:
text = "Hello"
text[0] = "J"   # ❌ Error



# But you can create a new string:
text = "J" + text[1:]



# 🟢 Summary

# Strings are ordered, immutable sequences.
# Support indexing, slicing, concatenation, repetition.
# Built-in methods: upper, lower, strip, replace, split, etc.
# Best formatting: f-strings.

