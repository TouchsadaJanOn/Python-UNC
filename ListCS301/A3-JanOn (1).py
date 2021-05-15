"""Assignment 3: Touchsada Jan On"""
class Stack():
  def __init__(self):
    print("Here is Stack class---------------------------")
    self.myStack = []
  # adds a new item to the top of the stack.
  # Running Time: O(1) or constant time because list added item to the end of list
  def push(self, item):
    print("Pushing new item ")
    self.myStack.append(item)
  # removes the top item from the stack. 
  # Running Time: O(1) because to delete the top of the element means last item in the list, require no shifting
  def pop(self):
    print("popping the top of stack ")
    try:
      return self.myStack.pop()
    except LookupError:
      return "Sorry, No index found! Possibly Empty.."
  # tests  to  see  whether  the  stack  is  empty. 
  # Running Time: O(1) or constant time because python len function take constant time to determine the size of the list and check against 0
  def isEmpty(self):
    print("Stack Empty? ")
    if len(self.myStack) == 0:
      return True
    return False
  # returns the top item from the stack but does not remove it.   
  # Running Time: O(1) or constant time because peek return last inserted item
  def peek(self):
    print("peeking from top of stack ")
    if len(self.myStack) != 0:
      return self.myStack[-1]
    else:
      return "Stack is empty"
  # returns the number of items on the stack. 
  # Running Time: O(1) or constant time because python len function take constant time to determine the size of the list
  def size(self):
    print("size: ")
    return len(self.myStack)
  # String method to print the list
  # O(1)
  def __str__(self):
    print("New Stack list")
    return str(self.myStack)

s=Stack()
print(s.isEmpty())
s.push(4)
s.push('dog')
s.push(5)
s.push(6)
s.push(7)
print(s)
s.push("newItem")
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.peek())
print(s)
print(s.pop())
print(s.pop())
print(s.size())
print(s)
print(s.pop())
print(s.pop())
print(s.pop())
print(s)
print(s.size())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
print(s.size())

class Queue():
  def __init__(self):
    print("\nHere is Queue Class ---------")
    self.my_queue = []
  #adds a new item to the rear of the queue.
  #Running time: O(n); as the list grow the longer the program take longer to go through the list and insert to the front.
  def enqueue(self, useritem):
    print("enqueuing")
    self.my_queue.insert(0, useritem)
  # tests  to  see  whether  the  Queue  is  empty. 
  # Running Time: O(1) or constant time because python len function take constant time to determine the size of the list and check against 0
  def isEmpty(self):
    print("Empty?")
    if len(self.my_queue) == 0:
      return True
    return False
  # remove first element that enter the list
  # Running Time: O(1); first inserted element is the last element in the list, therefore no shifting element is require
  def dequeue(self):
    print("dequeueing")
    try:  
      return self.my_queue.pop()
    except LookupError:
      return "Sorry, No index found! Possibly Empty.."
  # returns the number of items on the stack. 
  # Running Time: O(1) or constant time because python len function take constant time to determine the size of the list
  def size(self):
    print("size: ")
    return len(self.my_queue)
  #printing the elements of the queue
  # O(1)
  def __str__(self):
    print("current list: ")
    return str(self.my_queue)

q = Queue()
print(q.isEmpty())
q.enqueue("hi")
q.enqueue("dog")
q.enqueue(1)
print(q)
print(q.size())
print(q.isEmpty())
q.enqueue(8.4)
print(q.size())
print(q)
print(q.dequeue())
print(q)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
q.enqueue("NewItem")
q.enqueue("Meat")
print(q)
print(q.size())

class Deque():
  def __init__(self):
    print("\nHere is Deque Class -----------------------")
    self.my_deque = []
  #adds a new item to the front of the deque. 
  #Running time: O(1) or constant time, add element to the front which is the last item in the list
  def addFront(self, user_item):
    print("adding front of deque")
    self.my_deque.append(user_item)
  #adds  a  new  item  to  the  rear  of  the  deque. 
  #Running time: O(n); as the list grow the longer the program take longer to go through the list and insert to the rear or front of the list.
  def addRear(self, user_item):
    print("adding rear of deque")
    return self.my_deque.insert(0, user_item)
  # removes the front item from the deque. 
  # Running Time: O(1); remove front of the list is the last element in the list, therefore no shifting element is require
  def removeFront(self):
    print("removing front of deque")
    if len(self.my_deque) != 0:
      return self.my_deque.pop()
    else:
      return "No item in list"
  # removes the rear item from the deque.  
  # Running Time: O(n); the rear of the list is the first element in the list, therefore 
  # elements are required to be shifted
  def removeRear(self):
    print("removing rear of deque")
    if len(self.my_deque) != 0:
      return self.my_deque.pop(0)
    else:
      return "No item in list"
  # tests  to  see  whether  the  stack  is  empty. 
  # Running Time: O(1) or constant time because python len function take #constant time to determine the size of the list and check against 0
  def isEmpty(self):
    print("Empty?")
    if len(self.my_deque) == 0:
      return True
    return False
  # returns the number of items on the stack. 
  # Running Time: O(1) or constant time because python len function take constant time to determine the 
  def size(self):
    print("size: ")
    return len(self.my_deque)
  # print out list
  # O(1) 
  def __str__(self):
    print("Current list")
    return str(self.my_deque)

