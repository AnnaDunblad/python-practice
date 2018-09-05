### Python Data Structures



### Linked list #####
class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
                 
class LinkedList:
    def __init__(self):
         self.head = None
    def print_list(self):
        temp  = self.head
        while temp:
            print("Node data: {}".format(temp.data))
            temp = temp.next
            
    def insert_node_at_tail(self, data):
        temp = self.head
        while temp:
            if temp.next: #not at the tail
                temp = temp.next
            else: #at the tail
                temp.next = Node(data)
                return self.head
            
            
    def delete_node(self, value_to_delete):
        temp = self.head
        prev  =self.head
        
        while temp:
            if temp.data == value_to_delete:
                if temp is self.head:
                    self.head = temp.next
                    return self.head
                else:
                    prev.next = temp.next
                    return self.head
            prev  = temp
            temp = temp.next 
        
        return self.head #if we reach the tail without deleting a value, just return the head
                       
                 
if __name__ == "__main__":
    ## create list
    llist = LinkedList() #starting with initializing empty linked list
    llist.head = Node(0)
    node1 = Node(1)
    node2 = Node(2) #now we have a several nodes, not connected to each other

    llist.head.next = node1
    node1.next = node2

    #print list
    llist.print_list()
    
    #insert new node at tail
    llist.insert_node_at_tail("tail")
    
    
    #print new list with insertion
    print("---------------")
    llist.print_list()
    
    
    #print new list with delete
    print("---------------")
    llist.delete_node(2)
    llist.print_list()
    
    #print new list with delete head
    print("---------------")
    llist.delete_node(5) #first try to delete something that does not exist
    llist.delete_node(0) #then delete head
    llist.print_list()

     
 