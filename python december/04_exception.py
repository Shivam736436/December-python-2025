"""
==================================================
PYTHON EXCEPTIONS — COMPLETE EXPLANATION
==================================================

An EXCEPTION is an error that occurs while a program
is running and stops normal execution.

Python lets us HANDLE exceptions so the program
does not crash.
"""

# -----------------------------------------------
# 1. COMMON EXCEPTIONS
# -----------------------------------------------
"""
ZeroDivisionError
TypeError
ValueError
IndexError
KeyError
FileNotFoundError
ImportError
"""

# Example (commented to avoid crash)
# print(10 / 0)


# -----------------------------------------------
# 2. BASIC TRY - EXCEPT
# -----------------------------------------------
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")


# -----------------------------------------------
# 3. HANDLING MULTIPLE EXCEPTIONS
# -----------------------------------------------
try:
    num = int("abc")
except ValueError:
    print("ValueError: Invalid number")
except ZeroDivisionError:
    print("ZeroDivisionError occurred")


# -----------------------------------------------
# 4. MULTIPLE EXCEPTIONS TOGETHER
# -----------------------------------------------
try:
    a = int("abc")
except (ValueError, TypeError):
    print("Value or Type error occurred")


# -----------------------------------------------
# 5. GENERIC EXCEPTION
# -----------------------------------------------
try:
    print(x)
except Exception as e:
    print("Error:", e)


# -----------------------------------------------
# 6. ELSE BLOCK
# -----------------------------------------------
# Runs only if NO exception occurs
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error")
else:
    print("Success:", result)


# -----------------------------------------------
# 7. FINALLY BLOCK
# -----------------------------------------------
# Always executes (cleanup code)
try:
    file = open("test.txt", "w")
    file.write("Hello")
except Exception as e:
    print("Error:", e)
finally:
    file.close()
    print("File closed")


# -----------------------------------------------
# 8. REAL EXAMPLE: USER INPUT
# -----------------------------------------------
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Please enter a valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")


# -----------------------------------------------
# 9. FILE HANDLING WITH EXCEPTION
# -----------------------------------------------
try:
    file = open("missing.txt", "r")
except FileNotFoundError:
    print("File not found")


# -----------------------------------------------
# 10. RAISING EXCEPTIONS
# -----------------------------------------------
def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Access granted"

try:
    print(check_age(15))
except ValueError as e:
    print(e)


# -----------------------------------------------
# 11. CUSTOM EXCEPTION
# -----------------------------------------------
class NegativeNumberError(Exception):
    pass

def check_number(n):
    if n < 0:
        raise NegativeNumberError("Negative numbers not allowed")
    return n

try:
    check_number(-5)
except NegativeNumberError as e:
    print(e)


# -----------------------------------------------
# 12. ASSERTION
# -----------------------------------------------
# Used mainly for debugging
x = 10
assert x > 0, "x must be positive"


# -----------------------------------------------
# 13. TRY INSIDE FUNCTION
# -----------------------------------------------
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 2))
print(divide(10, 0))


# -----------------------------------------------
# 14. BEST PRACTICES
# -----------------------------------------------
"""
✔ Catch specific exceptions
✔ Use finally for cleanup
✔ Don't hide errors with bare except
✔ Use custom exceptions when needed
✔ Exceptions are for errors, not logic
"""


# -----------------------------------------------
# END
# -----------------------------------------------
print("All exception concepts explained ✅")
