def insertionSort(arr):
    for i in range(1,len(arr)):
        currentVal = arr[i]
        j = i-1
        while j >= 0 and currentVal < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                #print(arr)
        arr[j + 1] = currentVal

        #print(arr)
    
    return arr

arr = list(map(int,input("Enter : ").split()))
print(insertionSort(arr))
