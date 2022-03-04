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
# check if tree is valid binary search tree or not
def val(val,right,left):
    return val>left and val<right

def isvalid(root):
    if(root==None):
        return True
    else:
        return val(root.data,root.right.data,root.left.data) and isvalid(root.right) and isvalid(root.left)
    
def minheight(root):
    if root is None:
        return 0
    if(root.left == None):
        return minheight(root.left)+1
    if(root.right ==None):
        return minheight(root.right)+1
    return min(minheight(root.left),minheight(root.right))+1

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    root=insert(arr,None,0)
    print("min height of tree is",minheight(root))