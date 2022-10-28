'''
This file contains the implementation of methods of array Data Structures
'''
from ctypes import sizeof
import numpy as np

lists = [1,4,58,76,45]
# print(lists.__sizeof__())
# print(lists[3].__sizeof__())

array = np.array(lists)
print(array.size)
print(array.itemsize) # itemsize function gives the memory size of each element in an array
'''
this array takes total memory size of 5 * 8 = 40 bytes
we are storing the data in a sequentuial order so thecomputer remembers them
'''

'''
frequently used operations on array are as follows:
1. push / append // o(1)
2. pop // o(1)
3. insert // o(n) -> because elements are need be searched one by one
4. delete/remove // o(n) -> same as above
'''

# push / append
np.append(array, 34)
print(array)

# pop 