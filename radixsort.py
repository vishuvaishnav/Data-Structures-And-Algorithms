import math
def getdigit(n,i):
    return ( abs(n)//pow(10,i))%10
    
#print(getdigit(3485,2))

def digitcount(n):
    if n==0:
        return 0
    return math.floor(math.log10(abs(n)))+1
    
#print(digitcount(3485456))

def mostdigit(nums):
    maxdigit = 0
    for i in nums:
        maxdigit = max(maxdigit,digitcount(i))
    return maxdigit
    
#print(mostdigit([1,23,456,7894,46,732,2]))
