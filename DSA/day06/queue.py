from collections import deque 

class Queue:
    def __init__(self):
        self.buffer = deque()
        print("the queue created")
    
    def enqueu(self, data):
        self.buffer.appendleft(data)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)  == 0

    def size(self):
        return len(self.buffer)

if __name__ == "__main__":
    q =Queue()
    q.enqueu(10)
    q.enqueu(12)
    q.enqueu(13)
    q.enqueu(14)
    q.enqueu(15)
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())
    print(q.is_empty())