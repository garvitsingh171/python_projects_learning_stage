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
node7 = Node(17)
node8 = Node(18)
node9 = Node(19)
node10 = Node(20)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9
node9.next = node10

slow = node1
fast = node1

while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
print(slow.data)