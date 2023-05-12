class Node:
    def __init__(self, data:None, next:None):
        self.data = data
        self.next = data
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self, data):
        pass 

    def insert_at_end(self, data):
        pass

    def remove_at(self, data):
        pass

    def print(self):
        pass

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_beg(10)
    l.insert_at_beg(11)
    l.insert_at_beg(12)
    l.insert_at_beg(13)
    l.print()
    l.insert_at_end(100)
    l.insert_at_end(101)
    l.insert_at_end(102)
    l.insert_at_end(103)
    l.print()
    l.remove_at(0)
    l.remove_at(3)
    l.print()