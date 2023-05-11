from collections import deque

class Stack:
    def __init__(self):
        self.buffer = deque()
    
    def insert(self, data):
        pass

    def pop(self):
        pass

    def size(self):
        pass

    def is_empty(self):
        pass

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