d = Deque()
print(d.isEmpty())
d.addFront(1)
d.addFront(2)
d.addFront(3)
d.addRear(7)
d.addRear(8)
d.addRear(9)
print(d.size())
print(d)
print(d.isEmpty())
print(d.removeFront())
print(d.removeFront())
print(d.removeRear())
print(d.removeRear())
print(d.size())
print(d)

class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
class LinkedList():
  def __init__(self):
    print("\nSingly LinkedList ---------------------")
    self.head = None
  #adds a new item to the beginning of the list
  #Run-time: O(1); usning head node pointer
  def add(self, item):
    print("adding new node")
    new_node = Node(item)
    new_node.next = self.head
    self.head = new_node
  #removes the item from the list.
  # Run-time : O(n), search each node to match the item in order to remove it
  def remove(self, item):
    print("removing node")
    try:
      current_Node = self.head
      #check if head is the item to be delete
      if (current_Node and current_Node.data == item):
        self.head = current_Node.next
        current_Node = None
        return
      previous_Node = None
      #search for key to be delete
      while current_Node and current_Node.data != item:
        previous_Node = current_Node
        current_Node = current_Node.next
      previous_Node.next = current_Node.next
      current_Node = None
    except AttributeError:
      print("Item don't exist; try again")
  #searches for the item in the list
  #Run-Time: O(n), seach each node to match the item
  def search(self, item):
    print("searching node")
    current_Node = self.head
    while (current_Node is not None):
      if current_Node.data == item:
        return True
      else:
        current_Node = current_Node.next
    return False
  #tests to see whether the list is empty.
  #Runtime: O(1)
  def isEmpty(self):
    print("Empty? ")
    if (self.head == None):
      return True
    return False
  #returns the number of items in the list. 
  # Run-time: O(n); loop the amount of time depend on the size of the loop
  def size(self):
    current = self.head
    count = 0
    while (current is not None):
      count += 1
      current = current.next
    return count
  #adds a new item to the end of the list making it the last item in the collection.
  #Run-time: O(n), loop through the loop until the pointer points to None
  def append(self, item):
    print("appending..")
    new_node = Node(item)
    # if list if empty
    if self.head is None:
      self.head = new_node
      return
    last_node = self.head
    #list not empty
    while last_node.next is not None:
        last_node = last_node.next 
    last_node.next = new_node
   #returns the position of item in the list.
   # Run-Time: O(n); loop through the loop as long as the pointer is not none and continue to loop until it finds the item in list
  def index(self, item):
    print("finding index of item...")
    current_Node = self.head
    index = 0
    while (current_Node is not None):
      if current_Node.data == item:
        return index
      else:
        current_Node = current_Node.next
        index += 1
    return "index for item doesn't exist"
  #adds a new item to the list at position pos.
  # Run-Time: O(n); loop through the list as long as pointer is not none and keep track of each count until count == pos
  def insert(self,pos,item):
    print("inserting item to position")
    new_node = Node(item)
    current_node = self.head
    counter = 1
    if(pos < 0) | (self.size() < pos):
      print("Sorry, List too short")
    if(pos == 0):
      new_node.next = self.head
      self.head = new_node
    while current_node.next is not None:
      if counter == pos:
        new_node.next = current_node.next
        current_node.next = new_node
        break
      counter += 1
      current_node = current_node.next
  # remove the last item in link-list
  # Run-Time: O(n); loop through list until the last node pointer point to none
  def popEnd(self):
    print("popping at the end")
    if (self.head == None):
      return "List is empty"
    else:
      current_Node = self.head
      previous_Node = None
      while(current_Node.next != None):
        previous_Node = current_Node
        current_Node = current_Node.next
      if(previous_Node == None): # list contain 1 item
        self.head = None
        return current_Node.data
      else:
        previous_Node.next = None
        return current_Node.data
  #removes and returns the item at position pos.
  #Run-Time = O(n); loop through the list to determine the previous node of the node to be deleted
  def pop(self, pos):
    print("popping at position")
    # if empty list
    if self.head is None:
      return 'This is an empty list'
    # if the pos is neg or bigger than list size
    if pos < 0 or pos >= self.size():
      return "Pos is either negative or bigger than the list size, try again"
    current_Node = self.head
    # If pos is index 0 
    if pos == 0: 
      self.head = current_Node.next
      return current_Node.data
      current_Node = None
    # Find previous node of the node to be deleted 
    for i in range(pos-1): 
      current_Node = current_Node.next
      if current_Node is None: 
        break

    temp = current_Node.next.data
    next = current_Node.next.next 
    current_Node.next = None
    current_Node.next = next 
    return temp

  #print nodes in list
  #Run-time: O(n)
  def printInfo(self): 
    print("current list: ")
    temp_list = []
    current = self.head 
    while (current is not None):
      #print(current.data)
      temp_list.append(current.data)
      current = current.next
    print(temp_list)

