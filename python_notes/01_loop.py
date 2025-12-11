# -----------------------------------------
# 1. FOR LOOP with range()
# -----------------------------------------
print("1. For loop with range():")
for i in range(5):
    print(i, end=" ")
print("\n")

# -----------------------------------------
# 2. FOR LOOP with list
# -----------------------------------------
fruits = ["apple", "banana", "mango"]
print("2. For loop with list:")
for f in fruits:
    print(f, end=" ")
print("\n")

# -----------------------------------------
# 3. FOR LOOP with string
# -----------------------------------------
s = "Python"
print("3. For loop with string:")
for ch in s:
    print(ch, end=" ")
print("\n")

# -----------------------------------------
# 4. FOR LOOP with tuple
# -----------------------------------------
t = (10, 20, 30)
print("4. For loop with tuple:")
for x in t:
    print(x, end=" ")
print("\n")

# -----------------------------------------
# 5. FOR LOOP with set
# -----------------------------------------
st = {1, 2, 3}
print("5. For loop with set:")
for x in st:
    print(x, end=" ")
print("\n")

# -----------------------------------------
# 6. FOR LOOP with dictionary
# -----------------------------------------
d = {"name": "Ali", "age": 20}
print("6. For loop with dictionary (keys):")
for k in d:
    print(k, end=" ")
print("\n")

print("For loop with dictionary (values):")
for v in d.values():
    print(v, end=" ")
print("\n")

print("For loop with dictionary (key, value):")
for k, v in d.items():
    print(k, "=", v)
print("\n")

# -----------------------------------------
# 7. WHILE LOOP
# -----------------------------------------
print("7. While loop:")
i = 1
while i <= 5:
    print(i, end=" ")
    i += 1
print("\n")

# -----------------------------------------
# 8. WHILE LOOP with else
# -----------------------------------------
print("8. While loop with else:")
i = 1
while i <= 3:
    print(i, end=" ")
    i += 1
else:
    print("\nLoop finished normally")
print("\n")

# -----------------------------------------
# 9. FOR LOOP with else
# -----------------------------------------
print("9. For loop with else:")
for i in range(3):
    print(i, end=" ")
else:
    print("\nFor loop finished normally")
print("\n")

# -----------------------------------------
# 10. Nested loops
# -----------------------------------------
print("10. Nested loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i={i}, j={j}")
print("\n")

# -----------------------------------------
# 11. Loop control statements
# -----------------------------------------
print("11. Break in loop:")
for i in range(5):
    if i == 3:
        break
    print(i, end=" ")
print("\n")

print("12. Continue in loop:")
for i in range(5):
    if i == 3:
        continue
    print(i, end=" ")
print("\n")

print("13. Pass in loop (does nothing):")
for i in range(3):
    pass
print("Done with pass\n")
