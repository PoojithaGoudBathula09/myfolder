def push(data):
    if len(stack)<capacity:
        stack.append(data)
        print(data,"is pushed into the stack")
    else:
        print("stack overflow")
def pop():
    if stack:
        print(stack[-1],"popped from the stack")
        stack.pop()
    else:
        print("stack is underflow")
def peek():
    if stack:
        print(stack[-1],"is a top element in the stack")
    else:
        print("stack is empty")
def display():
    if stack:
        print(stack)
    else:
        print("stack is empty")
if __name__=="__main__":
    stack=[]
    capacity=int(input("enter stack capacity:- "))
    print("******WELCOME TO STACK OPERATIONS")
    print("enter 1 to push elements in the stack")
    print("enter 2 to pop elements from stack")
    print("enter 3 to peek the element")
    print("enter 4 to display stack elements")
    print("enter -1 to exit \n")
    while(True):
        ip=int(input("enter your choice:- "))
        if ip==1:
            data=int(input("enter the elements to push into the stack:- "))
            push(data)
        elif ip==2:
            pop()
        elif ip==3:
            peek()
        elif ip==4:
            display()
        elif ip==-1:
            print("you exited the program")
            break
        else:
            print("invalid choice")