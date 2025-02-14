def Enqueue(data):
    global front
    global rear
    if front==-1 and rear==-1:
        queue.append(data)
        front=rear=0
        print(data,"is enqueued into queue")
    else:
        queue.append(data)
        rear+=1
        print(data,"is enqueued into queue")
def Dequeue():
    global front
    global rear
    if front==-1 and rear==-1:
        print("queue is empty")
    elif front==rear:
        print(queue[front],"is dequeued from queue")
        queue.pop(0)
        front=-1
        rear=-1
    else:
        print(queue[front],"is dequeued from queue")
        queue.pop(0)
        rear-=1
def Display():
    if queue:
        print(queue)
    else:
        print("queue is empty")
    
if __name__=="__main__":
    queue=[]
    front=-1;
    rear=-1;
print("\n *****WELCOME TO QUEUE OPERATIONS*****")
print("enter 1 to enqueue an element into queue")
print("enter 2 to dequeue an element from queue")
print("enter 3 to display queue elements")
print("enter -1 to EXIT \n")
while(True):
    ip=int(input("enter your choice:- "))
    if ip==1:
        data=int(input("enter your enqueue value:- "))
        Enqueue(data)
    elif ip==2:
        Dequeue()
    elif ip==3:
        Display()
    elif ip==-1:
        print("you have exited the program")
        break
    else:
        print("invalid choice")



