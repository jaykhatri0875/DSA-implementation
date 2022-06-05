from pprint import pprint

def rod_cut(n,prices):
    dp = [[0]*(n+1)]*(n+1)
    
    for i in range(n+1):
        for j in range(n+1):
            if(i<=j):
                dp[i][j]=max(prices[i-1]+dp[i][j-1],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp

n = 8

prices = [1, 3, 4, 5, 7, 9, 10, 11]

print("highest profit is :")
pprint(rod_cut(n,prices))