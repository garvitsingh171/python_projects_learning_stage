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

while current is not None:
    if current.data == 15:
        print(True)
    else:
        print(False)
    current = current.next