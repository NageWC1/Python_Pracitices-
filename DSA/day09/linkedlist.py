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
            node = Node(data, None)
            self.head = None
        
        itr = self.head 
        while itr.next:
            itr = itr.next 
        
        node = Node(data, None)
        itr.next = node

    def print(self):
        l_str = ""
        itr = self.head 
        while itr:
            l_str += str(itr.data) + "-->"
            itr = itr.next
        print(l_str)

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
    def insert_after_at(self, ind, data):
        itr = self.head 
        count = 0 
        while itr:
    
            if count == ind:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next 
            count += 1

    def insert_before_at(self, ind, data):
        itr = self.head 
        count = 0
        while itr:
            if ind == 0:
                node = Node(data, self.head)
                self.head = node
                break
            
            if count == ind - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            
            itr = itr.next 
            count += 1
if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_beggining(10)
    l.insert_at_beggining(11)
    l.insert_at_beggining(12)
    l.insert_at_beggining(13)
    l.insert_at_beggining(14)
    l.insert_at_beggining(15)
    l.print()
    l.insert_at_end(100)
    l.insert_at_end(101)
    l.insert_at_end(102)
    l.insert_at_end(103)
    l.print()
    l.remove_at(1)
    l.remove_at(0)
    l.print()
    l.insert_after_at(0,1999)
    l.print()
    l.insert_before_at(0,9999)
    l.print()