from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueu(self, data):
        self.buffer.appendleft(data)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)
    
if __name__ == "__main__":
    q = Queue()
    q.enqueu(10)
    q.enqueu(11)
    q.enqueu(12)
    q.enqueu(13)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
