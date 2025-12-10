# global scope
a = "shivam"

# basic function
def greet():
    print("welcome",a,"have a great day brother")               # using global variable

#  function with parameter
def add(b,c):
    return b+c

# default parameter
def welcome(name = "archana"):
    print("hello",name)

# *argu ( unlimited position argument)
def total_sum(*num):
    return sum(num)

# *kwargs ( unlimited keyword argument)
def user_info(**details):
    print("User Details:")
    for key, value in details.items():
        print(key, "=", value)

# ---------- MULTIPLE RETURN VALUES ----------
def calculate(a, b):
    return a + b, a - b, a * b  # returns 3 values

# ---------- LAMBDA FUNCTION ----------
square = lambda x: x * x


# ---------- LOCAL SCOPE EXAMPLE ----------
def scope_example():
    x = "local variable"
    print("Inside function:", x)


# ---------- MAIN EXECUTION ----------
greet()

print("\nAdd:", add(5, 3))

welcome()
welcome("Aisha")

print("\nTotal sum:", total_sum(1, 2, 3, 4, 5))

user_info(name="Ali", age=20, country="UAE")

add_val, sub_val, mul_val = calculate(10, 5)
print("\nMultiple returns:", add_val, sub_val, mul_val)

print("\nSquare using lambda:", square(6))

scope_example()