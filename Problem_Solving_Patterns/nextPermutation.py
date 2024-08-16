def next_permutation(arr,n):
    k = -1
    for i in range(n-2,-1,-1):
        if arr[i] > arr[i-1]:
            k = i-1
            break
    if k == -1:
        arr.sort()
        return(arr)
    else:
        for i in range(n-1,k-1,-1):
            if arr[i]>arr[k] :
                arr[i],arr[k] = arr[k],arr[i]
                break
        #print(arr)
        left = k+1 
        right = n-1
        while (left < right):
            temp = arr[left]
            arr[left] = arr[right]
            arr[right] = temp
            left += 1
            right -= 1
        
        return(arr)

arr = [2,1,5,4,3,0,0]
n = len(arr)
ans = next_permutation(arr,n)
print(ans)
