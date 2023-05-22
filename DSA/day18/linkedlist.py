class Node:
    def __init__(self, data:None, next:None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_beg(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_end(self, data):
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


    def print(self):
        l_str = ""
        itr = self.head
        while itr:
            l_str += str(itr.data) + "-->"
            itr = itr.next
        print(l_str)

if __name__ == "__main__":
    pass