class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end = " ")
            temp = temp.next
        print() #Just to end the line
            
myList = SinglyLinkedList()
myList.prepend(1)
myList.prepend(3)

myList.traverse()
