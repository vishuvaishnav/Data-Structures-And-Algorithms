class Node:
    def __init__(self, data):
        self.item = data
        self.next = None
        self.prev = None
        
class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    #push iteams at the back just like in stack
    def push(self,item):
        newNode = Node(item)
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return self.length
    
    #pop item from the back
    def pop(self):
        if self.length == 0:
            return "Empty linked list"
        poppedNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = poppedNode.prev
            self.tail.next = None
            poppedNode.prev = None
        self.length -= 1
        return poppedNode.item
        
    # Remove the head of linked list 
    def shift(self):
        if self.length == 0:
            return "Empty List"
        oldHead = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:    
            self.head = oldHead.next
            self.head.prev = None
            oldHead.next = None
        self.length -= 1
        return oldHead.item
        
    #adding the element to the head of the linked list
    def unshift(self,value):
        newNode = Node(value)
        if(self.length == 0):
            self.head = newNode
            self.tail = newNode
        else :
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return self.length
    
    #to get any element from the entered index
    def get(self,index):
        if index<0 or index >= self.length:
            return False
        if index <= self.length//2:
            count = 0
            current = self.head
            while count != index :
                current = current.next
                count += 1
            
        else: 
            count = self.length-1
            current = self.tail
            while count != index:
                current = current.prev
                count -= 1
        print(current.item)
        return current
    
    #setting new value to a desired index
    def setl(self, index, newVal):
        foundNode = self.get(index)
        if foundNode :
            foundNode.item = newVal
            return True
        return False
        
    #inserting a new node anywhere in the doubly linked list    
    def insert(self, index, item):
        if index<0 or index > self.length :
            return False
        if index == 0:
            return self.unshift(item)
        if index == self.length:
            return self.push(item)
        
        newNode = Node(item)
        beforeNode = self.get(index-1)
        afterNode = beforeNode.next
        
        beforeNode.next = newNode
        newNode.prev = beforeNode
        afterNode.prev = newNode
        newNode.next = afterNode
        
        self.length += 1
        
        return self.length
        
    #deleting a node anywhere in the doubly linked list   
    def remove(self,index):
        if index<0 or index > self.length :
            return False
        if index == 0:
            return self.shift()
        if index == self.length:
            return self.pop()  
            
        removedNode = self.get(index)
        removedNode.prev.next = removedNode.next
        removedNode.next.prev = removedNode.prev
        
        removedNode.prev = None
        removedNode.next = None
        
        self.length -= 1
        return self.length
            
            
    #display out doubly linked list
    def display(self):
        if self.head is None:
            print("The list is empty")
            return 0
        else:
            new = self.head
            while new is not None:
                print("Element is: ", new.item)
                new = new.next
        print("\n")
        return 0
    
ll = doublyLinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)

ll.display()
ll.get(1)
print("Poppped element",ll.pop())
ll.display()
ll.setl(2,100)
ll.display()
print("Removed from front",ll.shift())
ll.display()
print(ll.unshift(101))
ll.display()
ll.insert(2,56)
ll.display()
ll.remove(3)
ll.display()
