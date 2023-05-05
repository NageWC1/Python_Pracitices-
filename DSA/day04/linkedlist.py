class Node:
    def __init__(self, data:None, next:None):
        data = data 
        next = next 

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beggining(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beggining(data)
        
        itr = self.head 
        while itr.next:
            itr = itr.next 
        node = Node(data, None)
        itr.next = node
    
    def remove_at(self, ind):
        count = 0 
        itr = self.head 
        while itr:
            if ind == 0:
                self.head = itr.next
                break 

            if count == ind - 1:
                itr.next = itr.next.next 
                break 
            count += 1
            itr = itr.next
        
    def print(self):
        l_str = ""
        itr = self.head 
        while itr:
            l_str += str(itr.dat) + "-->"
            itr = itr.next
        print(l_str)