from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
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
    print(q.size())
    q.enqueue(13)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.is_empty())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())