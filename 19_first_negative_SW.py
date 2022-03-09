# first negative in given array from subarray of size k
# in -> array = [1,-2,-3,-4,-5,6,7,9] , k = 3
# out -> [-2,-2,-3,-4,-5,0]
#
def firstNegative(array,k):
    i,j=0,0
    negarr = []
    l = len(array)
    while(j<l):
        if(j-i+1 < k):
            pass
        elif(j-i+1 == k):
            pass
    return negarr