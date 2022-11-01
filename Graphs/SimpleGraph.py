'''
This program demonstrates the implementation of simple graph and it's functions
using adjascency list
'''

# node class
class Node:
    def __init__(self,data):
        self.data = data
        self.connections = []

class Graph:
    def __init__(self,name = None):
        self.Gname = name
        self.nodeCount = 0
        self.adjascencyList = {}

    # adding a node to the graph
    def addNode(self,node):
        self.adjascencyList[node.data] = []
        self.nodeCount += 1

    # adding an edge between two nodes
    def addEdge(self,rootNode, ConnectionNode):
        if rootNode.data not in self.adjascencyList:
            self.addNode(rootNode)
        self.adjascencyList[rootNode.data].append(ConnectionNode.data)
        rootNode.connections.append(ConnectionNode)
    
    # display the list of Nodes and it's connections
    def displayConnections(self):
        for key, values in self.adjascencyList.items():
            print(key, end = " -> ")
            for item in values:
                print(item, end = " ")
            print()

graph = Graph("Simple Graph")
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)

graph.addNode(one)
graph.addEdge(two, three)
graph.addEdge(three, four)
graph.addNode(six)
graph.addEdge(four, five)
graph.addEdge(one, six)
graph.addEdge(one, three)
graph.addEdge(three, one)
graph.addEdge(three,six)

graph.displayConnections()


