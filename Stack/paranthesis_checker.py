class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0
    
    def top(self):
        self.stack[-1]
    
    def push(self, bracket):
        if bracket == '(' or bracket == '{' or bracket == '[':
            self.stack.append(bracket)
        elif not self.isEmpty():
            if bracket == ')' or bracket == '}' or bracket == ']':
                if self.top() == bracket:
                    self.stack.append(bracket)
                    return 'Balanced'
                else:
                    return 'Not Balanced. Re-enter the bracket.'
        else:
            return 'Stack is empty.'
        
mystack = Stack()

print(mystack.push('('))
print(mystack.push('['))
print(mystack.push('{'))
print(mystack.push('}'))
print(mystack.push(']'))