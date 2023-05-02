class Node:
    def __init__(self,data:None,next:None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_beggining(self,data):
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

    def print(self):
        l_str = ""
        itr = self.head

        while itr:
            l_str += str(itr.data) + "-->"
            itr = itr.next
        print(l_str)

    def delete_at(self, ind):
        itr = self.head
        count = 0 
        while itr:
            if ind == count:
                self.head = itr.next
                break
            
            if count == ind - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1

if __name__ == "__main__":
    ll = LinkedList()

    ll.insert_at_beggining(10)
    ll.insert_at_beggining(11)
    ll.insert_at_beggining(12)
    ll.insert_at_end(50)
    ll.insert_at_end(51)
    ll.insert_at_end(52)
    ll.delete_at(0)
    ll.delete_at(2)
    ll.print()
