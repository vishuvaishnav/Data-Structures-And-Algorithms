class Node:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class bst:
    def __init__(self):
        self.root = None
    def insert(self,value):
        newNode = Node(value)
        if self.root == None :
            self.root = newNode
            return self
        current = self.root
        while True :
            if value == current.val:
                return False
            if value < current.val :
                if current.left == None : 
                    current.left = newNode
                    return self
                current = current.left
                
            elif value > current.val :
                if current.right == None :
                    current.right = newNode
                current = current.right
            
            
tree = bst()
tree.insert(8)
tree.insert(3)
tree.insert(10)
tree.insert(1)
tree.insert(6)
tree.insert(14)
tree.insert(4)
tree.insert(7)
print(tree.root.val)
print(tree.root.right.val)
print(tree.root.left.val)
print(tree.root.right.right.val)
print(tree.root.left.left.val)
print(tree.root.val)
