# how to find sliding window problem

# maximum subarray sum of size k

from re import L

# without 2 pointers --> O(n^2) complexity 
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

# complexity -- O(n)
def maxSumSW(array,k):
    sum = 0
    maxsum = 0
    l = len(array)
    i,j=0,0
    while(j<l):
        sum = sum + array[j]
        if(j-i+1<k):
            #keep moving j untill given window size is not achieved
            j+=1
        elif(j-i+1 == k):
            #print(sum)
            # moving i and j and maintaining widow size here
            maxsum = max(maxsum,sum)
            sum = sum - array[i]
            j+=1
            i+=1
    return maxsum

if  __name__=='__main__':
    array = [1,2,33,4,5,6,7]
    k = 3
    print(maxSumSW(array,k))