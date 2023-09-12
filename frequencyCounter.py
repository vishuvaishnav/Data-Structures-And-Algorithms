def frequencyCounter(arr):
    d={}
    for i in arr:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d
    
k=frequencyCounter([1,2,3,4,5,1,2,3,4,1,2,3,1,2,3,1,2])
print(k)
