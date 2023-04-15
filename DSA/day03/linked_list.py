class Node:
    def __init__(self,data:None,next:None):
        self.data = data
        self.next = next 
    


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        node = Node(data, self.head)

    def insert_at_end(self, data):
        itr = self.head

        if self.head == None:
            self.head = Node(data, None)
            return
        
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_at_ind(self,ind, data):
        count = 0 
        itr = self.head

        if ind == count:
            self.head = Node(data, self.head)

        while itr:
            if count == ind - 1:
                node = Node(data, itr.next)
                itr.next = node
            itr = itr.next 
            count += 1


    def print(self):
        l_str = ''
        itr = self.head
        while itr:
            l_str += str(itr.data) + "-->"
            itr = itr.next
        
        print(l_str)
    
if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beggining(12)
    ll.insert_at_beggining(13)
    ll.insert_at_beggining(14)
    ll.insert_at_end(100)
    ll.insert_at_end(101)
    ll.insert_at_end(102)
    ll.print()