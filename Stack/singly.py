class Node():
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
#Lifo Method use korboo
class Stack():
    def __init__(self):
        self.start=None
        self.itemCount=0
    def is_empty(self):
        return self.start==None
    def push(self,data):
        n=Node(data,self.start)
        self.start=n
        self.itemCount+=1
    def pop(self):
        if not self.is_empty(): # jodi empty na hoi tahole tar moddhe data ache
            data=self.start.item # for return item
            self.start=self.start.next# start er modddhe next node er ref rakhbo
            self.itemCount-=1
            return data
        else:
            raise IndexError("Stack is empty")
    
    def peek(self):
        if not self.is_empty():
            return self.start.item
        else:
            raise IndexError("Stack is empty")
    
    def size(self):
      return self.itemCount


s1=Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print("Top elememt is",s1.peek())
print("Removed elememt is",s1.pop())
print("Now Top elememt is",s1.peek())
print()