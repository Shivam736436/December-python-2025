# -----------------------------------------
# 1. Creating lists
# -----------------------------------------
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "mango"]
mixed = [10, "hello", 3.14, True]
print("Numbers:", numbers)
print("Fruits:", fruits)
print("Mixed:", mixed)
print("\n")

# -----------------------------------------
# 2. Accessing elements (indexing)
# -----------------------------------------
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])
print("\n")

# -----------------------------------------
# 3. Slicing
# -----------------------------------------
print("Numbers 1 to 3:", numbers[0:3])
print("From 2nd element to end:", numbers[1:])
print("Last 3 elements:", numbers[-3:])
print("\n")

# -----------------------------------------
# 4. Updating elements
# -----------------------------------------
fruits[1] = "grapes"
print("Updated fruits:", fruits)
print("\n")

# -----------------------------------------
# 5. Adding elements
# -----------------------------------------
fruits.append("orange")
print("After append:", fruits)

fruits.insert(1, "kiwi")
print("After insert at index 1:", fruits)

fruits.extend(["papaya", "melon"])
print("After extend:", fruits)
print("\n")

# -----------------------------------------
# 6. Removing elements
# -----------------------------------------
fruits.remove("apple")
print("After remove('apple'):", fruits)

fruits.pop()  # remove last
print("After pop():", fruits)

fruits.pop(1)  # remove index 1
print("After pop(1):", fruits)

del fruits[0]
print("After del fruits[0]:", fruits)

fruits.clear()
print("After clear():", fruits)
print("\n")

# -----------------------------------------
# 7. List methods
# -----------------------------------------
numbers = [5, 2, 8, 3, 2]
print("Numbers:", numbers)
numbers.sort()
print("Sorted:", numbers)
numbers.sort(reverse=True)
print("Sorted descending:", numbers)
numbers.reverse()
print("Reversed:", numbers)
print("Count of 2:", numbers.count(2))
print("Index of 8:", numbers.index(8))

numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)
print("\n")

# -----------------------------------------
# 8. Looping through a list
# -----------------------------------------
fruits = ["apple", "banana", "mango"]
print("Looping using for:")
for f in fruits:
    print(f, end=" ")
print("\n")

print("Looping using range():")
for i in range(len(fruits)):
    print(i, fruits[i])
print("\n")

print("Looping using enumerate():")
for index, value in enumerate(fruits):
    print(index, value)
print("\n")

# -----------------------------------------
# 9. List comprehension
# -----------------------------------------
squares = [x*x for x in range(5)]
print("Squares using list comprehension:", squares)
print("\n")

# -----------------------------------------
# 10. Nested list
# -----------------------------------------
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("Element at row 2, col 3:", matrix[1][2])
