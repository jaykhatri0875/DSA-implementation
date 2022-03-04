
class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
class btree:
    def __init__(self,node):
        self.root = node
    
    def insert_node(self,node):
        if(self.root == None):
            self.root = node
        elif(self.root.data< node.data):
            self.root.left = node
        elif(self.root.data > node.data):
            self.root.right = node

def inorder(node):
    temp = node 
    if(node):
        inorder(node.left)
        print(node.data)
        inorder(node.right)

def preorder(node):
    temp = node 
    if(node):
        print(node.data)
        preorder(node.left)
        preorder(node.right)

def postorder(node):
    temp = node 
    if(node):
        postorder(node.left)
        postorder(node.right)
        print(node.data)
# wrong logic
'''
def height(node):
    h = 0
    if(node.left or node.right):
        h = max(height(node.left),height(node.right))+1
        return h
'''
def height(node):
    if node is None:
        return -1
    else:
        lh = height(node.left)
        rh = height(node.right)

        if(lh>rh):
            return lh+1
        else:
            return rh+1

            
#       a-10
#       /\
#     20  30
#    / \  / \  
#   50 40100 5
if __name__ ==  "__main__":
    a = node(10)
    b = node(20)
    c = node(30)
    d = node(40)
    e = node(50)
    f = node(5)
    h = node(100)
    bt = btree(a)
    a.left = b
    a.right = c
    b.right = d
    b.left = e
    c.right = f
    #f.right = node(3)
    c.left = h
    inorder(a)
    print("------")
    preorder(a)
    print("------")
    postorder(a)
    print("------")
    print(height(a))