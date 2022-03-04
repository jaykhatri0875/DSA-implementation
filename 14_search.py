# 1. two pointer method

def binary_search(arr,ele,left,right):
    mid = (left+right)//2
    if(ele>arr[mid]):
        return binary_search(arr,ele,mid+1,right)
    elif(ele<arr[mid]):
        return binary_search(arr,ele,left,mid-1)
    elif(ele==arr[mid]):
        return mid,arr[mid]
    else:
        return mid

if __name__=="__main__":
    arr = [1,2,6,7,8,10,11,12,14,17,19,45,67,222,440,600]
    ele = 222
    print(binary_search(arr,ele,0,len(arr)))