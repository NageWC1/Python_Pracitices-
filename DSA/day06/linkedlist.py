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
        node = Node(data, None)
        itr.next = node

    def remove_at(self, ind):
        itr = self.head 
        count = 0


        while itr:
            if ind == 0:
                self.head = itr.next
                break

            if count == ind - 1:
                itr.next = itr.next.next
            
            itr = itr.next 
            count += 1
    
    def print(self):
        l_str = ""
        itr = self.head
        while itr:
            l_str += str(itr.data) + "-->"
            itr = itr.next 
        print(l_str)

