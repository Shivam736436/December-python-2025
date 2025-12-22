# =================================================
# PYTHON FUNCTIONS — COMPLETE EXPLANATION BY CODE
# =================================================

# -------------------------
# 1. BASIC FUNCTION
# -------------------------
def say_hello():
    # No parameters
    # No return value
    print("Hello!")

say_hello()  # calling the function


# -------------------------
# 2. FUNCTION WITH PARAMETERS
# -------------------------
def greet(name):
    # 'name' is a parameter
    print("Hello", name)

greet("Alex")
greet("Sam")


# -------------------------
# 3. FUNCTION WITH RETURN
# -------------------------
def add(a, b):
    # return sends a value back to the caller
    return a + b

result = add(3, 5)
print("Result:", result)


# -------------------------
# 4. PRINT vs RETURN
# -------------------------
def wrong_add(a, b):
    print(a + b)  # prints but returns NOTHING

def correct_add(a, b):
    return a + b  # returns value

x = wrong_add(2, 3)
print(x)  # None

y = correct_add(2, 3)
print(y)  # 5


# -------------------------
# 5. DEFAULT PARAMETERS
# -------------------------
def introduce(name="Guest"):
    print("Hello", name)

introduce()
introduce("Alex")


# -------------------------
# 6. KEYWORD ARGUMENTS
# -------------------------
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info(age=20, name="Alex")


# -------------------------
# 7. *args (MULTIPLE VALUES)
# -------------------------
def add_numbers(*numbers):
    # *numbers becomes a tuple
    total = 0
    for num in numbers:
        total += num
    return total

print(add_numbers(1, 2, 3))
print(add_numbers(5, 10, 15, 20))


# -------------------------
# 8. **kwargs (KEY-VALUE PAIRS)
# -------------------------
def print_details(**details):
    # **details becomes a dictionary
    for key, value in details.items():
        print(key, ":", value)

print_details(name="Alex", age=20, country="India")


# -------------------------
# 9. FUNCTION INSIDE FUNCTION
# -------------------------
def outer():
    def inner():
        print("Inner function")
    inner()

outer()


# -------------------------
# 10. VARIABLE SCOPE
# -------------------------
x = 10  # global variable

def show_scope():
    x = 5  # local variable
    print("Inside function:", x)

show_scope()
print("Outside function:", x)


# -------------------------
# 11. RETURN MULTIPLE VALUES
# -------------------------
def calculate(a, b):
    return a + b, a - b, a * b

sum_, diff, prod = calculate(10, 5)
print(sum_, diff, prod)


# -------------------------
# 12. LAMBDA FUNCTION
# -------------------------
# Short, one-line function
square = lambda x: x * x
print(square(4))

# another example
is_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(is_even(4))  # Even
print(is_even(5))  # Odd

#filter --> Keep only items that match condition.

# -------------------------
# 13. DOCSTRING
# -------------------------
def multiply(a, b):
    """
    This function multiplies two numbers
    """
    return a * b

print(multiply.__doc__)


# -------------------------
# 14. PASS KEYWORD
# -------------------------
def future_function():
    # pass means "do nothing for now"
    pass


# -------------------------
# 15. RECURSION
# -------------------------
def factorial(n):
    # Function calling itself
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


# -------------------------
# END
# -------------------------
print("All function concepts covered 🚀")
