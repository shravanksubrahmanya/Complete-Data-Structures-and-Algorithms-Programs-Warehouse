'''This code demonstrates the dynamic resizing of a Python list and how memory allocation changes as elements are added.'''

import sys

l1 = []

print(f"Initial size of list: {sys.getsizeof(l1)} bytes")

for i in range(17):
    l1.append(i)
    print(f"{i} --> {sys.getsizeof(l1)} bytes")
    
a = 1
l1.append(1)

print(id(1))
print(id(a))
print(id(l1[-1]))
