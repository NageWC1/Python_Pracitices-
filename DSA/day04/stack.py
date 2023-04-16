from collections import deque

class Stack:
    def __init__(self):
        self.stack = deque()

    def insert(self, data):
        self.stack.append(data)

    def delete(self):
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) ==  0 
    
    def print(self):
        st = ''
        for data in self.stack:
            st += str(data) + '|'
        print(st)

if __name__ == "__main__":
    s = Stack()
    s.insert(10)
    s.insert(11)
    s.insert(12)
    s.insert(13)
    s.is_empty()
    print(s.size())
    print(s.delete())
    s.print()