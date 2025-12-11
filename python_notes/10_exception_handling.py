# -----------------------------------------
# 1. Basic try-except
# -----------------------------------------
try:
    x = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
print("\n")

# -----------------------------------------
# 2. Handling multiple exceptions
# -----------------------------------------
try:
    num = int("abc")
except ValueError:
    print("ValueError: invalid literal for int()")
except ZeroDivisionError:
    print("Cannot divide by zero")
print("\n")

# -----------------------------------------
# 3. Using else (runs if no exception)
# -----------------------------------------
try:
    x = 10 / 2
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Division successful, result:", x)
print("\n")

# -----------------------------------------
# 4. Using finally (always runs)
# -----------------------------------------
try:
    f = open("test.txt", "r")
except FileNotFoundError:
    print("File not found")
finally:
    print("This block runs always")
print("\n")

# -----------------------------------------
# 5. Raising custom exceptions
# -----------------------------------------
age = -5
try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print("Error:", e)
print("\n")

# -----------------------------------------
# 6. Catch all exceptions (not recommended)
# -----------------------------------------
try:
    x = 10 / 0
except Exception as e:
    print("Some error occurred:", e)
print("\n")

# -----------------------------------------
# 7. Nested try-except
# -----------------------------------------
try:
    num = int("abc")
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Inner: Cannot divide by zero")
except ValueError:
    print("Outer: Invalid input")
print("\n")

# -----------------------------------------
# 8. Assertions
# -----------------------------------------
x = 5
try:
    assert x > 10, "x is not greater than 10"
except AssertionError as e:
    print("AssertionError:", e)
print("\n")

# -----------------------------------------
# 9. Finally with return (demonstration)
# -----------------------------------------
def test_finally():
    try:
        return 10 / 2
    except ZeroDivisionError:
        return 0
    finally:
        print("Finally block always runs")
        # Even if we return from try, finally runs

result = test_finally()
print("Result:", result)
