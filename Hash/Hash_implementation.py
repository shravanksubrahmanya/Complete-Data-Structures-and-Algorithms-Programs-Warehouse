'''
This program is used to implement Hash tables and basic operations on them.
open Hashing
'''

import numpy as np

class HashIt:
    def __init__(self, size):
        self.data = [None] * size

    # hash function which returnns hashed value, which will be used as address of a key element
    def _Hash(self, key):
        hash = 0
        for i in range(len(key)):
            hash = (hash +ord(key[i]) * i) % len(self.data)
        return hash
    
    # setting a value to a Hash Table
    def set(self, key, value):
        # get the hashed value for key element
        address = self._Hash(key)
        # if the address does notexists already then create anew list to store values
        #  linked to  current cell i.e the cell for which current address is pointed to 
        if self.data[address] is not True:
            self.data[address] = [] # creation of new list
        # adding an element to the list
        self.data[address].append([key, value])

    #  getting an element from the hash table
    def get(self, key):
        address = self._Hash(key)
        currentBucket = self.data[address] # store the list of element inside a temporary list
        # if currentBucket exists, traverse through the list to find the element
        if len(currentBucket): 
            for i in currentBucket:
                if i[0] == key:
                    return i[1]
        return None
    
    # function to generate all the keys
    def keys(self):
        keyArray = []
        currentBucket = []
        for i in range(len(self.data)):
            if self.data[i]:
                currentBucket = self.data[i]
                keyArray.extend([x[0] for x in currentBucket])
        return keyArray

    # function to generate all the values
    def values(self):
        keyArray = []
        currentBucket = []
        for i in range(len(self.data)):
            if self.data[i]:
                currentBucket = self.data[i]
                keyArray.extend([x[1] for x in currentBucket])
        return keyArray

obj = HashIt(20)

obj.set('apples',232)
obj.set('Mangos',743)
obj.set('grapes',672)
obj.set('pineapple',123)
print(obj.get('apples'))
print(obj.keys())
print(obj.values())
     
        
        

