# -----------------------------------------
# 1. Creating tuples
# -----------------------------------------
t1 = (10, 20, 30)
t2 = ("apple", "banana", "mango")
t3 = (10, "hello", 3.14, True)
print("t1:", t1)
print("t2:", t2)
print("t3:", t3)
print("\n")

# -----------------------------------------
# 2. Single element tuple
# -----------------------------------------
t4 = (5,)  # Note the comma
print("Single element tuple:", t4)
print("\n")

# -----------------------------------------
# 3. Accessing elements (indexing)
# -----------------------------------------
print("First element of t2:", t2[0])
print("Last element of t2:", t2[-1])
print("\n")

# -----------------------------------------
# 4. Slicing
# -----------------------------------------
print("t2[0:2]:", t2[0:2])
print("t2[1:]:", t2[1:])
print("t2[-2:]:", t2[-2:])
print("\n")

# -----------------------------------------
# 5. Looping through a tuple
# -----------------------------------------
print("Looping through t1:")
for x in t1:
    print(x, end=" ")
print("\n")

# -----------------------------------------
# 6. Tuple methods
# -----------------------------------------
t5 = (1, 2, 2, 3, 4, 2)
print("t5:", t5)
print("Count of 2:", t5.count(2))
print("Index of 3:", t5.index(3))
print("\n")

# -----------------------------------------
# 7. Tuple unpacking
# -----------------------------------------
t6 = ("Ali", 20, "India")
name, age, country = t6
print("Name:", name)
print("Age:", age)
print("Country:", country)
print("\n")

# -----------------------------------------
# 8. Nested tuple
# -----------------------------------------
nested = ((1, 2), (3, 4), (5, 6))
print("Nested tuple:", nested)
print("Element nested[1][1]:", nested[1][1])
print("\n")

# -----------------------------------------
# 9. Tuple immutability
# -----------------------------------------
t7 = (1, 2, 3)
# t7[0] = 100  # ❌ Error: cannot change
# Instead, create a new tuple
t7 = (100,) + t7[1:]
print("Modified tuple:", t7)
print("\n")

# -----------------------------------------
# 10. Converting list to tuple
# -----------------------------------------
lst = [1, 2, 3]
t8 = tuple(lst)
print("List to tuple:", t8)

# -----------------------------------------
# 11. Membership test
# -----------------------------------------
print("Is 2 in t8?", 2 in t8)
print("Is 5 not in t8?", 5 not in t8)
