# in array of 0s and 1s, how many non empty subarrays have sum S?
# three sum




def threesum(array,S):
    i,j = 0,0
    win_sum = 0
    ans = 0
    l = len(array)
    while(j<l):
        win_sum += array[j]
        while(i<j and win_sum > S):
            win_sum -= array[i]
            i+=1
        if(win_sum == S):
            ans+=1
            print(i,j)
        j+=1
    return ans

def threeSum(array,S):
    i,i_h,j=0,0,0
    win_sum = 0
    ans = 0
    while(j<len(array)):
        win_sum += array[j]
        while(i<j and win_sum > S):
            win_sum -= array[i]
            i+=1
        i_h = 1
        while(i_h <j and win_sum == S and array[i_h]==0):
            ans += 1
            i_h += 1
            print(i,j)
        if(win_sum == S):
            ans+=1
            print(i,j)  
        j+=1
    return ans
        
array = [1, 0,1,0,1]
S = 2
print(threeSum(array,S))