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
            node = Node(data, None)
            self.head = node
        itr = self.head 
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def print(self):
        pass

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

if __name__ == "__main__":
    l = LinkedList()
    