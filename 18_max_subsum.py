# how to find sliding window problem

# maximum subarray sum of size k

from re import L

# without 2 pointers
def maxsum(array,k):
    sum = 0
    maxsum = 0
    l = len(array)
    for i in range(l):
        if(i+k<=l):
            for j in range(i,i+k):
                sum += array[j]
                if(sum>maxsum):
                    maxsum = sum
            #print(sum)
            sum = 0
    return maxsum 

if  __name__=='__main__':
    array = [111,2,3,4,5,6,7]
    k = 3
    print(maxsum(array,k))