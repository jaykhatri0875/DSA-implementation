# 0/1 - knapsack , recursive and DP version

# weights = []
#
#

def knapsack(wt,val,cap,n):
    if(n ==0 or cap == 0):
        return 0    
    if(val[n-1]<=cap):
        return max(val[n-1]+knapsack(wt,val,cap-val[n-1],n-1),
                knapsack(wt,val,cap,n-1))
    elif(wt[n-1]>cap):
        return knapsack(wt,val,cap,n-1)

wt = [1,2,3,4]
val = [1,2,3,1]
cap = 10
n = len(wt)-1

print(knapsack(wt,val,cap,n))