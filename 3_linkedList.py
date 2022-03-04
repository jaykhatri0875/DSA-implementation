#implementation of linkedlist from scratch

# linked list contains data and pointer to next node 
# node with data and pointer 
# all CRUD operations

import time
class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class linkedlist:
    def __init__(self):
        self.head = None

    def insertNode_front(self,node):
         temp = self.head 
         self.head = node
         node.next = temp
    def insertnode_end(self,new_node):
        last =self.head
        while(last.next):
            last = last.next
        last.next = new_node    
        
    def insert_node_mid(self,bw_node,new_node):
        temp = self.head
        while(temp.next != bw_node):
            temp = temp.next
        new_node.next = bw_node
        temp.next = new_node
        return True

    def delete_node(self,d_node):
        temp = self.head
        while(temp.next!=d_node):
            temp = temp.next
        temp.next = d_node.next
        del d_node
        return 'deleted successfully'
    
    def search(self,s_node):
        temp = self.head
        pos = 0
        while(temp.next!=s_node):
            temp = temp.next
            pos+=1
        print("node found at location {} and data of node is {}".format(pos,temp.next.data))
        

    def traverse(self):
        node = self.head
        len = 0
        while(node):
            print(node.data)
            print("|")
            print("v")
            node = node.next
            len+=1
            time.sleep(0.2)

# reversal of linked list
#
#      1  -> 2 -> 3-> 4-> 5->Null
# |     |    |
# prev head, Next
#     current
#steps:
#   while(next is not null ) -> traversing until reach null
#   1. next = curr.next -> storing next values of ll
#   2. curr.next = prev ->  pointing current node to previous node 
#   4. prev = current -> updating previous node so that we can point next time 
#   5. curr = next -> moving forward in linked list
#ll.head = prev-> pointing new head
#
def reverse_list(ll):
    head = ll.head
    prev = None
    curr = head
    next = curr.next
    while(next):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next 
    ll.head = prev
    
if __name__ ==  "__main__":
    a = node(10)
    b = node(20)
    c = node(30)
    d = node(40)
    e = node(50)
    f = node(5)
    h = node(100)
    ll = linkedlist()
    ll.head = a
    ll.head.next = b
    b.next = c
    c.next = d
    ll.insertnode_end(e)
    ll.insertnode_end(f)
    ll.insertnode_end(h)
    print(ll.traverse())
    print("==========")
    ######reversal try 1
    reverse_list(ll)
    print(ll.traverse())

    ## operations on linkedlist
    '''
    print("-----")
    ll.insertNode_front(e)
    print(ll.traverse())
    print("-----")

    ll.insertnode_end(f)
    print(ll.traverse())
    print("-----")

    print(ll.insert_node_mid(d,h))
    print(ll.traverse())

    print("==========")
    x = node(200)
    ll.insertnode_end(x)
    ll.search(x)
    print(ll.traverse())
    print("******")
    print(ll.delete_node(x))
    print(ll.traverse())
    print("******")
    print(ll.delete_node(a))
    print(ll.traverse())
    print("******")
    print(ll.delete_node(b))
    print(ll.traverse())
    print("******")
    print(ll.delete_node(c))
    print(ll.traverse())

    '''
