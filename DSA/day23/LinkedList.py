class Node:
    def __init__(self, data:None, next:None):
        self.data = data 
        self.next = next 
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
        
        itr = self.head
        while itr.next:
            itr = itr.next 
        itr.next = Node(data, None)

    def insert_after_at(self, ind, data):
        count = 0
        itr = self.head 
        while itr:
            if count == ind:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next 
            coun += 1 

    def print(self):
        pass

    def remove_at(self, ind):
        pass

if __name__ == "__main__":
    l = LinkedList()