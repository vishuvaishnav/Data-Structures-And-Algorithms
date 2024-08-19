def matrixMerge(arr,n):
    arr.sort()
    ans = []
    for i in range(0,n):
        if len(ans)==0 or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        else:
            ans[-1][1] = max(ans[-1][1],arr[i][1])
    
    return ans

arr = [[1,3],[2,6],[8,9],[9,11],[8,10],[2,4],[15,18],[16,17]]
n = len(arr)
print(matrixMerge(arr,n))
