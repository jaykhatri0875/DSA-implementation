#floyds cycle detection algo in linkedlist  
from os import link


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

def detectCycle(linkedlist):
    slow = fast = linkedlist.head
    while(fast and fast.next):
        fast = fast.next.next
        slow = slow.next
        if(slow == fast):
            removeCycle(linkedlist,slow,fast)
            return 
    return None
#removal of cycle from linkedlist
def removeCycle(linkedlist,slow,fast):
    slow = linkedlist.head
    while(fast and slow.next != fast.next):
        slow = slow.next
        fast = fast.next.next
    fast.next = None
    return fast.data
    
if __name__=="__main__":
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
    c.next = d
    d.next = e
    e.next = h
    h.next = d  
    print(detectCycle(ll1))