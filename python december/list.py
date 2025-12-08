# list --> A list is a collection of items that is ordered, mutable, and allows duplicates.

# create list

# Empty list
my_list = []

# List with elements
fruits = ["apple", "banana", "cherry"]

# List with different data types
info = ["John", 25, True, 5.9]





# (●'◡'●) Accessing List Elements

fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])   # apple
print(fruits[-1])  # date (last element)
print(fruits[1:3]) # ['banana', 'cherry'] (slice)



# Modifying Lists

fruits = ["apple", "banana", "cherry"]

# Change element
fruits[1] = "blueberry"
print(fruits)  # ['apple', 'blueberry', 'cherry']

# Add element at end
fruits.append("date")

# Insert at index
fruits.insert(1, "kiwi")

# Remove element by value
fruits.remove("apple")

# Remove element by index
del fruits[0]

# Remove last element
fruits.pop()





# list operation 
list1 = [1, 2, 3]
list2 = [4, 5]

# Concatenation
combined = list1 + list2
print(combined)  # [1, 2, 3, 4, 5]

# Repetition
print(list1 * 2)  # [1, 2, 3, 1, 2, 3]

# Check membership
print(2 in list1)  # True




# Useful List Methods

# Method	        Description
# append(x)	        Add element at end
# insert(i, x)  	Add element at index i
# remove(x)	        Remove first occurrence of x
# pop()	            Remove and return last element
# sort()        	Sort list ascending
# reverse()     	Reverse list
# index(x)	        Find index of first occurrence of x
# count(x)      	Count occurrences of x
# copy()	        Make a shallow copy
# clear()       	Remove all elements





# loop in list 

fruits = ["apple", "banana", "cherry"]

# Using for loop
for fruit in fruits:
    print(fruit)

# Using while loop
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1




# nested list

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(matrix[0])    # [1, 2, 3]
print(matrix[0][1]) # 2







# List Comprehensions (Advanced but Powerful)

# Squares of numbers 1-5
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# Filter even numbers
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]





# ✅ Key Points

# Lists are mutable → can change after creation.
# Indexing starts at 0; negative indexing starts from the end.
# Lists can store mixed data types.
# Use methods and list comprehensions for efficiency.