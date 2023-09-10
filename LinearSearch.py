arr = list(map(int,input("Enter the list").split()))
num = int(input("Enter the number to search "))

for i in arr:
  if i==num:
    print("Found at index",arr.index(num))
    break
else:
  print("Not Found")
