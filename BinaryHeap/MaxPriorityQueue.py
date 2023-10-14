class PriorityQueue:
    def __init__(self):
        self.values = []
    
    def enqueue(self,val,priority):
        newNode = Node(val,priority)
        self.values.append(newNode)
       
        idx = len(self.values)-1
        element = self.values[idx]
        while(idx > 0):
            parentIdx = (idx-1)//2

            parent = self.values[parentIdx]
            if element.priority <= parent.priority:
                break
            self.values[parentIdx] = element
            self.values[idx] = parent
            idx = parentIdx
        return
    
    def dequeue(self):
        '''
        maxm = self.values[0]
        end = self.values.pop()'''
        #checking for edge case
        if len(self.values)==1:
            maxm = self.values[0]
            self.values.pop()
            print(maxm.val,maxm.priority)
            return maxm
        maxm = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0 : 
            self.values[0] = end
            #calling bubble up func.
            self.bubbledown()
            print(maxm.val,maxm.priority)
            return maxm
            
        #if length is 0 then returning empty as message
        print(maxm.val,maxm.priority)
        return self.values
        
    def bubbledown(self):
        idx = 0
        length = len(self.values)
        element = self.values[0]
        while(True):
            leftIdx = 2*idx+1
            rightIdx = 2*idx+2
            swap = None
            
            if leftIdx < length :
                left = self.values[leftIdx]
                if left.priority > element.priority :
                    swap = leftIdx
            if rightIdx < length :
                right = self.values[rightIdx]
                if (swap == None and left.priority > element.priority) or (swap!=None and right.priority>left.priority):
                    swap = rightIdx
            if swap == None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap                
        
        
    def display(self):
        for i in self.values:
            print(i.val,i.priority)
        #return self.values
        
class Node:
    def __init__(self,val,priority):
        self.val = val
        self.priority = priority

hospital = PriorityQueue()
print("----------------------------------------")
hospital.enqueue("Common Cold",1)
hospital.enqueue("Gunshot Wound",5)
hospital.enqueue("High Fever",2)
hospital.enqueue("broken arm",4)
hospital.enqueue("glass in foot",3)
hospital.display()
print("----------------------------------------")
hospital.dequeue()
print("----------------------------------------")
hospital.dequeue()
print("----------------------------------------")
hospital.dequeue()
print("----------------------------------------")
hospital.dequeue()
print("----------------------------------------")
hospital.dequeue()
print("----------------------------------------")
