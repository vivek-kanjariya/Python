# Weak References in Python
# A weak reference allows you to reference an object without increasing its reference count. This means the object can still be garbage collected if no strong references exist to it, even if there are weak references pointing to it.

# Weak references are useful in cases like caching, where you want to hold onto an object only as long as it’s in use elsewhere but don’t want to prevent its cleanup if it's no longer needed

# When Are Weak References Used?
# Caching: Avoid retaining objects unnecessarily. For example, cache an object only if it’s being used elsewhere.
# Circular References: Prevent memory leaks caused by circular references in data structures.
# Event Handling: Create references to callback functions or observers without preventing their garbage collection



# The weakref Module
# Python provides the weakref module for creating and working with weak references.






# 1. Creating a Weak Reference
# A weak reference does not prevent its referent (the object it references) from being garbage collected.
import weakref

class MyClass:
    def __init__(self, name):
        self.name = name

obj = MyClass("example")
weak_obj = weakref.ref(obj)  # Create a weak reference to `obj`

print(weak_obj)  # <weakref at 0x...; to 'MyClass' at 0x...>
print(weak_obj())  # Access the object: <__main__.MyClass object at 0x...>

del obj  # Delete the strong reference
print(weak_obj())  # The weak reference now returns `None` as the object is garbage collected.




# 2. Using weakref.WeakValueDictionary
# A WeakValueDictionary is a special dictionary that holds weak references to its values. If an object stored in the dictionary is garbage collected, it is automatically removed from the dictionary.
import weakref

class MyClass:
    def __init__(self, name):
        self.name = name

obj1 = MyClass("Object1")
obj2 = MyClass("Object2")

cache = weakref.WeakValueDictionary()
cache['key1'] = obj1
cache['key2'] = obj2

print(cache['key1'])  # <__main__.MyClass object at 0x...>

del obj1  # Remove the strong reference to `obj1`
print(cache.get('key1'))  # `key1` is now removed from the dictionary: None






# AAAAAdvantages of Weak References
# Memory Efficiency: Avoid keeping objects alive unnecessarily, leading to better memory usage.
# Automatic Cleanup: Objects referenced only by weak references are cleaned up automatically.
# Avoid Circular References: Helps in breaking cycles between objects

# Limitations
# Weak references can only be created for objects that are "weak referenceable." This includes most user-defined classes and built-in types like dict, but not all types (e.g., int, list).
# Weak references require careful design since they can return None if the referenced object has been garbage collected



# When Should You Use Weak References?
# Caching Systems: When building a cache that shouldn’t hold objects in memory if they are no longer used elsewhere.
# Observer Pattern: For event systems where the listener objects can be garbage collected independently of the system itself.
# Complex Graphs and Cycles: To manage relationships between objects without causing circular references.