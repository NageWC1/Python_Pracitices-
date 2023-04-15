class Node:
    def __init__(self,data:None,next:None):
        self.data = data
        self.next = next 
    


class LinkedList:
    def __init__(self, head:None):
        self.head = head

    def insert_at_beggining(self, data):
        pass

    def insert_at_end(self, data):
        pass

    def insert_at_ind(self, data):
        pass

    def print(self):
        pass
    
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beggining(12)
    ll.insert_at_beggining(13)
    ll.insert_at_beggining(14)
    ll.insert_at_end(100)
    ll.insert_at_end(101)
    ll.insert_at_end(102)