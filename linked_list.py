class Node:
# This is where data is stored in the linked list.
    def __init__(self, data=None, next=None): #The node initializes with a single datum and its pointer is set to None by default (this is because the first node inserted into the list will have nothing to point at!
        self.data = data #The data in the node!
        self.next = next #The pointed for the next node!

    def get_data(self):
        print("get_data got the insertion " + self.data)
        return self.data

    def get_next(self):
        str(self.next)
        print(self.next)
        return self.next

    def set_next(self, new_next):
        self.next = new_next

    def __str__(self):
        return str(self.data)

    def print_list(self):
        node = self
        while node is not None:
            print(node.data)
            node = node.next
        print()

    __repr__ = __str__

class LinkedList:
    def __init__(self, head=None): # When the list is first initialized it has no nodes, so the head is set to None. (Note: the linked list doesn’t necessarily require a node to initialize. The head argument will default to None if a node is not provided.)
        self.head = head #Here we set the head node, the top node of the list

    def insert_front(self, data): # Our insert method takes data, inits a new node with that data, and adds it to the list! You can insert anywhere in a linked list but it's simple to place at the head and point the new node at the old head.
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

    def search(self, data):
        current = self.head
        found = False
        while current and found is False:
            if current.get_data() == data:
                found = True
            else:
                current = current.get_next()
        if current is None:
            raise ValueError("Data not in list")
        return current

    def delete(self, data): #really just changing the pointer...
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
            raise ValueError("Data not in list")
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
            print("Deleted")

    def __str__(self):
        return str(self.head)

    def print_list(self):#print list doesn't work right yet... don't call it. RECURSION! ugh I'm tired
        link_list = self.head
        while link_list is not None:
            print("Printing...")
            print(link_list)

    __repr__ = __str__


people = LinkedList()
person = Node()

people.insert_front("First")
people.insert_front("Second")
people.insert_front("Third")
people.insert_front("Fourth")
# people.delete("Second")
people.check_size()
people.delete("First")
people.check_size()
