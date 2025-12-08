# set --> A set is an unordered collection of unique items.

# No duplicates
# Unordered (no indexing)
# Mutable (can add/remove items)

#  create set
s = {1, 2, 3}
print(s)

# Empty set (important)
s = set()
# {} creates an empty dictionary, not a set.

# no duplicate
s = {1, 2, 2, 3}
print(s)  # {1, 2, 3}

#  add and remove
s = {1, 2, 3}

s.add(4)       # Add element
s.remove(2)    # Remove element (error if missing)
s.discard(5)   # Remove if exists (no error)
s.pop()        # Remove random element
s.clear()      # Remove all elements


#  set operation --> Sets are great for mathematical operations:

#  union 
a = {1, 2, 3}
b = {3, 4}
print(a | b)           # {1, 2, 3, 4}

# Intersection
print(a & b)           # {3}
print(a - b)           # {1, 2}             Difference
print(a ^ b)           # {1, 2, 4}          Symmetric Difference


# member testing
s = {1, 2, 3}
print(2 in s)     # True
print(4 in s)     # False

# . Iterating Over Sets
s = {"a", "b", "c"}
for item in s:
    print(item)


# Frozen Sets (Immutable Sets)
fs = frozenset([1, 2, 3])
# fs.add(4)  # ❌ Error (immutable)

# Safe, hashable, can be keys in dictionaries.



# Common Use Cases of Sets

# Remove duplicates from list
# Fast membership checking
# Mathematical operations
# Compare two collections

items = [1, 2, 2, 3, 4, 4]
unique = list(set(items))
print(unique)  # [1, 2, 3, 4]



# | Feature      | Set                  | List   |
# | ------------ | ------               | ------ |
# | Ordered      | ❌ No                | ✔️ Yes |
# | Unique items | ✔️ Yes               | ❌ No   |
# | Indexing     | ❌ No                | ✔️ Yes |
# | Mutable      | ✔️ Yes               | ✔️ Yes |


# 🔑 Key Points

# Sets store unique, unordered items.
# Useful for duplicates removal & fast lookups.
# Support powerful set operations.
# For immutable version, use frozenset.


