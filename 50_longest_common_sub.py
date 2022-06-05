from pprint import pprint
from re import L

# longest common subsequence without dp 

def lcsrec(M,N,m,n):
    if(m==0 or n==0):
        return 0
    elif(M[m-1]==N[n-1]):
        return 1+lcsrec(M,N,m-1,n-1)
    else:
        return max(lcsrec(M,N,m-1,n),lcsrec(M,N,m,n-1))
def lcsdp(M,N,m,n,dp):
    if(m==0 or n==0):
        return 0
    if (dp[m][n] != -1):
        return dp[m][n]
    elif(M[m-1]==N[n-1]):
        dp[m][n]=1+lcsdp(M,N,m-1,n-1,dp)
        return dp[m][n]
    else:
        dp[m][n]= max(lcsdp(M,N,m-1,n,dp),lcsdp(M,N,m,n-1,dp))
        return dp[m][n]


# print longest common subsequence

def printlcs(M,N,m,n,dp,a):
    i=m
    j=n
    while(i>0 and j>0):
        if(M[i-1]==N[j-1]):
            a.append(M[i-1])
            i-=1
            j-=1
        elif(dp[i-1][j]>dp[i][j-1]):
            i-=1
        else:
            j-=1
    return a

def lcstd(M,N):
    m = len(M)
    n = len(N)
    dp = [[None]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i==0 or j==0):
                dp[i][j]=0
            elif(M[i-1]==N[j-1]):
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
    return dp

M = 'abcdefga'
N = 'acdaaa'
dp = [[-1 for i in range(len(N) + 1)]for j in range(len(M) + 1)]


print(lcsrec(M,N,len(M),len(N)))

print(lcsdp(M,N,len(M),len(N),dp))
print("++++++++++++++=")
pprint(dp)
print("++++++++++++++=")
a = []
print(printlcs(M,N,len(M),len(N),dp,a))

pprint(lcstd(M,N))