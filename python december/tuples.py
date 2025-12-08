# tuple --> A tuple is a collection similar to a list, but it is immutable (cannot be changed after creation).

#  create tuple
# Empty tuple
t = ()

# Tuple with elements
numbers = (1, 2, 3)

# Mixed data types
info = ("John", 25, True)

# Tuple without parentheses (optional)
t = 1, 2, 3



# Accessing Tuple Elements

t = (10, 20, 30, 40, 50)

print(t[0])   # 10
print(t[-1])  # 50
print(t[1:4]) # (20, 30, 40)




# Immutability (Very Important) --> you can not modifiye tuple
t = (1, 2, 3)
t[0] = 5    # ❌ Error

# But you can create new tuples by combining:
a = (1, 2)
b = (3, 4)
c = a + b   # (1, 2, 3, 4)




# Tuple Methods

# Tuples have only two methods:

# Method	Description
# count(x)	Count occurrences of x
# index(x)	Returns index of first occurrence of x

t = (1, 2, 3, 2)
print(t.count(2))   # 2
print(t.index(3))   # 2





# Iterating Over Tuples

t = (10, 20, 30)

for item in t:
    print(item)




# Nested Tuples
t = (1, (2, 3), (4, 5))
print(t[1])      # (2, 3)
print(t[1][1])   # 3






# Why Use Tuples?

# Feature	            Tuple	            List
# Mutability        	❌ Immutable	        ✔️ Mutable
# Performance	        Faster	            Slower
# Memory	               Less          	More
# Safety	            Safer	            Less safe


# Advantages of tuples:

# Faster than lists
# Used for fixed data
# Can be used as keys in dictionaries (because immutable)



# Common Use Cases

# Returning multiple values from a function
# Constant data (days of week, months)
# Safe configuration values
# Dictionary keys





# ✅ Summary

# Tuples are ordered, immutable, and faster than lists.
# Good for data that should not change.
# Support indexing, slicing, packing/unpacking.
# Have only two methods: count and index.