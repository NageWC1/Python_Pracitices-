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
            self.head = Node(data, None)
        
        itr = self.head 
        while itr.next:
            itr = itr.next 
        itr.next = Node(data, None)

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
            itr = itr.next 
            count += 1


    def print(self):
        l_str = ""
        itr = self.head 
        while itr:
            l_str += str(itr.data) + "-->"
            itr = itr.next 
        print(l_str)


    def insert_before_at(self, ind, data):
        count = 0
        itr = self.head 
        while itr:
            if ind == 0:
                node = Node(data, self.head)
                self.head = node
                break
            if count == ind - 1:
                node = Node(data, itr.next)
                itr.next  = node
                break
            itr = itr.next
            count += 1

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_beg(10)
    l.insert_at_beg(11)
    l.insert_at_beg(12)
    l.insert_at_beg(13)
    l.insert_at_beg(14)
    l.print()
    l.insert_at_end(100)
    l.insert_at_end(101)
    l.insert_at_end(102)
    l.insert_at_end(103)
    l.insert_at_end(104)
    l.print()
    l.insert_before_at(0, 1999)
    l.insert_before_at(3,1333)
    l.print()
    l.remove_at(4)
    l.remove_at(5)
    l.print()