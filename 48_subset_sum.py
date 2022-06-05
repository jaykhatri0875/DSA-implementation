# non DP version of subset
 
def subset(arr,sum,n):
    if(sum == 0):
        return True
    if(sum>0 and n==0):
        return False
    if(arr[n-1]>sum):
        return subset(arr,sum,n-1)

    return subset(arr,sum,n-1) or subset(arr,sum-arr[n-1],n-1)
# DP version - memoization added 
def subset(arr,sum,n):
    if(sum == 0):
        return True
    if(sum>0 and n==0):
        return False
    if(arr[n-1]>sum):
        return subset(arr,sum,n-1)

    return subset(arr,sum,n-1) or subset(arr,sum-arr[n-1],n-1)

arr = [2,3,7,8,10]
sum = 6
n = len(arr)
dp = [[]]
#print(arr[n-1])
print(subset(arr,sum,n))