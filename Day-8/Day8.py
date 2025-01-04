# Covered Topics 

# -Modules Creating
# -Modules Using
# -Modules Importing
# -Modules Exporting
# -Modules Deleting
# -pip


# NOTEEEE
# Export isnt always preferred in python unlike working with Frameworks

# What is pip?
# pip is a package manager for Python packages, or modules in other words. It is a tool for installing and managing Python packages.
# (just like npm for node.js and its frameworks like react)

# What is a module?
# A module is a Python file containing Python code, usually written in Python, that can be imported by another Python file.
# (you can use it in other python files)
# (usually its an file with written code in python)

# What is a package?
# A package is a directory containing one or more modules.

# importing an package 
# (there are 2 types of packages as external and internal)

# internal module
import math

# external module
import exModule
#importing an specific function from a module
from exModule import mul
from exModule import add

# Using modules
print(math.pi)
print(exModule.func(5))
print(mul(2, 3))
print(add(2, 3))

# Delete the module from the current namespace or Sequence Running code
del math
del exModule


# PACKAGES

# STARNDARD ANATOMY

# mypackage/
#     __init__.py
#     module1.py
#     module2.py
#     submodule/
#         __init__.py
#         submodule1.py
#         submodule2.py

# __init__.py is a special file that makes the directory a package. It can be empty, but it's often used to specify the package's metadata.
# module1.py and module2.py are regular Python modules.
# submodule/ is a subpackage, which is a package inside another package

# importing a package
import exPackage
# Specific module inside an package import
from exPackage import Module1
from exPackage import Module2
# Import a specific function or class from a module
from exPackage.Module1 import myfunction
# Import a submodule
from exPackage.submodule import submodule1

#Deleting a package
del exPackage


# PIP
# PIP is a package manager for Python packages

# Install a package
# pip install <package_name>

# Uninstall a package
# pip uninstall <package_name>

# Update a package
# pip install --upgrade <package_name>

# List installed packages
# pip list

# EXAMOLES
# pip install pandas
# pip install numpy
# pip install sklearn