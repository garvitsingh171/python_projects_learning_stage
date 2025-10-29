class Queue:

    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty.'
        else:
            self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            return self.queue[0]
    
    def size(self):
        return len(self.queue)
    
my_queue = Queue()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
print(my_queue.size())
my_queue.dequeue()
print(my_queue.size())
my_queue.enqueue(4)
my_queue.enqueue(5)
print(my_queue.size())
my_queue.enqueue(6)
my_queue.dequeue()
my_queue.dequeue()
print(my_queue.queue)
print(my_queue.size())