def pascal_row(n):
    ans = 1
    l = []
    l.append(ans)
    for i in range(1,n):
        ans = ans*(n-i)
        ans = ans // i
        l.append(ans)
    return l

def pascal_triangle(n):
    ans = []
    for i in range(1,n+1):
        ans.append(pascal_row(i))
    return ans

n = 6
result = pascal_triangle(n)
for i in result:
    for j in i:
        print(j,end=" ")
    print()
