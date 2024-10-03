class Node:
  def __init__(self,item=None,next=None):
    self.item = item
    self.next = next
# 2.
class SLL:
  def __init__(self,start=None,):
    self.start = start
# 3.
  def is_empty(self):
    return self.start==None
# 4.
  def insert_at_start(self,data):
    n = Node(data,self.start)
    self.start = n
# 5.
  def insert_at_last(self,data):
    n = Node(data)
    if not self.is_empty():
      temp = self.start
      while temp.next is not None:
        temp = temp.next
      temp.next = n

    else:
      self.start = n
# 6.
  def search(self,data):
    temp = self.start
    while temp is not None:
      temp = temp.next
      if temp.item == data:
        return temp
      temp = temp.next
    return None
# 7.
  def insert_after(self,temp,data):
    if temp is not None:
      n = Node(data,temp.next)
      temp.next = n
# 8.
  def print_list(self):
    temp = self.start
    while temp is not None:
      print(temp.item,end=' ')
      temp = temp.next
# 10.
  def delete_first(self):
    if self.start is not None:
      self.start=self.start.next
# 11.
  def delete_last(self):
    if self.start is None:
      pass
    elif self.start.next is not None:
      self.start = None
    else:
      temp = self.start
      while temp.next.next is not None:
        temp = temp.next
      temp.next = None
# 12.
  def delete_item(self,data):
    if self.start is None:
      pass
    elif self.start.next is None:
      if self.start.item == data:
        self.start = None
    else:
      temp = self.start
      if temp.item == data:
        self.start = temp.next
      else:
        while temp.next is not None:
          if temp.next.item == data:
            temp.next = temp.next.next
            break
          temp = temp.next
  def __iter__(self):
    return SLLIterator(self.start)
# 9.
class SLLIterator:
  def __init__(self,start):
    self.current = start
  def __iter__(self):
    return self
  def __next__(self):
    if not self.current:
      raise StopIteration
    data = self.current.item
    self.current = self.current.next
    return data


#driver code
mylist = SLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_last(30)
mylist.insert_after(mylist.search(20),25)
mylist.print_list()
mylist.delete_item(30)
print()

for x in mylist:
  print(x,end=' ')

print()