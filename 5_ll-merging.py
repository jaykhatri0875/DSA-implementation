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
# function to merge linkedlist
def merge(ll1,ll2):
    node = ll1.head
    while(node.next):
        node = node.next
    node.next = ll2.head
    return 

#function to merge sorted linkedlists in sorted manner
# ex.INPUT: 1->2->3 and 2->3->4 
# OUTPUT:  1->2->2->3->3->4

def link(node1,node2):
    n1nxt = node1.next
    n2nxt = node2.next
    node1.next = node2
    node2.next = n1nxt
def merges(ll1,ll2):
    node1 = ll1.head
    node2 = ll2.head
    mll = linkedlist()
    mll.head = ll1.head
    while(node1 or node2):
        if(node1.data < node2.data):
            mll.insertnode_end(node1)
            node1 = node1.next
        elif(node1.data > node2.data):
            mll.insertnode_end(node2)
            node2 = node2.next
        else:
            mll.insertnode_end(node1)
            mll.insertnode_end(node2)
            node1 = node1.next
            node2 = node2.next        
    return mll

def sort_ll(ll):
    pass
if __name__ ==  "__main__":
    a = node(1)
    b = node(2)
    c = node(3)
    d = node(4)
    e = node(5)
    f = node(5)
    h = node(100)
    ll1 = linkedlist()
    ll1.head = a
    a.next = b
    b.next = c   
    ll1.traverse()
    print("-------")
    x=node(2)
    y=node(1)
    p=node(6)
    q=node(9)
    ll2 = linkedlist()
    ll2.head = x
    x.next = y
    y.next = p
    ll2.insertnode_end(q)
    ll2.traverse()
    print("++++++++++++=")
    #merge(ll1,ll2)
    #l1.traverse()

    n = merges(ll1,ll2)
    n.traverse()