l = LinkedList()
print(l.isEmpty())
l.add("kk")
l.add(10)
l.add(20)
l.add(30)
l.add(40)
l.add(50)
l.add(60)
l.printInfo()
l.remove("kk")
l.printInfo()
print(l.search(60))
print(l.search("Bobby"))
print("size:")
print(l.size())
print(l.isEmpty())
l.append("LOL")
l.printInfo()
print(l.index(40))
l.insert(5, 99)
l.insert(0, 88)
l.printInfo()
print("size")
print(l.size())
print(l.popEnd())
print(l.pop(2))
l.printInfo()

class NodeDLL:
  def __init__(self, user_data):
    self.data = user_data
    self.prev = None
    self.next = None
class DoublyLinkedList():
  def __init__(self):
    print("\nHere is Doubly LinkedList list------------------------------")
    self.head = None
    self.tail = None
  #adds a new item to the beginning of the list
  #Run-Time: O(1), insert item using head, don't have to go through list
  def add(self, item):
    print("adding node...")
    new_node = NodeDLL(item)
    current_node = self.head
    if self.head == None:
      self.head = new_node
      self.head.prev = None
      self.tail = new_node
      self.tail.next = None
    else:
      self.head.prev = new_node
      self.head = new_node
      self.head.next = current_node
      self.head.prev = None    
  #removes the item from the list.
  #Run-Time: O(n), must loop through to find the item to remove
  def remove(self, item):
    print("Removing item..")
    try:
      current = self.head
      #list empty
      if current is None:
        return "List is empty"
      #first item
      elif current.data == item:
        self.head = current.next
        self.head.prev = None
      #last item
      elif self.tail.data == item:
        self.tail = self.tail.prev
        self.tail.next = None
      #any item; not first or last
      #search for key to be delete
      previous_Node = None
      #search for key to be delete
      while current and current.data != item:
        previous_Node = current
        current = current.next
      previous_Node.next = current.next
      nxt_node = current.next
      nxt_node.prev = previous_Node
      current = None
    except AttributeError:
      print("Item don't exist; try again")
  #searches for the item in the list
  #Run-time: O(n); loop through list to find item
  def search(self, item):
    print("searching (exist?)")
    current_Node = self.head
    while (current_Node is not None):
      if current_Node.data == item:
        return True
      else:
        current_Node = current_Node.next
    return False
  #tests to see whether the list is empty.
  # Run-time: O(1)
  def isEmpty(self):
    if self.head == None:
      return True
    return False
  #returns the number of items in the list. 
  #Run-time: O(n); loop through list and counter the nodes
  def size(self):
    current = self.head
    count = 0
    while (current is not None):
      count += 1
      current = current.next
    return count
  #adds a new item to the end of the list making it the last item in the collection.
  #Run-time: O(1), add at thend end using tail; faster than singly linkedlist
  def append(self, item):
    print("appending to end...")
    new_node = NodeDLL(item)
    # if list is empty
    if self.head == None:
      self.head = new_node
      self.head.prev = None
      self.tail = new_node
      self.tail.next = None
    else:
      self.tail.next = new_node
      new_node.prev = self.tail
      self.tail = new_node
      self.tail.next = None
   #returns the position of item in the list.
   # Run-time: O(n); loop though to find item
  def index(self, item):
    print("finding index...")
    current_Node = self.head
    index = 0
    while (current_Node is not None):
      if current_Node.data == item:
        return index
      else:
        current_Node = current_Node.next
        index += 1
    return "index for item doesn't exist"
  #adds a new item to the list at position pos.
  #Run-time: O(n); use loop to find the position and add counts
  def insert(self,pos,item):
    print("inserting item at pos")
    new_node = NodeDLL(item)
    current_node = self.head
    counter = 1
    if(pos < 0) or ( pos > self.size()):
      print("Sorry, List too short or pos is negative")
    if self.isEmpty():
      self.head = new_node
      self.tail = new_node
      self.head.prev = None
      self.tail.next = None
    if(pos == 0):
      self.head.prev = new_node
      self.head = new_node
      self.head.next = current_node
      new_node.prev = None
    current_node = self.head
    while current_node.next is not None:
      #last position in list
      if (pos == self.size()):
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node
        self.tail.next = None
        break
      elif (counter == pos):
        stored_node = current_node.next
        new_node.next = stored_node
        stored_node.prev = new_node
        current_node.next = new_node
        new_node.prev = current_node
        break
      counter += 1
      current_node = current_node.next
  # remove the last item in link-list
  # Run-time: O(1); remove using the tail, faster than singly linkedlist
  def popEnd(self):
    print("popping end")
    #list empty
    if (self.head == None):
      return "Sorry, List is empty...."
    if(self.head.next == None): # list contain 1 item
        temp = self.head.data
        self.head = None
        self.tail = None
        return temp
    else:
      prev_node = self.tail.prev
      current_last = self.tail
      if self.tail.next == None:
        self.tail = prev_node
        temp = current_last.data
        prev_node.next = None
        current_last = None
    return temp
  #removes and returns the item at position pos.
  # Run-time: O(n); remove using the loop to find position
  def pop(self, pos):
    print("popping at pos")
        #if list is empty
    if self.head is None:
      return 'This is an empty list'
    #if pos is neg or bigger than list size
    if pos < 0 or pos >= self.size():
      return "Pos is either negative or bigger than the list size, try again"
    
    current_Node = self.head
    # If pos is index 0
    if pos == 0:
      temp = current_Node.data
      self.head = self.head.next
      self.head.prev = None
      self.head.next = current_Node.next.next
      current_Node = None
      return temp
    else:
      for i in range(pos -1):
        current_Node = current_Node.next
      nxt = current_Node.next.next
      if nxt is None:
        temp = current_Node.next.data
        current_Node.next = None
        return temp
      else:
        temp = current_Node.next.data
        node_del = nxt.prev
        current_Node.next = nxt
        nxt.prev = current_Node
        node_del = None
        return temp

  #print nodes in list
  #Run-time: O(n)
  def printInfo(self): 
    print("current list: ")
    temp_list = []
    current = self.head 
    while (current is not None):
      #print(current.data)
      temp_list.append(current.data)
      current = current.next
    print(temp_list)

