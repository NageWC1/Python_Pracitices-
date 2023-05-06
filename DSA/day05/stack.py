from collections import deque

class StacK:
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

if __name__ == "__main__":
    s = StacK()
    s.insert(10)
    s.insert(11)
    s.insert(12)
    s.insert(13)
    s.insert(14)
    print(s.size())
    print(s.pop())
    print(s.pop())
    print(s.size())
    print(s.is_empty())
    