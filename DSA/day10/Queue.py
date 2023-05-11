from collections import deque

class Queueu:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, data):
        pass

    def dequeue(seflf):
        pass 

    def size(self):
        pass 

    def is_empty(self):
        pass

if __name__ == "__main__":
    q = Queueu()
    q.enqueue(10)
    q.enqueue(12)
    q.enqueue(13)
    q.enqueue(14)
    q.enqueue(15)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())