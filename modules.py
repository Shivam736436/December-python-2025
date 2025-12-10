# # # A module is simply a Python file (.py) that contains code such as: variable, function, classes, constant..
# # # ex --> math.py, os.py, my_utils.py

# # ⭐ Why Use Modules?

# # Reuse code
# # Organize large programs into smaller files
# # Make debugging easier
# # Share code with others
# # Keep code clean and manageable

# type of modules

# 1. build in modules                       
# 2. user-defined modules
# 3. third-party modules


# import math
# print(math.sqrt(4345))

# import with aliaS
# import math as m
# print(m.sqrt(16))

# if u want import eveything then
from math import *
# print(sqrt(16))

# if you want to create your own module then 
import cal_created_module
# print(cal_created_module.add(2,10))
# print(cal_created_module.sub(2,10))

# ⭐ Module Search Path (sys.path)
import sys
# print(sys.path)
