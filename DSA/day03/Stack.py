from collections import deque 

class Stack:
    def __init__(self):
        self.buffer = deque()
    
    def insert(self, data):
        self.buffer.append(data)
    
    def pop(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer) == 0
    