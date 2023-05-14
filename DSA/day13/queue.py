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