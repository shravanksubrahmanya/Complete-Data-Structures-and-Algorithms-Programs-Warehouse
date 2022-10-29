'''
The below program demonstrates the implementation of Doubly lionked lists and it's opeartions

steps:
1. implement node class to create a node, with following properties
    * previous pointer
    * data / value
    * next pointer
2. implement a list class to create list and implement following methods
     * create a list
        * create head and tail  pointer
     * insert element into list
        * 3 conditions
             1. if list is empty:
                * assign head ad tail pointers to new node 
                * assign previous and next pointer points to the current node itself
            1. insert begining
                *  assign next pointer of new node points to the node for which head is pointing to
                * assign previous pointer of new node as tail node
                * assign next pointer of tail node as new node
                * assign previous of node for which head is pointing to as new node
                * assign header to new node
            2. insert end
                * go to tail node
                * assign previous pointer of new node as tail node
                * assign next pointer of new node as node for whiich head is pointing to
                * assign next pointer of tail node as new node
                * assign previous pointer of head node as new node
            3. insert in the middle
                * loop till the given location
                * assign previous pointer of new node as current node
                * assign next pointer of new node as the node for which current node's next pointer is pointing to
                * assign nextNode's previous pointer points to new node
                * assign current node's next pointer points new node
     * delete element fro list
        * 3 conditions
             1. id list has only one element :
                 * assign None to head and tail pointers
            1. delete begining
                * make the next pointer of tail points to next node to the head
                * make the previous pointer of head's next node point to tail
            2. delete end
                * loop till the end and  delete node
                 * make previous element of tail points to  first/head element
                 * make previous pointer of head node points to previous element of tail element
                 * garbage collector automatically remove the node which do have reference to it
            3. delete in the middle
                * loop till one place less than givven location
                * create a variable to store next node
                * make next pointer of current node to point the node references in the next pointer of nextNod0e
                * make the previous pointer of node pointed by nextnode point to current node
     * display list /  traverse through list
        * traverse till next pointer of last node iis the first node
     * search a particula item in list
'''
'''
this program needs below validations
    * programm only needs location as -1 for insertion or deletion at the last position
    * program pnly needs location as 0 for insertion or deletion at begining
    * needs validation for invalid location value
    * location value other than -1 must not point to last element
'''
# Creation of nodes
class Node:
    # we can also pass nodes/address to the pointers
    def __init__(self, prev = None, value = None, next = None):
        self.prev = prev
        self.value = value
        self.next = next

class CDLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # def __iter__(self):
    #     tempNode = self.head
    #     while tempNode:
    #         yield tempNode
    #         tempNode = tempNode.next

    # insert function
    def insertCDLL(self, value, location):
        if location == 0: # insert begining
            if self.head is None:
                newNode = Node(value = value)
                newNode.next = newNode
                newNode.prev = newNode
                self.head = newNode
                self.tail = newNode
            else:
                newNode = Node(self.tail,value,self.head) # passing value along with previous and next address
                self.tail.next = newNode
                self.head.prev = newNode
                self.head = newNode
        elif location == -1:
            if self.head is None:
                newNode = Node(value = value)
                newNode.next = newNode
                newNode.prev = newNode
                self.head = newNode
                self.tail = newNode
            else:
                newNode = Node(self.tail, value, self.head)
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
        else:
            tempNode = self.head
            for i in range(location-1):
                tempNode = tempNode.next
            newNode = Node(tempNode,value,tempNode.next)
            tempNode.next.prev = newNode
            tempNode.next = newNode
    
    # deletion function
    def deleteCDLL(self,location):
        if self.head is None:
            print("List is empty")
        else:
            if location == 0:
                if self.head.next == self.head:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.next = self.head.next
                    self.head.next.prev = self.tail
                    self.head = self.head.next
            elif location == -1:
                if self.head.next == self.head:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = self.head
                    self.head.prev = self.tail.prev
                    self.tail = self.tail.prev
            else:
                tempNode = self.head
                for i in range(location-1):
                    tempNode = tempNode.next
                tempNode.next.next.prev = tempNode
                tempNode.next = tempNode.next.next
    
    def displayCDLL(self):
        tempNode = self.head
        while True:
            print(tempNode.value)
            tempNode = tempNode.next
            if(tempNode == self.head):
                break
        print("*" * 20)
    
dcll = CDLL()
dcll.insertCDLL(12,0)
dcll.insertCDLL(13,-1)
dcll.insertCDLL(23,0)
dcll.insertCDLL(67,0)
dcll.insertCDLL(64,2)

dcll.displayCDLL()

dcll.deleteCDLL(0)
dcll.deleteCDLL(2)
dcll.deleteCDLL(-1)

dcll.displayCDLL()


