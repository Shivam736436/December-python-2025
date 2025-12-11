# -----------------------------------------
# 1. Creating and writing to a file
# -----------------------------------------
f = open("example.txt", "w")  # w = write mode (creates file)
f.write("Hello, this is a test file.\n")
f.write("Python is awesome!\n")
f.close()
print("File created and written successfully\n")

# -----------------------------------------
# 2. Appending to a file
# -----------------------------------------
f = open("example.txt", "a")  # a = append mode
f.write("This line is appended.\n")
f.close()
print("Data appended successfully\n")

# -----------------------------------------
# 3. Reading a file
# -----------------------------------------
f = open("example.txt", "r")  # r = read mode
content = f.read()
print("File content:\n", content)
f.close()

# -----------------------------------------
# 4. Reading line by line
# -----------------------------------------
f = open("example.txt", "r")
print("Reading line by line:")
line = f.readline()
while line:
    print(line.strip())  # strip removes \n
    line = f.readline()
f.close()
print("\n")

# -----------------------------------------
# 5. Reading all lines into a list
# -----------------------------------------
f = open("example.txt", "r")
lines = f.readlines()
print("All lines as list:", lines)
f.close()
print("\n")

# -----------------------------------------
# 6. Using with statement (context manager)
# -----------------------------------------
with open("example.txt", "r") as f:
    content = f.read()
    print("Using 'with' statement:\n", content)
# No need to close file; automatically closed

# -----------------------------------------
# 7. Writing list of lines
# -----------------------------------------
lines_to_write = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("example2.txt", "w") as f:
    f.writelines(lines_to_write)
print("List of lines written to example2.txt\n")

# -----------------------------------------
# 8. File modes summary
# -----------------------------------------
# r = read (default), w = write, a = append
# rb, wb, ab = binary modes
# x = create file, fails if file exists

# -----------------------------------------
# 9. Checking if file exists (os module)
# -----------------------------------------
import os
if os.path.exists("example.txt"):
    print("example.txt exists")
else:
    print("File does not exist")
print("\n")

# -----------------------------------------
# 10. Deleting a file
# -----------------------------------------
# os.remove("example2.txt")  # Uncomment to delete the file
# print("example2.txt deleted")
