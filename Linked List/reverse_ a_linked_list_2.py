class Node:

    def __init__(self,data):
        self.data = data
        self.next = None

node1 = Node(12)
node2 = Node(13)
node3 = Node(14)
node4 = Node(15)
node5 = Node(16)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

current = node1
previous = None

while current is not None:
    next = current.next
    current.next = previous
    previous = current
    current = next

current = previous
while current is not None:
    print(current.data, end=' -> ')
    current = current.next
print(None)