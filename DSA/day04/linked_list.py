class Node:
    def __init__(self, data:None, next:None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 

        itr = self.head 
        while itr.next:
            itr = itr.next
        node = Node(data, None)
        itr.next = node
    
    def print(self):
        l_str = ''
        itr = self.head 
        while itr:
            l_str += str(itr.data) + '-->'
            itr = itr.next
        print(l_str)
    
    def remove_at(self, ind):
        pass

    def insert_at_index(self, ind, data):
        pass

    def list_size(slelf):
        pass

    def insert_after(self,ind, data):
        pass

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_beggining(10)
    ll.insert_at_beggining(11)
    ll.insert_at_beggining(12)
    ll.insert_at_end(23)
    ll.insert_at_end(24)
    ll.insert_at_end(25)
    ll.print()