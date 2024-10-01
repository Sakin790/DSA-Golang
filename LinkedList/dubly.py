class Node:
    def __init__(self,prev=None,item=None,next=None):
        self.prev=prev
        self.item=item
        self.next=next

class DDL:
    def __init__(self,start=None):
        self.start=start
    def is_empty(self):
     return self.start==None
    def insert_first(self,data):
        newNode= Node()
        if self.is_empty():
            self.start=newNode
            newNode.prev=None
            newNode.item=data
            newNode.next=None
        else: 
            self.start=newNode
            newNode.prev=None
            newNode.item=data
            newNode.next=self.start
            self.start.prev=newNode
    def insert_at_last(self,data):
        lastNode= Node()
        if self.is_empty():
             lastNode.prev=None
             lastNode.item=data
             lastNode.next=None
             self.start=lastNode
        else:
            lastNode.prev=self.start
            lastNode.item=data
            lastNode.next=None
            self.start.next=lastNode


        
    def printData(self):
        temp=self.start
        while temp is not None:
            print(temp.item, end=" ")
            temp=temp.next
    def search(self, data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return
            temp=temp.next
        return None
    def delete_last(self):
        tem=self.start
        while tem.next is not None:
            if tem.next ==None:
              tem.prev=None
              self.start.next=None
              return
            tem=tem.next
        return
        

       
   


test=DDL()
test.is_empty()
test.insert_first(30)
test.insert_at_last(50)
test.insert_at_last(60)
test.printData()