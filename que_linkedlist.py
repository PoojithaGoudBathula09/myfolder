
class Node:
    def __init__(self,data):
        self.data = data 
        self.next = None
class Queue:
    def __init__(self):
        self.front = None 
        self.rear = None
    
    def Enqueue(self, data):
        newnode = Node(data)
        if self.front==None and self.rear==None:
            self.front = newnode
            self.rear = newnode
        else:
            self.rear.next = newnode
            self.rear = newnode
        print(newnode.data,"is Enqueued into Queue")
        
    def Dequeue(self):
        if self.front==None and self.rear==None:
            print("Queue is Empty")
        elif self.front==self.rear:
            print(self.front.data,"is Dequeued from Queue")
            self.front = None
            self.rear = None
        else:
            print(self.front.data,"is Dequeued from Queue")
            self.front = self.front.next 
            
    
    def Display(self):
        if self.front==None:
            print("Queue is Empty")
        else:
            print("Queue :- ",end='')
            temp = self.front 
            while(temp):
                print(temp.data,end=' ')
                temp = temp.next 
            print()
            
    
if __name__ == "__main__":
    
    q = Queue()
    print("\n**********WELCOME TO QUEUE OPERATIONS***********")
    print("Enter 1 to Enqueue an element into Queue")
    print("Enter 2 to Dequeue an element from Queue")
    print("Enter 3 to Display all elements in Queue")
    print("Enter -1 to EXIT\n")
    
    while(True):
        ip = int(input("Enter your Choice :-  "))
        if ip==1:
            data = int(input("Enter your Enqueue value :- "))
            q.Enqueue(data)
        elif ip==2:
            q.Dequeue()
        elif ip==3:
            q.Display()
        elif ip==-1:
            print("You have Exited the Program")
            break
        else:
            print("Invalid Choice ")