d = DoublyLinkedList()
print("Empty?")
print(d.isEmpty())
d.add("hi")
d.add(10)
d.add(20)
d.add(30)
d.add(40)
d.add(50)
d.printInfo()
d.append("sick")
d.printInfo()
print("size")
print(d.size())
print("Empty? ")
print(d.isEmpty())
d.remove(20)
d.printInfo()
print(d.search("sick"))
print(d.search(69))
d.printInfo()
print("size: ")
print(d.size())
d.insert(3, "insert")
d.printInfo()
print(d.popEnd())
print(d.popEnd())
print(d.pop(2))
d.printInfo()
print(d.popEnd())
d.insert(0, "AR4")
d.insert(10, "gooo")
d.printInfo()
d.append("hiiiiiiii")
d.printInfo()
print(d.popEnd())
print(d.popEnd())
print(d.popEnd())
print(d.popEnd())
print(d.popEnd())
print(d.popEnd())
d.printInfo()

"""6.  Do you think that python’s internal representation of a list is a linked-list, a doubly-linked list,
or something else? Why or why not? Insert a comment in your code to explain your thinkingabout this.
I think that python's internal representation of a list is like an array. I believe this because in python lists, 
we do not have to keep track of the head or tails of the node and its pointer. Also in regular list, the program iterate 
over each item as you perform remove item, insert item, pop item, etc whereas with linked list, the program traverse 
to each node.

7. Now that you’ve implemented linked lists and doubly-linked lists, you have the option of using these in place of 
python lists inside your implementation of stacks, queues, and dekes. For each of these, explain which type of list 
(python list, linked list, or doubly-linked list)should give the best Big Oh running time in a comment.

I believe that the type of list (python list, linked list, or doubly-linked list)should give the
best Big Oh running time is doubly-linked list because a singly-linked list can only give the best Big Oh 
running time if the value is to be accessed in the first element. Python lists like stacks, queues, and dekes uses
iteration to get to the beginning and that takes more time as the list's size increases. Therefore, I believe that
the doubly linked list can give best Big Oh running if the programmer is operating on either the first or the last element.
Also because each elements will be keep track of by the nodes and the pointers, operations such as searching can be done
with less time compare to the python lists.  

"""