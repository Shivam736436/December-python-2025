# -----------------------------------------
# 1. Importing standard modules
# -----------------------------------------
import math
import random
import datetime
import os
import sys

print("math.sqrt(16):", math.sqrt(16))       # square root
print("math.factorial(5):", math.factorial(5))
print("math.pi:", math.pi)

# -----------------------------------------
# 2. Random module
# -----------------------------------------
print("Random number 0-9:", random.randint(0, 9))
print("Random choice from list:", random.choice([1, 2, 3, 4, 5]))
print("Shuffle list:")
lst = [1, 2, 3, 4, 5]
random.shuffle(lst)
print(lst)
print("\n")

# -----------------------------------------
# 3. datetime module
# -----------------------------------------
now = datetime.datetime.now()
print("Current date and time:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)
today = datetime.date.today()
print("Today's date:", today)
print("\n")

# -----------------------------------------
# 4. os module
# -----------------------------------------
print("Current working directory:", os.getcwd())
print("List files & folders in current directory:", os.listdir())
# os.mkdir("test_folder")   # create folder
# os.rmdir("test_folder")   # remove folder
print("\n")

# -----------------------------------------
# 5. sys module
# -----------------------------------------
print("Python version:", sys.version)
print("Python path:", sys.path)
print("\n")

# -----------------------------------------
# 6. Import specific functions
# -----------------------------------------
from math import sqrt, pow
print("Square root of 25:", sqrt(25))
print("2 to the power 3:", pow(2,3))
print("\n")

# -----------------------------------------
# 7. Using alias
# -----------------------------------------
import math as m
print("math.pi using alias:", m.pi)
print("\n")

# -----------------------------------------
# 8. Creating your own module
# -----------------------------------------
# Suppose we have a file mymodule.py with:
# def greet(name):
#     print(f"Hello, {name}!")
# Then we can import it:

# import mymodule
# mymodule.greet("Ali")

# OR
# from mymodule import greet
# greet("Ali")

# (You need to create mymodule.py separately)

# -----------------------------------------
# 9. dir() function
# -----------------------------------------
print("All functions in math module:", dir(math))

# -----------------------------------------
# 10. pip (external modules)
# -----------------------------------------
# !pip install requests  # Install external module (run in terminal)
# import requests
# response = requests.get("https://api.github.com")
# print("Status code:", response.status_code)
