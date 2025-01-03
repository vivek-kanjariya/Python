# Covered TOPICS

# -OS MODULE
# -File Handling
# -Exception Handling

import os
print(os.getcwd())
print(os.path.join("C:\\", "Users", "Administrator", "Desktop", "python"))
print(os.chdir("C:\\Users\\Administrator\\Desktop\\python"))
print(os.curdir)
print(os.chdir(".."))
print(os.getcwd())
print(os.listdir("C:\\Users\\Administrator\\Desktop\\python"))
print(os.path.exists("C:\\Users\\Administrator\\Desktop\\python"))


counter = 0
def increment():
    global counter
    counter += 1

def get_counter():
    return counter

try:
    print(os.rmdir("c:\\Users\\Administrator\\Desktop\\python\\python.txt"))
except NotADirectoryError:
    print("Directory not found")
finally:
    print("Code Executed times",get_counter())
    increment()
    print("Code Executed times",get_counter())
