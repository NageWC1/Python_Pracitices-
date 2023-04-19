class Node:
    def __init__(self, data:None, next:None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count 
    
    def insert_after_ind(self,ind,data):
        if ind < 0 or ind >= self.get_length():
            raise Exception("The index is wrong")
        
        itr = self.head 
        count = 0 
        while itr:
            if count == ind:
                node = Node(data, itr.next)
                itr.next = node 
            itr = itr.next 
            count += 1
    def remove_at_ind(self,ind):
        if ind < 0 or ind >= self.get_length():
            raise Exception("The index is wrong")
        if ind == 0:
            self.head = None

        itr = self.head 
        count = 0
        while itr:
            if count == ind - 1:
                itr.next = itr.next.next
            itr = itr.next
            count += 1
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def print(self):
        if self.head is None:
            print("the list ins empty")
            return 
        itr = self.head 
        l_str = ''
        while itr:
            l_str += str(itr.data) +'-->'
            itr = itr.next
        print(l_str)

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beginning(10)
    ll.insert_at_beginning(11)
    ll.insert_at_beginning(12)
    ll.print()
    ll.insert_after_ind(1,100)
    ll.print()
    ll.remove_at_ind(1)
    ll.print()
    ll.remove_at_ind(2)
    ll.print()
    ll.insert_at_end(999)
    ll.print()
    
