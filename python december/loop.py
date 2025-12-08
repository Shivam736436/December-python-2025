# loop --> Loops are used to repeat a block of code multiple times until a condition is met.

#  for loop --> Used to iterate over a sequence (like a list, tuple, string, or range).

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range()

for i in range(5):  # 0 to 4
    print(i)

#  while loop --> Repeats a block of code as long as a condition is True.

i = 0
while i < 5:
    print(i)
    i += 1


# 3. Loop Control Statements
# Statement	Purpose
# break	Exit the loop immediately
# continue	Skip current iteration and go to next
# pass	Do nothing (placeholder)

# Example of break and continue:

for i in range(10):
    if i == 5:
        break  # exits loop at 5
    if i % 2 == 0:
        continue  # skips even numbers
    print(i)


# 4. Nested Loops --> You can put a loop inside another loop:

for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)



# Use for when iterating over a sequence.
# Use while when looping based on a condition.
# Avoid infinite loops: make sure condition eventually becomes False.

# ✅ Summary Table

# Loop Type	Best Use	Example
# for	Iterating over sequence/range	for x in [1,2,3]: print(x)
# while	Repeat until a condition is False	while x < 10: x += 1