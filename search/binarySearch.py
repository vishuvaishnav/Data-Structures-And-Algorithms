arr = list(map(int,input("Enter : ").split()))
num = int(input("Enter number to be searched"))
first=0
last=len(arr)
k=0
while(first<last):
    mid=(first+last)//2
    if arr[mid]==num:
        k+=1
        break
    elif arr[mid]>num:
        last=mid-1
    else:
        first=mid+1
if(k==1):
    print("Found")
else:
    print("Not found")
