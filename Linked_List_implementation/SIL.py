'''
this program demonstrates the operations performed on singly linked list
'''

# creation of singly linked list

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
    
    def __del__(self):
        print("node deleted", self.value)

class SlinkedList:
    def __init__(self):
        self.head = None # in python we will use None instead of Null
        self.tail = None
        self.nodeCount = 0

    # iterator 
    def __iter__(self):
        node = self.head
        while node:
            yield node #  generator function returns the elements one by one
            node = node.next

    # node insertion function 
    def insertSLL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0: # insert  element at the begining
                newNode.next = self.head
                self.head = newNode
            elif location == -1: # insert element at the end of the list
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                for i in range(1,location):
                    tempNode = tempNode.next

                newNode.next = tempNode.next
                tempNode.next = newNode
                if tempNode == self.tail:
                    self.tail = newNode

        self.nodeCount += 1

    # list traversal function
    def traverseSLL(self):
        if self.head is None:
            print("List is Empty");
        else:
            tempNode = self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode = tempNode.next

    # search function
    def searchSLL(self, elem):
        if self.head is None:
            print("List is Empty")
        else:
            tempNode = self.head
            index = 1
            while tempNode:
                if tempNode.value == elem:
                    print("the element found at the location : ", index)
                    return
                tempNode = tempNode.next
                index += 1
            print("The node does not exists in the list")

    # deletion of a node from single linked list
    def deleteSLL(self, location):
        if self.head is None:
            print("LinkedList is Empty ")
        else:
            if self.head.next is None:
                self.head = None
                self.tail = None
            else:
                tempNode = self.head
                if location == 0:
                    self.head = self.head.next
                    # tempNode.next = None
                elif  location == -1 or (location - self.nodeCount) == 0:
                    while tempNode.next is not self.tail:
                        tempNode = tempNode.next
                    tempNode.next = None
                    self.tail = tempNode
                else:
                    for i in range(1,location):
                        tempNode = tempNode.next

                    nextNode =  tempNode.next
                    tempNode.next = nextNode.next
                    # nextNode.next = None

            self.nodeCount -= 1

    # deleting an entire single linked list
    def delEntireSLL(self):
        if self.head is None:
            print("The linkedlist does not exists ")
        else:
            self.head = None
            self.tail = None

    # destructor function
    def __del__(self):
        print("Destructor called, List Deleted ")
        
SSL = SlinkedList()

while True:
    print(" 1 -> insert\n 2 -> delete\n 3 -> display the list\n 4 -> search an element\n 5 -> delete list and exit\n")
    ch = int(input("Enter your choice : "))

    if ch == 1:
        print(" 0 -> insert at begining\n -1 -> insert at last\n otherwise, enter specific location of the node\n")
        location = int(input())
        value = int(input("Enter the value to insert : "))
        SSL.insertSLL(value, location)
    elif ch == 2:
        print(" 0 -> insert at begining\n -1 -> insert at last\n otherwise, enter specific location of the node\n")
        location = int(input())
        SSL.deleteSLL(location)
    elif ch == 3:
        SSL.traverseSLL()
    elif ch == 4:
        key = int(input("Enter the key element to search : "))
        SSL.searchSLL(key)
    elif ch == 5:
        SSL.delEntireSLL()
        break
    else:
        print("Enter a valid value ")

