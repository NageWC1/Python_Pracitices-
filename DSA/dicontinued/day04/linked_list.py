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
        count = 0 
        itr = self.head 
        while itr:
            if count == ind - 1:
                itr.next = itr.next.next 
                break
            itr = itr.next
            count += 1


    def insert_at_index(self, ind, data):
        count = 0 
        itr = self.head 
        while itr:
            if count == ind - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next 
            count += 0

    def list_size(self):
        itr = self.head
        count = 0
        while itr:
            itr = itr.next
            count += 1
        print(count)

    def insert_after(self,ind, data):
        itr = self.head
        count = 0
        while itr:
            if count == ind:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next
            count += 1

if __name__ == "__main__":
    # All done 
    ll = LinkedList()
    ll.insert_at_beggining(10)
    ll.insert_at_beggining(11)
    ll.insert_at_beggining(12)
    ll.insert_at_end(23)
    ll.insert_at_end(24)
    ll.insert_at_end(25)
    ll.print()
    ll.remove_at(3)
    ll.print()
    ll.insert_after(2,100)
    ll.list_size()
    ll.print()