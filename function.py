# function --> A function lets you group code, give it a name, and run it whenever you need—without repeating the code

# 🔹 Why use functions?

# Avoid repeating code
# Make programs organized
# Make code easier to test and maintain
# Break big problems into smaller parts

# 🔹 How to define a function

# You use the def keyword:

# def function_name(parameters):
#     # code block
#     return result

def square(num):
    return num * num

result = square(5)
print(result)   # Output: 25


# tyoe of function 

# 1. built in function
# 2. user define function
# 3. function with parameter
# 4. function with default parameter
# 5. function return value
# 6. lambda function

#  built in function 
# print(), len(), type(), sum()

# B. User-defined Functions

# You create these yourself using def.

def greet():
    print("Hello!")

# Functions with Default Parameters

# Useful when you want optional values.
def greet(name="friend"):
    print("Hello,", name)

# Lambda (Anonymous) Functions

# Small one-line functions.

square = lambda x: x * x
print(square(4))

# 🔹 3. Scope of Variables

# 1. local scope      // access on inside a function
# 2. global scope     // access everywhere