"""
==================================================
PYTHON MODULES — COMPLETE EXPLANATION IN ONE FILE
==================================================

A MODULE in Python is simply a file that contains:
- variables
- functions
- classes
- executable code

Even THIS file is a module.
"""

# -----------------------------------------------
# 1. BUILT-IN MODULES
# -----------------------------------------------
# Python already comes with many modules

import math        # math-related functions
import random      # random numbers
import datetime    # date & time

print(math.sqrt(16))              # square root
print(random.randint(1, 6))       # random number
print(datetime.datetime.now())    # current date & time


# -----------------------------------------------
# 2. IMPORTING WITH ALIAS
# -----------------------------------------------
# Alias = short name

import math as m

print(m.pi)
print(m.pow(2, 3))


# -----------------------------------------------
# 3. IMPORTING SPECIFIC ITEMS
# -----------------------------------------------
from math import sqrt, pi

print(sqrt(25))
print(pi)


# -----------------------------------------------
# 4. WHAT IS __name__ ?
# -----------------------------------------------
# Every module has a built-in variable called __name__

print("Module name:", __name__)

# If this file is run directly:
# __name__ == "__main__"
# If imported:
# __name__ == module_name


# -----------------------------------------------
# 5. __main__ CHECK
# -----------------------------------------------
# Prevents code from running when imported

if __name__ == "__main__":
    print("This file is running directly")


# -----------------------------------------------
# 6. CREATING OUR OWN MODULE (SIMULATION)
# -----------------------------------------------
# Imagine this code is inside a file called mymodule.py

def greet(name):
    """Returns a greeting"""
    return f"Hello, {name}"

pi_value = 3.14159

# If this file were named mymodule.py, we could do:
# import mymodule
# mymodule.greet("Alex")


# -----------------------------------------------
# 7. USING dir() TO EXPLORE MODULES
# -----------------------------------------------
print(dir(math))   # shows everything inside math module


# -----------------------------------------------
# 8. USING help() FOR DOCUMENTATION
# -----------------------------------------------
help(math.sqrt)


# -----------------------------------------------
# 9. MODULE SEARCH PATH
# -----------------------------------------------
# Python searches modules in these locations

import sys
print(sys.path)


# -----------------------------------------------
# 10. EXTERNAL MODULES (INSTALLED VIA pip)
# -----------------------------------------------
"""
Example (not executed here):

pip install requests

import requests
response = requests.get("https://example.com")
print(response.status_code)
"""


# -----------------------------------------------
# 11. PACKAGE EXPLANATION (THEORY)
# -----------------------------------------------
"""
A PACKAGE is a folder containing modules.

Example:
my_package/
│
├── __init__.py
├── module1.py
└── module2.py

Used as:
from my_package import module1
"""


# -----------------------------------------------
# 12. WHY MODULES ARE IMPORTANT
# -----------------------------------------------
"""
- Organize code
- Reuse code
- Avoid duplication
- Make projects readable
- Enable teamwork
"""


# -----------------------------------------------
# END
# -----------------------------------------------
print("All module concepts explained ✅")
