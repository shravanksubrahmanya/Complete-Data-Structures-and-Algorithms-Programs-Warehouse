'''
This program demonstrates the implementation of trees and respective operations on trees.
'''
from collections import deque

class TreeNode:
    def __init__(self, value,children = None):
        self.value = value
        self.children = children if children is not None else [] # unlimited childrens can be added
    
    # performs deapth first traversal / pre order
    def __str__(self, level = 0):
        ret = " " * level + str(self.value) + "\n" # " " * level adds indentation based on level
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def print_tree(self, level=0):
        print(" " * level + str(self.value))
        for child in self.children:
            child.print_tree(level + 1)

    def addChild(self, TreeNode):
        self.children.append(TreeNode)
    
    @classmethod
    def take_input(cls):
        data = input("Enter the data for the node: ")
        node = TreeNode(data)
        
        num_children = int(input(f"Enter the number of children for node {data}: "))
        for eachChild in range(num_children):
            child = cls.take_input()
            node.children.append(child)
        return node
    
    # taking input level wise uses queue 
    @classmethod
    def take_input_levelwise(cls):
        data = input("Enter the data for the root node: ")
        root = TreeNode(data)
        queue = deque([root])
        
        while queue:
            current_node = queue.popleft()
            num_children = int(input(f"Enter the number of children for node {current_node.value}: "))
            for child_num in range(num_children):
                child_data = input(f"Enter the data for the child {child_num + 1} of node {current_node.value}: ")
                child = TreeNode(child_data)
                queue.append(child)
                current_node.children.append(child)
        return root
    
    @classmethod
    def count_nodes(cls, node):
        if node is None:
            return 0
        number_of_nodes = 1
        return number_of_nodes + sum(cls.count_nodes(n) for n in node.children)
    
    @classmethod
    def pre_order_traversal(cls, node):
        if node is None:
            return
        print(node.value)
        for child in node.children:
            cls.pre_order_traversal(child)
    
    @classmethod
    def post_order_traversal(cls, node):
        if node is None:
            return
        for child in node.children:
            cls.post_order_traversal(child)
        print(node.value)
                
    
    # Height of a Tree
    @classmethod
    def height(cls, node):
        if node is None:
            return 0
        if not node.children:
            return 1
        return 1 + max(cls.height(child) for child in node.children)

# root node
# tree = TreeNode('Drinks',[])

# # level 1 sub categories
# cold = TreeNode('Cold',[])
# hot = TreeNode('Hot',[])

# tree.addChild(cold)
# tree.addChild(hot)


# # subcategories of hot drinks
# tea = TreeNode("Tea", [])
# coffee = TreeNode("Coffee", [])
# hot.addChild(tea)
# hot.addChild(coffee)

# # sub categories of cold drink
# cola = TreeNode("Cola",[])
# fanta = TreeNode("Fanta",[])
# cold.addChild(cola)
# cold.addChild(fanta)

# # print(tree)
# tree.print_tree()


# def take_input for tree

# newTree = TreeNode.take_input()
# print(newTree)

newTree = TreeNode.take_input_levelwise()
# print(newTree)
# print("Number of nodes in the tree:", TreeNode.count_nodes(newTree))
# print("Height of the tree:", TreeNode.height(newTree))
# print("Pre-order Traversal of the tree:")
# TreeNode.pre_order_traversal(newTree)
# print("Post-order Traversal of the tree:")
# TreeNode.post_order_traversal(newTree)


