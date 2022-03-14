# middle of linked list with only one iteration
from email import header


class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

def middle(ll):
    slow = fast = ll.head
    while(fast and fast.next):  
        fast = fast.next.next
        slow = slow.next
    return slow

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
    print(middle(ll1).data)