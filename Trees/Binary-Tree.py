'''
This program demonstrates the creation of Binary tree and set of operations on them.
here queue data structure is imported from file "QueueLinkedList.py"
'''
from collections import deque
import QueueLinkedList as queue

class TreeNode:
    '''
    A tree Node consists of 3 parts
        1. data
        2. left child pointer
        3. right child pointer
    '''
    def __init__(self,data):
        self.leftChild = None
        self.data = data
        self.rightChild = None

    # add left child
    def getLeftChild(self):
        return self.leftChild

    # add right Child
    def getRightChild(self):
        return self.rightChild

    def __del__(self):
        print("Deleting : ", self.data)

# pre order traversal
def preOrderTraversal(root):
    if not root:
        return
    print(root.data,  end = " ")
    preOrderTraversal(root.leftChild)
    preOrderTraversal(root.rightChild)

# In-order traversal
def inOrderTraversal(root):
    if not root:
        return
    inOrderTraversal(root.leftChild)
    print(root.data, end = " ")
    inOrderTraversal(root.rightChild)

# post order traversal
def postOrderTraversal(root):
    if not root:
        return
    postOrderTraversal(root.leftChild)
    postOrderTraversal(root.rightChild)
    print(root.data, end  = " ")

# level order traversal / Breadth first search traversal
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customeQueue = queue.Queue()
        customeQueue.enqueue(rootNode)

        while not (customeQueue.isQueueEmpty()):
            root = customeQueue.dequeue()
            print(root.data.data, end = " ")
            if root.data.leftChild is not None:
                customeQueue.enqueue(root.data.leftChild)
            if root.data.rightChild is not None:
                customeQueue.enqueue(root.data.rightChild)


# inserting the new node to the vacant place  before sorting:
# inserting using level order traversal method
def insertNewNode(rootNode, newNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isQueueEmpty()):
            root = customQueue.dequeue()
            if root.data.leftChild is not None:
                customQueue.enqueue(root.data.leftChild)
            else:
                root.data.leftChild = newNode
                print("left insertion successful")
                return
            
            if root.data.rightChild is not None:
                customQueue.enqueue(root.data.rightChild)
            else:
                root.data.rightChild = newNode
                print("right insertion successful")
                return

# deleting a node from tree
'''
1. find the last node using level order traversal
2. replace the contentof last node with the node intended for deletion
3. delete the last node
'''

def deleteNode(rootNode, intendedValue):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        root = rootNode
        parent = None
        intendedNode =  None
        while not customQueue.isQueueEmpty():
            root = customQueue.dequeue()
            if root.data.data == intendedValue:
                intendedNode = root.data # saving the node location if the value is found
            if root.data.leftChild is not None:
                parent =  root # saving the parent node for future references
                customQueue.enqueue(root.data.leftChild)
            if root.data.rightChild is not None:
                parent = root
                customQueue.enqueue(root.data.rightChild)

    # finding the deepest node
        deepestNode = root.data

    # swap the values of intended node and the last node:
    if intendedNode is None:
        print("Given value is not found")
        return
    else:
        deepestNode.data, intendedNode.data = intendedNode.data, deepestNode.data

    # deletion of last Node
        if parent is None:
            # single node tree do not have any parent nodes
            deepestNode.data = None # if it has only one node assign data to None
        elif deepestNode.rightChild is not None:
            # remove the link to the chld node to delete it
            parent.data.rightChild = None
        else:
            parent.data.leftChild = None
    
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    

tree = TreeNode("Drinks")
cold = TreeNode('Cold')
hot = TreeNode('Hot')

tree.leftChild = cold
tree.rightChild = hot

# subcategories of hot drinks
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea
hot.rightChild = coffee

# sub categories of cold drink
cola = TreeNode("Cola")
fanta = TreeNode("Fanta")
cold.leftChild = cola
cold.rightChild = fanta


preOrderTraversal(tree)
print()
inOrderTraversal(tree)
print()
postOrderTraversal(tree)
print()
levelOrderTraversal(tree)
print()

# creating a new node for insertion
noSugarCola = TreeNode("No Sugar Cola")
insertNewNode(tree,noSugarCola)

levelOrderTraversal(tree)
print()

deleteNode(tree,"Hot")
levelOrderTraversal(tree)
print()

deleteBT(tree)