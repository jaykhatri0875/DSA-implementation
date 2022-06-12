def longestPalindromicss(M):
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
    N = M[::-1]
    ans = lcstd(M,N)
    return ans

M =  'ABCABCDS'
print(longestPalindromicss(M))

