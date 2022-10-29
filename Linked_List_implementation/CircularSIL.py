'''
The below program demonstrates the use and operations of circular singly linked list
'''

from platform import node


class Node:
    def __init__(self,value = None):
        self.value = value
        self.next = None

class CircularSIL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    
    def insertNode(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
            newNode.next = newNode
        else:
            if location == 0: # insert at the begining 
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1: # insert at the end
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                for i in range(location-1):
                    tempNode = tempNode.next
                newNode.next = tempNode.next
                tempNode.next = newNode
                if tempNode == self.tail:
                    self.tail = newNode
    
    # here removing the reference to a memory location/node makes the memory to be recovered by the garbage collector
    def deleteNode(self, location):
        if self.head is None:
            print("List is Empty")
        else:
            if self.head.next is None:
                self.head = None
                self.tail = None

            if location == 0:
                # removing the pointers to the node
                self.tail.next = self.head.next
                self.head = self.head.next

            elif location == -1:
                tempNode = self.head
                while tempNode.next != self.tail:
                    tempNode = tempNode.next
                tempNode.next = self.head
                self.tail= tempNode
            else:
                tempNode = self.head
                for i in range(0,location-1):
                    tempNode = tempNode.next
                nextNode = tempNode.next
                tempNode.next = nextNode.next
                if self.tail == nextNode:
                    self.tail = tempNode
        
    # display Nodes:
    def displayNodes(self):
        if self.head is None:
            print("List is Empty")
        else:
            tempNode = self.head
            while True:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.head:
                    break
            print("*" * 20)


csil = CircularSIL()
csil.insertNode(24,0)
csil.insertNode(34,-1)
csil.insertNode(56,-1)
csil.insertNode(11,2)
csil.insertNode(78,0)

csil.displayNodes()
csil.deleteNode(0)
csil.deleteNode(-1)
csil.deleteNode(1)
csil.displayNodes()





            