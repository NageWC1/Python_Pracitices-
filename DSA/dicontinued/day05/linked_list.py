class Node:
    def __init__(self, data:None,next:None):
        self.data = data
        self.next = next
    
class LinkedList:
    def insert_at_beggining(self, data):
        pass

    def insert_at_end(self, data):
        pass 

    def print(self):
        pass

    def remove_at(self, ind):
        pass

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_beggining(10)
    l.insert_at_beggining(11)
    l.insert_at_beggining(12)
    l.insert_at_beggining(13)
    l.insert_at_end(100)
    l.insert_at_end(101)
    l.insert_at_end(102)
    l.insert_at_end(103)
    l.print()
    l.remove_at(4)
    l.print()

