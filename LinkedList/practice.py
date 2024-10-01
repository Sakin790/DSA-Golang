class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class SSL:
    def __init__(self, start=None):
        self.start = start

    def is_empty(self):
        return self.start is None 

    def insert_at_first(self, data):
        n = Node(data, self.start)
        self.start = n

    def insert_at_last(self, data): 
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
        else:
            current = self.start
            while current.next is not None:
                current = current.next
            current.next = new_node

    def delete_first(self):
     if self.start is None:
        # If the list is already empty, nothing to delete
        print("The list is already empty.")
     else:
        # Move the start pointer to the next node
        self.start = self.start.next
    

    def insertAt(self,data):
        newNode= Node(data)
        self.next=newNode
        newNode.next=self.next



    def delete_last(self):
     if self.start is None:
        # Case 1: The list is empty
        print("The list is already empty.")
        return

     if self.start.next is None:
        # Case 2: The list has only one node
        self.start = None
        return

    # Case 3: The list has more than one node
     current = self.start

    # Traverse to the second-to-last node
     while current.next.next is not None:
        current = current.next

    # Remove the last node
     current.next = None

     if self.next is None:
            print("Link is empty")
            return
     if self.start.next is  None:
            self.next=None
            return
        
     current = self.start
     while current.next is not None:
            current = current.next
            current.next = None
       

    def printData(self):
        current = self.start
        while current:
            print(current.data, end=" ")
            current = current.next
        print()  



test = SSL()


test.insert_at_first(10)
test.printData()  


test.insert_at_last(21)
test.printData()  
test.insertAt(12)
