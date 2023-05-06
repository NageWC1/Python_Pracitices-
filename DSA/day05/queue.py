from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, data):
        self.buffer.appendleft(data)
    
    def dequeue(self, data):
        return  self.buffer.pop()
    
    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer) == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(14)
    q.enqueue(12)
    print(q.size())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())
    