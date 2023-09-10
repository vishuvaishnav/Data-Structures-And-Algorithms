stack=[]
Top=0
def pop():
    global stack,Top
    Top=len(stack)
    if Top==0:
        print("UnderFlow")
    else:
        print(stack[0],"is pop")
        stack=stack[1:Top]
        
def push():
    global stack
    n=int(input("enter"))
    l=[n]
    stack=l+stack
def display():
    print(stack)
while True:
    print("enter 1 for push more elements")
    print("enter 2 for pop")
    print("enter 3 for display")
    print("enter exit to exit")
    c=input("enter choice")
    if c=='1':
        push()
    elif c=='2':
        pop()
    elif c=='3':
        display()
    elif c=="exit":
        break
