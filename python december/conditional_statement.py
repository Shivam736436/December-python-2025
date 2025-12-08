# if Statement --> The if statement runs a block of code only if a condition is True.

age = 18
if age >= 18:
    print("You are an adult")

# else Statement --> The else statement runs a block of code if the if condition is False.

age = 16
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# elif Statement --. elif stands for “else if” and lets you check multiple conditions in sequence.

marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# . Nested if Statements --> You can also put if statements inside other if statements for more complex decisions.

age = 20
gender = "Male"

if age >= 18:
    if gender == "Male":
        print("Adult Male")
    else:
        print("Adult Female")
else:
    print("Minor")


# 5. Tips

# Use proper indentation (4 spaces per level).
# elif is optional; you can have multiple elif statements.
# Only one block of if, elif, else executes in a sequence.

# ✅ Summary Table

# Statement	Executes When
# if	Condition is True
# elif	Previous if/elif False, current condition True
# else	All previous conditions False