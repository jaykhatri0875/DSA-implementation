# maximum of subarray of size k 

def maxSUb(array,k):
    i,j=0,0
    le = len(array)
    s=ms=0
    while(j<le):
        s = s + array[j]
        if(j-i+1 < k):
            j += 1
        elif(j-i+1 == k):
            if(s > ms):
                ms = s
            s = s - array[i]
            i += 1
            j += 1
    return ms

def maxnum(A,k):
    i,j=0,0
    l = len(A)
    maxw = []
    while(j<l):
        m = max(A[i],A[j])
        if(j-i+1<k):
            j+=1
        elif(j-i+1 == k):
            maxw.append(m)
            i+=1
            j+=1
    return maxw

if __name__=='__main__':
    array = [1,2,100,-1,3,8,9,-6]
    k = 3
    print(maxSUb(array,k))
    print(maxnum(array,k))