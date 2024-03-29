class Node:
    def __init__(self, data:None, next:None):
        self.data = data 
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def insert_at_end(self,data):
        if self.head is None:
            node = Node(data, None)
            self.head = node
        
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None) 
    
    def remove_at(self, ind):
        count = 0
        itr = self.head 

            
        while itr:
            if ind == 0:
                self.head = itr.next
                break 

            if count == ind - 1:
                itr.next = itr.next.next

            itr = itr.next
            count += 1

    def print(self):
        itr = self.head 
        l_str = ""
        while itr: 
            l_str += str(itr.data) + "-->"
            itr = itr.next 
        print(l_str)
    
    def insert_after_at(self, data, ind):
        itr = self.head 
        count = 0

        while itr:
            if count == ind:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

if __name__ == "__main__":
    l = LinkedList()
    l.insert_at_begining(10)
    l.insert_at_begining(11)
    l.insert_at_begining(12)
    l.insert_at_begining(13)
    l.insert_at_end(100)    
    l.insert_at_end(102)    
    l.insert_at_end(103)
    l.print()
    l.remove_at(0)
    l.remove_at(3)
    l.print()    
    l.insert_after_at(10000,0)
    l.print()