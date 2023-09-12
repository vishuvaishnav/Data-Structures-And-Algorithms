def pivot(arr,start,end):
    p = arr[start]
    swapindex = start
    
    for i in range(start+1,len(arr)):
        if p>arr[i]:
            swapindex+=1
            arr[swapindex],arr[i] = arr[i],arr[swapindex]
            
    arr[start],arr[swapindex] = arr[swapindex],arr[start]
    
    return swapindex
    
def quicksort(arr,left,right):
    if left<right :
        pindex = pivot(arr,left,right)
        #for the left side of the arr
        quicksort(arr,left,pindex-1)
        #for the right side of the arr
        quicksort(arr,pindex+1,right)
    return arr
    
arr = [4,6,9,1,2,5,3]
start = 0
end = len(arr)
print(quicksort(arr,start,end))
