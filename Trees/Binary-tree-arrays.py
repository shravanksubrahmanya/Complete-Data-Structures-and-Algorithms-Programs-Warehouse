'''
This program demonstrates the  implementation of binary tree and it's operations using 
python list(array)  
'''

from sys import maxsize


class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None] # creation of fixed size array
        self.lastUsedIndex = 0
        self.maxSize = size

    def insertNode(self,value):
        if self.lastUsedIndex+1 == self.maxSize:
            print("Binary Tree is full")
            return 
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        # print(value,"has been inserted successfully")

    # pre-order traversal
    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index], end = " ")
        self.preOrderTraversal(index * 2)
        self.preOrderTraversal(index * 2 + 1)
    
    # post-order traversal
    def postOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2 + 1)
        print(self.customList[index], end = " ")

    # in-order traversal
    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index * 2)
        print(self.customList[index], end = " ")
        self.inOrderTraversal(index * 2 + 1)

    def deleteNode(self,value):
        if self.lastUsedIndex == 0:
            print("Tree is empty")
        for index,item in enumerate(self.customList):
            if item == value:
                self.customList[index] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return
        print("Value is not found in the tree")    
    
    def __del__(self):
        print("Deleting the whole tree")

        
newBT = BinaryTree(8)
newBT.insertNode("Drinks")
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
newBT.insertNode("cola")
newBT.insertNode("fanta")

newBT.preOrderTraversal(1)
print()
print()
newBT.postOrderTraversal(1)
print()
print()

newBT.deleteNode('Hot')
newBT.inOrderTraversal(1)
print()
print()