"""
==================================================
PYTHON FILE HANDLING — COMPLETE EXPLANATION
==================================================

File handling allows Python to:
- create files
- read files
- write to files
- append data
- close files safely
"""

# -----------------------------------------------
# 1. OPENING A FILE
# -----------------------------------------------
# open(filename, mode)

# Modes:
# 'r'  -> read (file must exist)
# 'w'  -> write (creates new file, deletes old content)
# 'a'  -> append (adds content, keeps old data)
# 'x'  -> create (error if file exists)
# 'rb' -> read binary
# 'wb' -> write binary


# -----------------------------------------------
# 2. WRITING TO A FILE
# -----------------------------------------------
file = open("example.txt", "w")   # create/open file
file.write("Hello, this is Python file handling.\n")
file.write("This line is written using write().\n")
file.close()   # always close the file


# -----------------------------------------------
# 3. READING FROM A FILE
# -----------------------------------------------
file = open("example.txt", "r")
content = file.read()   # reads entire file
print(content)
file.close()


# -----------------------------------------------
# 4. READ LINE BY LINE
# -----------------------------------------------
file = open("example.txt", "r")

print(file.readline())  # reads one line
print(file.readline())  # reads next line

file.close()


# -----------------------------------------------
# 5. READ ALL LINES AS LIST
# -----------------------------------------------
file = open("example.txt", "r")
lines = file.readlines()  # returns list of lines
print(lines)
file.close()


# -----------------------------------------------
# 6. APPENDING TO A FILE
# -----------------------------------------------
file = open("example.txt", "a")
file.write("This line is appended.\n")
file.close()


# -----------------------------------------------
# 7. WITH STATEMENT (BEST PRACTICE)
# -----------------------------------------------
# Automatically closes file

with open("example.txt", "r") as file:
    data = file.read()
    print(data)


# -----------------------------------------------
# 8. CHECK IF FILE EXISTS
# -----------------------------------------------
import os

if os.path.exists("example.txt"):
    print("File exists")
else:
    print("File not found")


# -----------------------------------------------
# 9. DELETE A FILE
# -----------------------------------------------
# Be careful — this permanently deletes the file

# os.remove("example.txt")


# -----------------------------------------------
# 10. FILE POINTER POSITION
# -----------------------------------------------
with open("example.txt", "r") as file:
    print(file.tell())   # current position
    print(file.read(5))  # read first 5 characters
    print(file.tell())   # updated position
    file.seek(0)         # move pointer to beginning
    print(file.read(5))


# -----------------------------------------------
# 11. WRITE MULTIPLE LINES
# -----------------------------------------------
lines = [
    "Line 1\n",
    "Line 2\n",
    "Line 3\n"
]

with open("multi.txt", "w") as file:
    file.writelines(lines)


# -----------------------------------------------
# 12. FILE HANDLING SUMMARY
# -----------------------------------------------
"""
open()       -> opens file
read()       -> reads content
readline()   -> reads one line
readlines()  -> reads all lines
write()      -> writes data
writelines() -> writes list
close()      -> closes file
with         -> safest way
"""


# -----------------------------------------------
# END
# -----------------------------------------------
print("All file handling concepts explained ✅")
