# two sum : pait with target sum
# two sum when array is not sorted


def twosum(array,sum):
    i,j=0,0
    l = len(array)
    s = 0
    while(j<l-1):
        s = s + array[j]
        if(s==sum):
            return 