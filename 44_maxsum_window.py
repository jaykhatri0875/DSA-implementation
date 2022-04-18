
def maxsum(array,k):
    i=0
    j=0
    l = len(array)
    s = []
    temp = 0
    while(j<l):
        temp+=array[j]
        print(temp)
        if(temp>k):
            while(temp>k and i<=j):
                temp -= array[i]
                i+=1
        elif(temp==k):
            s.append([array[j],array[i],j,i])
            j+=1
        j+=1
    return s    

def long_subarray(arr, k):
    n = len(arr)
    sum = 0
    win_size = 0
    i = 0
    j = 0
    while j < n:
        sum = sum + arr[j]
        if sum == k:
            win_size = max(win_size, j-i+1)
        elif sum > k:
            while sum > k and i <= j:
                sum -= arr[i]
                i += 1
                if sum == k:
                    win_size = max(win_size, j-i+1)
        j += 1

    return win_size
arr =[10, 5, 2, 7, 1, 9]
sum = 15
print(long_subarray(arr, sum))
print(maxsum([4,1,1,1,2,3,5],5))

