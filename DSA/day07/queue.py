from collections import deque

class queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueu(self, data):
        self.buffer.appendleft(data)
    
    def dequeue(self):
        return self.buffer.pop()

    def size(self):
        return len(self.buffer)
    
    def is_empty(self):
        return len(self.buffer) == 0

if __name__ == "__main__":
    q = queue()
    q.enqueu(10)
    q.enqueu(11)
    q.enqueu(12)
    q.enqueu(13)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())
    