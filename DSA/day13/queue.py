from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, data):
        self.buffer.appendleft(data)
    
    def dequeu(self):
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)

    def is_empty(self):
        return len(self.buffer) == 0

if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(11)
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(14)
    print(q.dequeu())
    print(q.dequeu())
    print(q.dequeu())
    print(q.dequeu())
    print(q.size())
    print(q.is_empty())