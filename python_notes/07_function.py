# -----------------------------------------
# 1. Simple Function (No input, no return)
# -----------------------------------------
def greet():
    print("Hello, brother!")
    
greet()
print("\n")

# -----------------------------------------
# 2. Function with parameters (input)
# -----------------------------------------
def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Ali")
print("\n")

# -----------------------------------------
# 3. Function with return value
# -----------------------------------------
def add(a, b):
    return a + b

result = add(5, 3)
print("Sum:", result)
print("\n")

# -----------------------------------------
# 4. Default parameters
# -----------------------------------------
def greet_person(name="Friend"):
    print(f"Hello, {name}!")

greet_person()
greet_person("Sara")
print("\n")

# -----------------------------------------
# 5. Keyword arguments
# -----------------------------------------
def info(name, age):
    print(f"Name: {name}, Age: {age}")

info(age=25, name="Ali")
print("\n")

# -----------------------------------------
# 6. Arbitrary arguments (*args)
# -----------------------------------------
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum of numbers:", add_numbers(1, 2, 3, 4))
print("\n")

# -----------------------------------------
# 7. Arbitrary keyword arguments (**kwargs)
# -----------------------------------------
def student_info(**kwargs):
    for k, v in kwargs.items():
        print(k, "=", v)

student_info(name="Ali", age=20, city="Delhi")
print("\n")

# -----------------------------------------
# 8. Nested Function
# -----------------------------------------
def outer():
    print("This is outer function")
    def inner():
        print("This is inner function")
    inner()

outer()
print("\n")

# -----------------------------------------
# 9. Lambda Function (Anonymous function)
# -----------------------------------------
square = lambda x: x*x
print("Square of 5:", square(5))

sum_two = lambda a, b: a + b
print("Sum of 4 and 6:", sum_two(4,6))
print("\n")

# -----------------------------------------
# 10. Function with list as input
# -----------------------------------------
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [1,2,3,4,5]
print("Sum of list:", sum_list(nums))
print("\n")

# -----------------------------------------
# 11. Function returning multiple values
# -----------------------------------------
def get_name_age():
    return "Ali", 20

name, age = get_name_age()
print("Name:", name, "Age:", age)
print("\n")

# -----------------------------------------
# 12. Recursion (Function calling itself)
# -----------------------------------------
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print("Factorial of 5:", factorial(5))
print("\n")

# -----------------------------------------
# 13. Docstring (Documentation)
# -----------------------------------------
def multiply(a, b):
    """This function multiplies two numbers"""
    return a * b

print(multiply(4,5))
print("Docstring:", multiply.__doc__)
