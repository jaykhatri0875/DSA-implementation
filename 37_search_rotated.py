#search in rotated sorted array
# binary search is applicate to literally every sorted array out there in market
# find index of minimum element of array - whichc would give two sorted array
# ex. 10, 11, 12 ,13,3,4,5,8 --> min element is 3, so we get two sorted arrays, now element has to be searched in both arrays with binary search


def binarySearch(array,target):
    left,right = 0,len(array)-1
    mid = -1
    while(left<=right):
        mid = (left+right)//2
        if(target<array[mid]):
            right = mid-1
        elif(target>array[mid]):
            left = mid+1
        elif(target==array[mid]):
            return mid
    return -1

# find index of mininmum element in rotated sorted array
# property of mid, its smaller than both of its neighbours
# 

def rotatedBinarySearch(array,target):
    # find index of minimum element
    N = len(array)
    left , right = 0,len(array)-1
    while(left<=right):
        mid = left+((right-left)//2)
        next = (mid+1)%N
        prev = (mid+N-1)%N
        if(array[mid]<=array[prev] and array[mid]<=array[next]):
            return mid
        elif(array[mid]<=array[right]):
            right = mid - 1
        elif(array[mid]>=array[left]):
            left = mid + 1
    return -1




array = [1,2,3,4,5,6,7,8,11]
target = 10 
rarray = [11,25,26,27,50,1,2,5,6]
index = binarySearch(array,target)
rindex = rotatedBinarySearch(rarray,target)
print(rindex)


