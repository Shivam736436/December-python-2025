"""
=====================================
PYTHON OPERATORS – COMPLETE GUIDE
=====================================
Operators are symbols that perform
operations on variables and values.
"""

# -------------------------------------
# 1. ARITHMETIC OPERATORS
# -------------------------------------
a = 10
b = 3

print("Addition:", a + b)               # +
print("Subtraction:", a - b)            # -
print("Multiplication:", a * b)         # *
print("Division:", a / b)               # /
print("Modulus:", a % b)                # %
print("Exponent:", a ** b)              # **
"""
=====================================
PYTHON OPERATORS – COMPLETE GUIDE
=====================================
Operators are symbols that perform
operations on variables and values.
"""

# -------------------------------------
# 1. ARITHMETIC OPERATORS
# -------------------------------------
a = 10
b = 3

print("Addition:", a + b)        # +
print("Subtraction:", a - b)     # -
print("Multiplication:", a * b)  # *
print("Division:", a / b)        # /
print("Modulus:", a % b)         # %
print("Exponent:", a ** b)       # **
print("Floor Division:", a // b) # //

# -------------------------------------
# 2. COMPARISON (RELATIONAL) OPERATORS
# -------------------------------------
x = 5
y = 10

print(x == y)           # Equal
print(x != y)           # Not equal
print(x > y)            # Greater than
print(x < y)            # Less than
print(x >= y)           # Greater or equal
print(x <= y)           # Less or equal

# -------------------------------------
# 3. ASSIGNMENT OPERATORS
# -------------------------------------
n = 5
n += 3    # n = n + 3
print(n)

n -= 2
print(n)

n *= 2
print(n)

n /= 2
print(n)

n %= 3
print(n)

n **= 2
print(n)

n //= 2
print(n)

# -------------------------------------
# 4. LOGICAL OPERATORS
# -------------------------------------
a = True
b = False

print(a and b)   # AND                  # both must be true
print(a or b)    # OR                   # atleast one must be true
print(not a)     # NOT                  # true become false or false become true

# -------------------------------------
# 5. BITWISE OPERATORS
# -------------------------------------
x = 5    # 101
y = 3    # 011

print(x & y)   # AND
print(x | y)   # OR
print(x ^ y)   # XOR
print(~x)      # NOT
print(x << 1)  # Left shift
print(x >> 1)  # Right shift

# -------------------------------------
# 6. MEMBERSHIP OPERATORS
# -------------------------------------
text = "Python"
numbers = [1, 2, 3, 4]

print("P" in text)
print("Java" not in text)
print(2 in numbers)
print(5 not in numbers)

# -------------------------------------
# 7. IDENTITY OPERATORS

# They are used to check whether two variables refer to the same object in memory — not whether their values are equal.

# is checks object identity (same memory location)
# is not checks different object identity
# -------------------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # Same memory
print(a is c)       # Different memory
print(a == c)       # Same values

print(a is not c)

# -------------------------------------
# 8. OPERATOR PRECEDENCE
# -------------------------------------
result = 10 + 5 * 2
print(result)       # Multiplication first

result = (10 + 5) * 2
print(result)

# -------------------------------------
# 9. TERNARY OPERATOR

# used to write an if–else statement in one line.

# value_if_true if condition else value_if_false

# -------------------------------------
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

# -------------------------------------
# 10. UNARY OPERATORS
# -------------------------------------
x = 5
print(+x)
print(-x)

# -------------------------------------
# 11. STRING OPERATORS
# -------------------------------------
s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)  # Concatenation
print(s1 * 3)         # Repetition

# -------------------------------------
# 12. LIST OPERATORS
# -------------------------------------
l1 = [1, 2]
l2 = [3, 4]

print(l1 + l2)    # Concatenation
print(l1 * 2)     # Repetition

# -------------------------------------
# END OF OPERATORS GUIDE
# -------------------------------------
      # //

# -------------------------------------
# 2. COMPARISON (RELATIONAL) OPERATORS
# -------------------------------------
x = 5
y = 10

print(x == y)   # Equal
print(x != y)   # Not equal
print(x > y)    # Greater than
print(x < y)    # Less than
print(x >= y)   # Greater or equal
print(x <= y)   # Less or equal

# -------------------------------------
# 3. ASSIGNMENT OPERATORS
# -------------------------------------
n = 5
n += 3    # n = n + 3
print(n)

n -= 2
print(n)

n *= 2
print(n)

n /= 2
print(n)

n %= 3
print(n)

n **= 2
print(n)

n //= 2
print(n)

# -------------------------------------
# 4. LOGICAL OPERATORS
# -------------------------------------
a = True
b = False

print(a and b)   # AND
print(a or b)    # OR
print(not a)     # NOT

# -------------------------------------
# 5. BITWISE OPERATORS
# -------------------------------------
x = 5    # 101
y = 3    # 011

print(x & y)   # AND
print(x | y)   # OR
print(x ^ y)   # XOR
print(~x)      # NOT
print(x << 1)  # Left shift
print(x >> 1)  # Right shift

# -------------------------------------
# 6. MEMBERSHIP OPERATORS
# -------------------------------------
text = "Python"
numbers = [1, 2, 3, 4]

print("P" in text)
print("Java" not in text)
print(2 in numbers)
print(5 not in numbers)

# -------------------------------------
# 7. IDENTITY OPERATORS
# -------------------------------------
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)       # Same memory
print(a is c)       # Different memory
print(a == c)       # Same values

print(a is not c)

# -------------------------------------
# 8. OPERATOR PRECEDENCE
# -------------------------------------
result = 10 + 5 * 2
print(result)       # Multiplication first

result = (10 + 5) * 2
print(result)

# -------------------------------------
# 9. TERNARY OPERATOR
# -------------------------------------
age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)

# -------------------------------------
# 10. UNARY OPERATORS
# -------------------------------------
x = 5
print(+x)
print(-x)

# -------------------------------------
# 11. STRING OPERATORS
# -------------------------------------
s1 = "Hello"
s2 = "Python"

print(s1 + " " + s2)  # Concatenation
print(s1 * 3)         # Repetition

# -------------------------------------
# 12. LIST OPERATORS
# -------------------------------------
l1 = [1, 2]
l2 = [3, 4]

print(l1 + l2)    # Concatenation
print(l1 * 2)     # Repetition

# -------------------------------------
# END OF OPERATORS GUIDE
# -------------------------------------
