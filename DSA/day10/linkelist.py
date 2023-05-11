class Node:
    def __init__(self, data:None, next:None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_bg(self, data):
        pass

    def insert_at_end(self, data):
        pass

    def remove_at(self, ind):
        pass

    def print(self):
        pass

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_bg(10)
    l.insert_at_bg(11)
    l.insert_at_bg(12)
    l.insert_at_bg(13)
    l.print()
    l.insert_at_end(101)
    l.insert_at_end(102)
    l.insert_at_end(103)
    l.insert_at_end(104)
    l.print()