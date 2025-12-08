# and Operator --> True only if both conditions are True.

age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")

# or Operator --> : True if at least one condition is True.

day = "Saturday"
holiday = False

if day == "Saturday" or holiday:
    print("You can relax")

# Only one of the conditions needs to be True.

# not Operator --> Inverts the Boolean value. True becomes False, False becomes True.

raining = False

if not raining:
    print("Go for a walk")


# Combining Boolean Operators --> You can combine and, or, not for complex conditions:

age = 20
has_id = True
vip_pass = False

if (age >= 18 and has_id) or vip_pass:
    print("Entry allowed")


# 5. Truth Table Summary
# A	B	A and B	A or B	not A
# True	True	True	True	False
# True	False	False	True	False
# False	True	False	True	True
# False	False	False	False	True

# ✅ Key Points

# and → both must be True
# or → at least one True
# not → invert True/False

# Use parentheses ( ) to control order of evaluation