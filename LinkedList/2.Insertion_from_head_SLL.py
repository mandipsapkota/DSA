class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertFromHead(self,value):
        newNode = Node(value)
        Node.next = self.head   
        self.head = newNode

myList = SinglyLinkedList()
myList.insert(2)
myList.insert(10)