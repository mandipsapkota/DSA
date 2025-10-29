class Node:
    def __init__(self,value):
        self.next = None
        self.data = value

a = Node(10)
b = Node(20)
c = Node(30)
a.next = b
b.next = c

# a-> b -> c Simply Linked List created

print(a.data)
print(a.next.data)
print(a.next.next.data)