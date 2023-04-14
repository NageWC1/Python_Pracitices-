from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def pop(self):
        return self.buffer.pop()
    
    def size(self):
        return len(self.buffer)
    
    def isEmpty(self):
        return  len(self.buffer) == 0
    
if __name__ == "__main__":
    q  = Queue()

    q.enqueue(1)
    q.enqueue(12)
    q.enqueue(13)
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.isEmpty())


