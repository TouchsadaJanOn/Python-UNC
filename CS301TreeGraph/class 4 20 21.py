class Node:
    def __init__(self, idata):
        self.Data = idata
        self.NextNodes = []
        self.Seen = False

    def __str__(self):
        output = "Node " + str(self.Data) + " -> "
        for n in self.NextNodes:
            output = output + str(n.getData()) + " "
        return output

    def getData(self):
        return self.Data

    def addChild(self, node):
        self.NextNodes.append(node)

    def getChildren(self):
        return self.NextNodes

    def setSeen(self, value):
        self.Seen = value

    def isSeen(self):
        return self.Seen
    

class Stack:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def empty(self):
        return self.data == []

class Queue:
    def __init__(self):
        self.data = []

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop(0)

    def empty(self):
        return self.data == []

class Tree:
    def __init__(self, inode):
        self.root = inode

    def DFSearch(self, item):
        searchstack = Stack()
        searchstack.push(self.root)
        while not searchstack.empty():
            currentnode = searchstack.pop()
            if currentnode.getData() == item:
                return True
            else:
                for child in currentnode.getChildren():
                    searchstack.push(child)
        return False

    def rDFS(self, item, node):
        print(node)
        if node.getData() == item:
            return True
        else:
            children = node.getChildren()
            if children == []:
                return False
            else:
                for child in children:
                    if self.rDFS(item, child):
                        return True
                return False

    def recursiveDFS(self, item):
        return self.rDFS(item, self.root)

    def BFSearch(self, item):
        searchstack = Queue()
        searchstack.push(self.root)
        while not searchstack.empty():
            currentnode = searchstack.pop()
            if currentnode.getData() == item:
                return True
            else:
                for child in currentnode.getChildren():
                    searchstack.push(child)
        return False

class DirectedGraph:
    def __init__(self):
        self.Nodes= []

    def addNode(self, node):
        self.Nodes.append(node)

    def reset(self):
        for node in self.Nodes:
            node.setSeen(False)

    def DFSearch(self, item, startnode):
        searchstack = Stack()
        searchstack.push(startnode)
        while not searchstack.empty():
            currentnode = searchstack.pop()
            if currentnode.getData() == item:
                return True
            else:
                for child in currentnode.getChildren():
                    if not child.isSeen():
                        searchstack.push(child)
                        child.setSeen(True)
        return False

    def BFSearch(self, item, startnode):
        searchstack = Queue()
        searchstack.push(startnode)
        while not searchstack.empty():
            currentnode = searchstack.pop()
            if currentnode.getData() == item:
                return True
            else:
                for child in currentnode.getChildren():
                    if not child.isSeen():
                        searchstack.push(child)
                        child.setSeen(True)
        return False

    def rDFS(self, item, node):
        if node.isSeen():
            return False
        node.setSeen(True)
        print(node)
        if node.getData() == item:
            return True
        else:
            children = node.getChildren()
            if children == []:
                return False
            else:
                for child in children:
                    if self.rDFS(item, child):
                        return True
                return False

  
            












            
