import numpy as np

class Array:
    def __init__(self):
        self.length = -1
        self.data = {} # hash table / to associate index position with element

    # fetching an element from an array using index position
    def getItem(self, index): # o(1)
        if self.length != -1:
            return self.data[index]
        else:
            return "Array is empty"

    # pushing the item inside an array
    def pushItem(self, element): # o(1)
        self.length += 1
        self.data[self.length] = element
    
    # popping an element from an array
    def popItem(self): # o(1)
        if self.length != -1:
            lastItem = self.data[self.length]
            self.length -= 1
            return lastItem
        else:
            return "Array is empty"
    
    # deleting an item from an array
    def deleteItem(self, index):
        print("deleted : ", self.data[index])
        self.shiftLeft(index)
        del self.data[self.length]
        self.length -= 1
    
    # left shifting the elements after deletion
    def shiftLeft(self, index):
        for i in range(index,self.length):
            self.data[i] = self.data[i+1]

    # inserting an element
    def insertItem(self, index, element):
        if index in range(1,self.length+2):
            self.shiftRight(index)
            self.data[index] = element
            print("inserted: ",self.data[index])
            self.length += 1

    # right shifting the element after insert
    def shiftRight(self,index):
        for i in range(self.length,index-1,-1):
            self.data[i+1] = self.data[i]
            
    # Displaying the elements
    def displayArray(self):
        for i in range(self.length+1):
            print(self.data[i], end = " ")
        print()


arrObj = Array()

arrObj.pushItem(10)
arrObj.pushItem(12)
arrObj.pushItem(78)
arrObj.displayArray()

print("popped item : ",arrObj.popItem())

arrObj.insertItem(2,30)
arrObj.insertItem(1,34)
arrObj.displayArray()

arrObj.deleteItem(3)
arrObj.deleteItem(1)
print(arrObj.getItem(1))

arrObj.displayArray()