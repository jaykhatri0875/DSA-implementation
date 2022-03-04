# array to tree -- done
# tree leaf node calculation -- done
# breadth of tree -- 
# tree balancing -- 
# sum problems -- sum done

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

def preorder(node):
    temp = node 
    if(node):
        print(node.data)
        preorder(node.left)
        preorder(node.right)

if __name__=="__main__":
    arr = [1,2,3,4,5,6,7]
    root=insert(arr,None,0)
    preorder(root)