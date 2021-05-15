#Assignment 4- Searching ; Touchsada Jan On
def recur_search(sorted_list, lower, upper, item):
    if upper >= lower:
        mid = lower + ((upper - lower) // 2)
        if sorted_list[mid] == item:
            return True
        elif sorted_list[mid] > item:
            return recur_search(sorted_list, lower, mid - 1, item)
        else:
            return recur_search(sorted_list, mid + 1, upper, item)
    return "item not in the list"

def search_sorted_list(sorted_list , item):
  return(recur_search(list, 0, len(list)-1, item))

list = [1,5,7,9,10,11,18]
print("Recursion--------------------")
print(search_sorted_list(list, 11))
print(search_sorted_list(list, 44))
print(search_sorted_list(list, 18))
print(search_sorted_list(list, 1))


class HashList:
  length = 0
  list = []
  #create a list with given length and create open slot
  def __init__(self, user_length):
    self.length = user_length
    self.list = ["None"]* user_length
  #tells you which slot the item is assigned to.
  def hashfunction(self, item):
    slot = item % self.length
    return slot
  # adds the given item to the list. If the list is full, it throws an error.
  def put(self, item):
    # get the slot position
    slot = self.hashfunction(item)
    count_col = 0 #counter for possible collision
    # check open slot in the list
    while self.list[slot] != "None":
      #if list current position is not open slot
      slot += 1
      slot = slot % self.length
      count_col += 1 # count how many slot is not empty
      #exception for when collision occur
      if (count_col == self.length):
        raise Exception("The HashList is full")
    # found the slot, then add item to list
    self.list[slot] = item
  #returns True if the given item is in the list,#and False otherwise. Make sure
  #your method still works in the extreme case #in which the list is entirely full and the #given
  #item isn’t in the list.
  def contains(self,item):
    # get the slot position
    slot = self.hashfunction(item)
    count_col = 0
    #found the item
    if self.list[slot] == item:
      return True
    #will loop until it find the item or find an open slot, which mean item isn't there
    while self.list[slot] != "None":
      if self.list[slot] != item:
        slot +=1
        slot = slot % self.length
      count_col +=1
      #at the end of the list and not found item
      if (count_col == self.length):
        return False
    return False
  #returns a list of all items in the HashList.
  def items(self):
    return self.list

print("HashList----------------")
hash = HashList(5)
#Adding element to the hash list
hash.put(5)
#Displaying haslist
print(hash.items())
#Adding more elements to the list
hash.put(11)
hash.put(18)
hash.put(24)
hash.put(125)
#Displaying hashlist
print(hash.items())
#Check for elements are in the hash list or not
print(hash.contains(8))
print(hash.contains(67))
print(hash.contains(24))
# below will throws an error because the list is full!
#hash.put(33)
"""
3. In a comment, explain the running times of the HashList methods in the best-case scenario
in which there are no collisions, and in the worst-case scenario in which there are many
collisions.
  - HashList method takes constant running time or O(1) in both best-case and worse-case scenerio
  - hashfunction method also takes constant running time or O(1) in both best-case and worse-case scenerio
  - put method takes constant running time or O(1) for best-case scenerio with no collision and linear running time 
  or O(n) for worse case scenerio with collisions
  - contain method also takes constant running time or O(1) for best-case scenerio with no collision and linear 
  running time or O(n) for worse case scenerio with collisions items method takes constant running time or O(1) in 
  both best-case and worse-case scenerio
4. Also explain how we would have to modify things to convert our HashList into a dictionary.

First, we will have to use two lists in order to create a hash table for the dictionary. 
The first list can be the slots of the data from the HashList, which will be the key for that corresponding data. 
The second list can be the data values. When we look up a key, the corresponding position in the data list will 
hold the associated data value.


"""  
