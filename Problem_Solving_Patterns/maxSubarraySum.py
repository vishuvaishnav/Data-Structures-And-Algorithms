#Kadane's Algorithm
def maxSubarray(arr,n):
    sum_array = 0
    maxi = min(arr)
    ansStart = -1
    ansEnd = -1
    start = -1
    for i in range(0,n):
        sum_array += arr[i]
        if sum_array > maxi:
            maxi = sum_array
            ansStart = start
            ansEnd = i
        
        if sum_array < 0:
            sum_array = 0
        if sum_array == 0:
            start = i
    if maxi < 0:
        return 0
    print("Subarray :",arr[ansStart+1:ansEnd+1])
    return maxi
        
arr = [-2,-3,4,-1,-2,1,5,-3]
n = len(arr)

print("Sum :",maxSubarray(arr,n))
