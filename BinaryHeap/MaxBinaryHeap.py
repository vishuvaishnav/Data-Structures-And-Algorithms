class maxBinaryHeap:
    def __init__(self):
        self.values = [41,39,33,18,27,12]
    
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
        return self.values
        
heap = maxBinaryHeap()
print(heap.insert(55))
print(heap.insert(1))
print(heap.insert(199))
print(heap.insert(45))
