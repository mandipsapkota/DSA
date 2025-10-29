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

    # INSERT OPERATOR HERE 
    def insert(self,value,data):
        
        prev = self.head
        while prev is not None:
            if prev.data == value:
                break
            prev = prev.next

        if prev is None:
            print("Node not found")
        else:
            newNode = Node(data)
            newNode.next = prev.next
            prev.next = newNode

    def traverse(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end = " ")
            temp = temp.next
        print() #Just to end the line

    
            
myList = SinglyLinkedList()
myList.prepend(1)
myList.prepend(3)
myList.insert(3,4)
myList.traverse()
