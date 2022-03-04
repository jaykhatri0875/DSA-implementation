class node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def insert(arr,root,i):
    if(i<len(arr)):
        temp = node(arr[i])
        root = temp
        root.left = insert(arr,root.left,2*i+1)
        root.right = insert(arr,root.right,2*i+2)
    return root

def inorder(root):
    if(root!=None):
        inorder(root.left)
        print(root.data,end = " ")
        inorder(root.right)
        
def numofleafs(root):
    if(root.right == None and root.left == None):
        return 1
    else:
        return numofleafs(root.right)+numofleafs(root.left)
    
def sumofleafs(root):
    if(root.right == None and root.left == None):
        return root.data
    else:
        return sumofleafs(root.right)+sumofleafs(root.left)

def numofNonleafs(root):
    if(root.right != None or root.left != None):
        return 1+numofNonleafs(root.right)+numofNonleafs(root.left)
    else:
        return 0

def sumofNonleafs(root):
    if(root.right != None or root.left != None):
        return root.data+sumofNonleafs(root.right)+sumofNonleafs(root.left)
    else:
        return 0

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7]
    root=insert(arr,None,0)
    leafs = numofleafs(root)
    print(leafs)
    sum = sumofleafs(root)
    print(sum)
    nonlef = numofNonleafs(root)
    print(nonlef)
    sumnon = sumofNonleafs(root)
    print(sumnon)