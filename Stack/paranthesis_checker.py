class ParenthesisChecker:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def push(self, bracket):
        self.stack.append(bracket)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_balanced(self, text):
        pairs = {')': '(', '}': '{', ']': '['}
        self.stack.clear()
        for ch in text:
            if ch in '({[':
                self.push(ch)
            elif ch in ')}]':
                if self.is_empty() or self.top() != pairs[ch]:
                    return False
                self.pop()
        return self.is_empty()

    def returnf(self):
        return self.is_empt