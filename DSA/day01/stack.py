from collections import deque

class Stack:
    def __init__(self):
        self.buffer = deque()
    
    def insert(self,data):
        self.buffer.append(data)
    
    def remove(self):
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer) ==  0

if __name__ == "__main__":
    s = Stack()
    s.insert(10)
    s.insert(11)
    s.insert(12)
    s.insert(13)
    print(s.remove())
    print(s.remove())
    print(s.remove())
    print(s.is_empty())
    print(s.size())