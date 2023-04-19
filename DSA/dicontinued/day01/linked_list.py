# day one linked list practice
# this is represent individual element of the linked list 
class Node:
    def __init__(self, data:None, next:None):
        self.data = data 
        self.next = next #pointer to the next element

# this will point to the head of the linkedlist 
class linkedList:
    def __init__(self):
        self.head = None

    # Imagin im going to insert a value infront of the linked list 
    def insert_at_beggining(self,data):
        # create a node element and pass the head element as next element 
        # because the head should be now next to the new head element 
        node = Node(data, self.head)
        # and set that element as head now 
        self.head = node

    def print(self):
        if self.head is None:
            print("The linked is emepty")
            return 
        # initially we assign the head of the element to the itr so we can check the element 
        # has value in the next and find out 
        itr = self.head
        list_str  = ''
     
        while itr:
            list_str += str(itr.data) + '-->'
            itr = itr.next
        print(list_str)

    def insert_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        # automatically the while loop will be end when there is no next value, that mean we are now 
        # in the last element
        # we settting the last element as None becase the last element will not have the next element 
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        # wipping out all the values from previous linked list
        self.head = None
        for data in data_list:
            self.insert_end(data)
    
    def get_length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_ele_at_ind(self, ind):
        lenth = self.get_length()
        itr = self.head
        if ind >= lenth or ind < 0:
            raise Exception("the index is out of bound")
        count = 0
        if ind == 0:
                self.head = self.head.next
                return
        while itr:
            if count == ind - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
        
    def insert_at(self, ind,data):
            lenth = self.get_length()
            itr = self.head
            if ind >= lenth or ind < 0:
                raise Exception("the index is out of bound")
            
            if ind == 0:
                self.insert_at_beggining(data)

            
            itr = self.head
            count = 0
            while itr:
                if count == ind - 1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                count += 1

    def insert_after_at_ind(self,ind, data):
        if ind < 0 or ind >= self.get_length():
            raise Exception("the index is invalid")
        
        itr = self.head
        count = 0
        while itr:
            if count == ind:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def delete_by_value(self,value):
        itr = self.head 

        if self.head.data == value:
            self.head = None
        count = 0
        while itr: 
            if itr.data == value:
                self.remove_ele_at_ind(count)
                break

            itr = itr.next
            count += 1
                
    
if __name__ == "__main__":
    ll = linkedList()
    ll.insert_at_beggining(5)
    ll.insert_at_beggining(15)
    ll.insert_at_beggining(23)
    ll.insert_end(33)
    ll.insert_end(55)

    # check with entering list of values to the linked list 
    ll.insert_values([12,13,14,15])

    ll.insert_at(1,100)
    ll.print()
    ll.insert_at(4,1400)
    ll.print()
    ll.insert_after_at_ind(2,10)
    ll.print()
    ll.delete_by_value(10)
    ll.print()
    ll.delete_by_value(15)
    ll.print()
    print(ll.get_length()) 