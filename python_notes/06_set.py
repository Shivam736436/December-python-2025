# -----------------------------------------
# 1. Creating a set
# -----------------------------------------
my_set = {1, 2, 3, 3, 4}
print("Original Set:", my_set)   # Duplicate removed → {1, 2, 3, 4}

# -----------------------------------------
# 2. Adding items
# -----------------------------------------
my_set.add(5)
print("After add:", my_set)

# -----------------------------------------
# 3. Adding multiple items
# -----------------------------------------
my_set.update([6, 7, 8])
print("After update:", my_set)

# -----------------------------------------
# 4. Removing items
# -----------------------------------------
my_set.remove(4)        # Removes 4 (error if not present)
print("After remove(4):", my_set)

my_set.discard(10)      # No error even if 10 not present
print("After discard(10):", my_set)

# -----------------------------------------
# 5. pop() – removes random element
# -----------------------------------------
removed_item = my_set.pop()
print("Popped:", removed_item)
print("After pop:", my_set)

# -----------------------------------------
# 6. clear() – empty set
# -----------------------------------------
temp = {1, 2, 3}
temp.clear()
print("After clear:", temp)

# -----------------------------------------
# 7. Set Operations
# -----------------------------------------
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union (A ∪ B) → combine
print("Union:", A.union(B))  # {1,2,3,4,5,6}

# Intersection (A ∩ B) → common elements
print("Intersection:", A.intersection(B))  # {3,4}

# Difference (A - B) → items only in A
print("Difference A-B:", A.difference(B))  # {1,2}

# Symmetric Difference (A △ B) → uncommon elements
print("Symmetric Difference:", A.symmetric_difference(B))  # {1,2,5,6}

# -----------------------------------------
# 8. Checking membership
# -----------------------------------------
print(3 in A)   # True
print(10 in A)  # False

# -----------------------------------------
# 9. Loop in set
# -----------------------------------------
print("Looping:")
for i in A:
    print(i)

# -----------------------------------------
# 10. Copying a set
# -----------------------------------------
C = A.copy()
print("Copied Set:", C)
