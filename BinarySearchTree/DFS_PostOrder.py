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
    def DFSPostOrder(self):
        data = []
        current = self.root
        def traverse(node):
            if node.left :
                traverse(node.left)
            if node.right :
                traverse(node.right)
            data.append(node.val)
        traverse(current)
        
        return data


'''
        10
    6       15
  3   8        20
'''        

tree = bst()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

#Printing DFS Preorder search result
print(tree.DFSPostOrder())
