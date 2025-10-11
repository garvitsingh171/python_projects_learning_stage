class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(11)
node2 = Node(12)
node3 = Node(13)
node4 = Node(14)
node5 = Node(15)
node6 = Node(16)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

current = node1
previous = None

value = 14

while current is not None:
    if current.data == 14:
        if previous is None:
            node1 = current.next
        else:
            previous.next = current.next
        break
    previous = current
    current = current.next