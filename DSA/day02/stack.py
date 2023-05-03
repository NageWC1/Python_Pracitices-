from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()
    
    def insert(self, data):
        self.stack.append(data)
    
    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack)  ==  0
    
if __name__ == "__main__":
    s = Stack()
    s.insert(10)
    s.insert(11)
    s.insert(12)
    s.insert(13)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.is_empty())