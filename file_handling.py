# # File handling in Python allows you to create, read, update, and delete files.

# Common Modes

# Mode	    Meaning	        Action
# "r"	    Read	         Error if file doesn’t exist
# "w"	    Write	         Creates new file OR overwrites
# "a"	    Append	         Adds to end of file
# "x"	    Create	         Error if file exists
# "b"	    Binary	         Images, PDFs, videos
# "t"	    Text	         Default mode
# "r+"	    Read + Write	 No overwrite
# "w+"	    Write + Read	 Overwrites existing

file = open("text.txt","r")
file.close()

# Important: Always close files to free system resources.

# ⭐ 3. Best Practice — with Statement
with open("data.txt", "r") as f:
    content = f.read()


# ✔ Automatically closes the file
# ✔ Cleaner and safer