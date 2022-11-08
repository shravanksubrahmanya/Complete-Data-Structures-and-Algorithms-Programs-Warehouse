'''
This program demonstrates implementation of topological sorting method on a graph
'''
'''
This program demonstrates the implementation of simple graph using adjascency list
'''

from collections import defaultdict

class Graph:
    def __init__(self, noOfVertices):
        self.graph = defaultdict(list)
        self.noOfVertices = noOfVertices

    # adding the edges of the node/vertex
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    # printing the graph
    def printGraph(self):
        for keys, values in self.graph.items():
            print(keys,":",values)
    
    # topological sort utility function
    def topologicalSortUtil(self, vertex, visited, stack):
        visited.append(vertex)

        for i in self.graph[vertex]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        
        # in this stack all elements are inserted at first position
        stack.insert(0, vertex)
    
    # topological sort function to sort each element
    def topologicalSort(self):
        visited = []
        stack = []

        # to visit only key elements of the graph
        for k in list(self.graph): # for each key elements in a graph
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)

        print(stack)


g = Graph(8)
# g.addVertex("A")
# g.addVertex("B")
# g.addVertex("C")
# g.addVertex("D")
# g.addVertex("E")
# g.addVertex("F")
# g.addVertex("G")
# g.addVertex("H")

g.addEdge("B",'C')
g.addEdge("A",'C')
g.addEdge("B",'D')
g.addEdge("C",'E')
g.addEdge("E",'H')
g.addEdge("E",'F')
g.addEdge("D",'F')
g.addEdge("F",'G')

g.printGraph()
g.topologicalSort()