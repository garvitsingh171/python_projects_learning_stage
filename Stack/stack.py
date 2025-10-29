class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack Underflow"
        else:
            return self.stack.pop()
    
    def top(self):
        if self.isEmpty():
            return "Stack Underflow"
        else:
            return self.stack[-1]
        
    def size(self):
        return len(self.stack)
    
mystack = Stack()

mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)
mystack.pop()
mystack.pop()
mystack.push(5)
mystack.push(6)
mystack.push(7)
mystack.pop()
mystack.top()

print(mystack.stack)
print(mystack.top())
print(mystack.isEmpty())