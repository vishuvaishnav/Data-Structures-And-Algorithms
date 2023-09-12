import math

def getdigit(n,i):
    return ( abs(n)//pow(10,i))%10
    
def digitcount(n):
    if n==0:
        return 0
    return math.floor(math.log10(abs(n)))+1
    
def mostdigit(nums):
    maxdigit = 0
    for i in nums:
        maxdigit = max(maxdigit,digitcount(i))
    return maxdigit
    
def radixSort(nums):
    maxDigitCount = mostdigit(nums)
    for i in range(0,maxDigitCount):
        digitBucket = [[] for j in range(10)]
        for k in range(0,len(nums)):
            digit = getdigit(nums[k],i)
            digitBucket[digit].append(nums[k])
         
        #print(digitBucket) 
        
        nums = [j for sub in digitBucket for j in sub]
        
    return nums
    
l = [12,15,3,5,18,30,23]
k = radixSort(l)
print(k)

