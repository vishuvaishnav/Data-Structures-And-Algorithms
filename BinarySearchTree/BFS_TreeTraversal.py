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
    def BFS(self):
        node = self.root
        data = []
        queue = []
        queue.append(node)
        while len(queue) :
            node = queue.pop(0)
            data.append(node.val)
            if node.left :
                queue.append(node.left)
            if node.right :
                queue.append(node.right)
        return data
        
tree = bst()
tree.insert(10)
tree.insert(6)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(20)

#Printing BFS search result
print(tree.BFS())
