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

current_index = 0
value_index = 3

while current is not None:
    if current_index == value_index:
        print(current.data)
    current_index += 1
    current = current.next

