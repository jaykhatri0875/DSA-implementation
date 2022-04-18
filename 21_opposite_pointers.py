# opposite directional two pointers
# we can reverse an array or string withour extra space
# 
def reverse(array):
    i,j=0,len(array)-1
    while(i<j):
        array[i],array[j] = array[j],array[i]
        i+=1
        j-=1
    return array
# given sorted array and targetsum k,find two numbers such that they add up to k
def twoSum(array,k):
    i,j=0,len(array)-1
    while(i<j):
        sum = array[i] + array[j]
        if(k==sum):
            return [array[i],array[j]]
        elif(k>sum):
            i +=1
        else:   
            j-=1
    return []
if __name__=="__main__":
    array = [1,2,3,4,5,6,7,8]
    k = 5
    string = 'jayk'
    print(twoSum(array,k))  