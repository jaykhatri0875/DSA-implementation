# given array of n elements, find minimal length of contiguous subarray of which sum>=s
# In : s= 7, array = [1,4,1,2,4,3]
# out: 2

def minlen(array,sum):
    i,j=0,0
    acc = 0
    ans = float('inf')
    while j<len(array):
        acc += array[j]
        while acc >= sum:
            ans = min(ans,j-i+1)
            acc -= array[i]
            i+=1
        j+=1
    return ans

if __name__=="__main__":
    s= 9
    array = [1,4,1,2,4,3]
    print(minlen(array,s))