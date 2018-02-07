class Node:
  def __init__(self, data=None, next=None):
      self.data = data
      self.next = next
  def get_data(self):
      print("i like to know whats happen" + self.data)
      return self.data
  def get_next(self):
      str(self.next)
      print(self.next)
      return self.next 
  def set_next(self, new_next):
      self.next = new_next
  def __str__(self):
      return str(self.data)
  __repr__ = __str__ 
class LinkedList:
  def __init__ (self, head=None):
      
      self.head = head
  def insert_front(self, data):
      new_node = Node(data)
      new_node.set_next(self.head)
      self.head = new_node
      return
  def check_size(self):
      current = self.head
      count = 0
      while current:
          count += 1 
          current = current.get_next()
          print(count)
      return count
  def delete(self, data):
      current = self.head
      previous = None
      found = False
      while current and found is False:
          if current.get_data() == data:
              found = True
          else:
              previous = current
              current = current.get_next()
      if current is None:
          raise ValueError("data lacking bro")
      if previous is None:
          self.head = current.get_next()
      else: 
          previous.set_next(current.get_next)
          print("deleted")
  def __str__(self):
      return str(self.head)
  __repr__=__str__
person = Node()
people = LinkedList()
people.insert_front('first')
people.insert_front('second')
people.insert_front('third')
people.insert_front('fourth')
people.check_size()
people.delete("first")
people.delete("second")