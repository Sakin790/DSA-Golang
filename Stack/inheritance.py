"""List is Father class/ and Stack is child class 
Stack er kache List class er sob method achee"""


class Stack(list): 
    def is_empty(self):
        return len(self==0)
    def push(self,data):
        self.append(data)
    def pop(self):
       if not self.is_empty():
          return super().pop()
       else:
           raise IndexError("Error is Stack || Empty")
    def peek(self):
        if not self.is_empty():
            return self[-1] # returning last element/ deep element
        else:
           raise IndexError("Error is Stack || Empty")
    def size(self):
        return len(self)
    def insert(self, index, data):
        raise AttributeError("No Attribute such insert")