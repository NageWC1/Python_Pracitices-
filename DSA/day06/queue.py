from collections import deque 

class queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueu(self, data):
        self.buffer.appendleft(data)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)  == 0

    def size(self):
        return len(self.buffer)

if __name__ == "__main___":
    q =queue()
    q.dequeue(10)
    q.dequeue(12)
    q.dequeue(13)
    q.dequeue(14)
    q.dequeue(15)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())