'''
This program demonstrates the implementation of trees and respective operations on trees.
'''

class TreeNode:
    def __init__(self, value,children = []):
        self.value = value
        self.children = children # unlimited childrens can be added
    
    # performs deapth first traversal
    def __str__(self, level = 0):
        ret = " " * level + str(self.value) + "\n" # " " * level adds indentation based on level
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

# root node
tree = TreeNode('Drinks',[])

# level 1 sub categories
cold = TreeNode('Cold',[])
hot = TreeNode('Hot',[])

tree.addChild(cold)
tree.addChild(hot)


# subcategories of hot drinks
tea = TreeNode("Tea", [])
coffee = TreeNode("Coffee", [])
hot.addChild(tea)
hot.addChild(coffee)

# sub categories of cold drink
cola = TreeNode("Cola",[])
fanta = TreeNode("Fanta",[])
cold.addChild(cola)
cold.addChild(fanta)

print(tree)


