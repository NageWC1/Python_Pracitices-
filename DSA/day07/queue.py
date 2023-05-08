from collections import deque

class queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueu(self, data):
        self.buffer.appendleft(data)
    
    def dequeue(self):
        self.buffer.pop()

    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer) == 0
    