from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def dequeue(self):
        return self.buffer.pop()
    
    def endqueue(self, val):
        self.buffer.appendleft(val)
    
    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer) == 0

if __name__ == "__main__":
    q = Queue()

    q.endqueue(10)
    q.endqueue(12)
    q.endqueue(13)
    q.endqueue(14)
    print(q.dequeue())
    print(q.is_empty())
    print(q.size())



