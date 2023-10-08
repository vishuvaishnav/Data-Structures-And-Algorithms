class maxBinaryHeap:
    def __init__(self):
        self.values = []
    
    def insert(self,item):
        self.values.append(item)
       
        idx = len(self.values)-1
        while(idx > 0):
            parentIdx = (idx-1)//2

            parent = self.values[parentIdx]
            if item <= parent:
                break
            self.values[parentIdx] = item
            self.values[idx] = parent
            idx = parentIdx
        return
    
    def extractMax(self):
        '''
        maxm = self.values[0]
        end = self.values.pop()'''
        #checking for edge case
        if len(self.values)==1:
            maxm = self.values[0]
            self.values.pop()
            return maxm
        maxm = self.values[0]
        end = self.values.pop()
        if len(self.values) > 0 : 
            self.values[0] = end
            #calling bubble up func.
            self.bubbledown()
            return maxm
            
        #if length is 0 then returning empty as message
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
                if left > element :
                    swap = leftIdx
            if rightIdx < length :
                right = self.values[rightIdx]
                if (swap == None and left > element) or (swap!=None and right>left):
                    swap = rightIdx
            if swap == None:
                break
            self.values[idx] = self.values[swap]
            self.values[swap] = element
            idx = swap                
        
        
    def display(self):
        return self.values
        
#[55, 39, 41, 18, 27, 12, 33]
        
heap = maxBinaryHeap()
heap.insert(41)
heap.insert(39)
heap.insert(33)
heap.insert(18)
heap.insert(27)
heap.insert(12)
heap.insert(55)
print(*heap.display())
print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())
print(heap.extractMax())
