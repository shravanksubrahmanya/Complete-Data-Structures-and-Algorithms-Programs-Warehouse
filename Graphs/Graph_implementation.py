'''
This program demonstrates the implementation of simple graph using adjascency list
'''
# importing queue data structure from manually created queue
import QueueLinkedList as queue

# we can use list data structure of python as a queue as well.

# create a node
# add linkes to the node
# create a list
# add links/ edges to the list

class Graph:
    def __init__(self):
        self.gdict = {}
  
    # adding the vertex/node to the graph
    def addVertex(self, vertex):
        self.gdict[vertex] = []

    # adding the edges of the node/vertex
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    # printing the graph
    def printGraph(self):
        for keys, values in self.gdict.items():
            print(keys,":",values)
    
    # removing an edge
    def removeEdge(self,vertex, edge):
        try:
            self.gdict[vertex].remove(edge)
        except ValueError:
            print("The edge does not exists !")
    
    # removing a vertex from the graph
    # if we are removing a vertex from a graph we must all the edges related to it first.
    def removeVertex(self, vertex):
        try:
            for l in self.gdict.values(): # ------> o(n)
                if vertex in l:
                    l.remove(vertex)
            del self.gdict[vertex]
        except ValueError:
            print("The vertex does not exists! ")

    # BFS/ level order traversal
    def BFSTraversal(self, vertex):
        # since we are starting from the given vertex we are alrady visited that vetrex
        visited = [vertex]

        # creating a queue to perform operation
        customQueue = queue.Queue()

        # enqueing the given element since we have already visited it.
        customQueue.enqueue(vertex)

        # the loop stops when the queue is empty
        while not customQueue.isQueueEmpty():
            current = customQueue.dequeue().data # accessing the data of current element
            print(current, end = " ")

            # adding the adjascent nodes of the current node to the queue
            # and marking it as visited
            for adjascentVertex in self.gdict[current]:
                if adjascentVertex not in visited:
                    customQueue.enqueue(adjascentVertex)
                    visited.append(adjascentVertex)
        print()

    
    # DFSTraversal
    def DFSTraversal(self, vertex):
        stack = [vertex]
        visited = [vertex]
        while len(stack) != 0:
            currentElement = stack.pop()
            print(currentElement, end = " ")
            for item in self.gdict[currentElement]:
                if item not in visited:
                    stack.append(item)
                    visited.append(item)
        print()

    # DFS Using recursion
    # recursion uses stack we don't need to use stack specifically
    def DFSRecursion(self, vertex):
        visited = []
        def helper(vertex):
            visited.append(vertex)
            print(vertex)

            for item in self.gdict[vertex]:
                if item not in visited:
                    helper(item)
        helper(vertex)


g = Graph()
g.addVertex("A")
g.addVertex("B")
g.addVertex("C")
g.addVertex("D")
g.addVertex("E")
g.addVertex("F")
g.printGraph()

g.addEdge("A",'E')
g.addEdge("A",'C')
g.addEdge("D",'E')
g.addEdge("F",'E')
g.addEdge("A",'F')
g.addEdge("C",'A')
g.addEdge("C",'D')
g.addEdge("B",'A')
g.addEdge("E",'F')
g.addEdge("E",'B')
g.printGraph()

# g.removeEdge("A","F")
# g.printGraph()

# g.removeVertex("F")
# g.printGraph()

g.BFSTraversal("A")
g.DFSTraversal("A")
g.DFSRecursion("A")