'''
Queue implementation using linked list
make the class name and file name to avoid accessing errors outside.
'''
class Node:
    def __init__(self,data):
        self.prev = None
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.rear = None
        self.front = None
        self.nodeCount = 0
    

    def __iter__(self):
        node = self.rear
        while node:
            yield node
            node = node.prev
    
    def __str__(self):
        node = self.rear
        output = ''
        while node:
            output += str(node.data) +" "
            node = node.prev
        return output

    '''
    insertion(enqueue) -> rear end
    deletion(dequeue) -> front end
    '''

    def enqueue(self, data):
        newNode = Node(data)
        if self.rear == None:
            self.rear = newNode
            self.front = newNode
        else:
            newNode.prev = self.rear
            self.rear.next = newNode
            self.rear = newNode
        self.nodeCount += 1
    
    def dequeue(self):
        if self.front == None:
            print("Queue is Empty")
        else:
            data = self.front
            if self.front == self.rear:
                self.front = None
                self.rear = None
            else:
                self.front = self.front.next
                self.front.prev.next = None
                self.front.prev = None
                self.nodeCount -= 1
            return data

    def peek(self):
        if self.front == None:
            print("Empty queue")
        else:
            return self.front

    def isQueueEmpty(self):
        return self.front == None

    def haveSingleElement(self):
        return self.front == self.rear

q = Queue()
q.dequeue()
q.enqueue(23)
q.enqueue(54)
q.enqueue(89)
q.enqueue(12)
q.enqueue(34)


print(q)

print(q.dequeue().data)
print(q.dequeue().data)

print(q.isQueueEmpty())
print(q)

