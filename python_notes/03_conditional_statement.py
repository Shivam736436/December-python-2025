"""
=========================================
PYTHON CONDITIONAL STATEMENTS – FULL GUIDE
=========================================
Conditional statements are used to
make decisions based on conditions.
"""

# -----------------------------------------
# 1. IF STATEMENT
# -----------------------------------------
age = 20

if age >= 18:
    print("You are an adult")

# -----------------------------------------
# 2. IF–ELSE STATEMENT
# -----------------------------------------
number = 5

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# -----------------------------------------
# 3. IF–ELIF–ELSE STATEMENT
# -----------------------------------------
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")

# -----------------------------------------
# 4. NESTED IF STATEMENT
# -----------------------------------------
username = "admin"
password = "1234"

if username == "admin":
    if password == "1234":
        print("Login successful")
    else:
        print("Wrong password")
else:
    print("Wrong username")

# -----------------------------------------
# 5. LOGICAL OPERATORS IN CONDITIONS
# -----------------------------------------
age = 25
citizen = True

if age >= 18 and citizen:
    print("Eligible to vote")

# -----------------------------------------
# 6. COMPARISON OPERATORS
# -----------------------------------------
a = 10
b = 20

if a < b:
    print("a is smaller")

# -----------------------------------------
# 7. MEMBERSHIP OPERATORS
# -----------------------------------------
text = "Python"

if "P" in text:
    print("P is present")

# -----------------------------------------
# 8. IDENTITY OPERATORS
# -----------------------------------------
x = None

if x is None:
    print("No value")

# -----------------------------------------
# 9. TERNARY CONDITIONAL OPERATOR
# -----------------------------------------
age = 17
status = "Adult" if age >= 18 else "Minor"
print(status)

# -----------------------------------------
# 10. MULTIPLE CONDITIONS
# -----------------------------------------
num = 15

if num > 0:
    if num % 3 == 0:
        print("Positive and divisible by 3")

# -----------------------------------------
# 11. PASS STATEMENT
# -----------------------------------------
# Used when a statement is required syntactically
# but no action is needed

x = 10
if x > 5:
    pass

# -----------------------------------------
# 12. TRUTHY & FALSY VALUES
# -----------------------------------------
# False values: 0, None, "", [], {}, set()

value = ""

if value:
    print("Truthy")
else:
    print("Falsy")

# -----------------------------------------
# 13. SHORT-CIRCUIT BEHAVIOR
# -----------------------------------------
a = 0
b = 10

if a != 0 and b / a > 2:
    print("This won't run")

# -----------------------------------------
# 14. INPUT WITH CONDITION
# -----------------------------------------
# Uncomment to test
# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# -----------------------------------------
# END OF CONDITIONAL STATEMENTS
# -----------------------------------------
