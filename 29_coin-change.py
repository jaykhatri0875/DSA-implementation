'''table = [[0 for x in range(m)] for x in range(target+1)]
		
		for i in range(m):
			table[0][i] = 1
		for i in range(1,target+1):
			for j in range(m):
				if(i-coins[j]>=0):
					x = table[i-coins[j]][j]
				else:
					x = 0
				if(j>=1):
					y = table[j][j-1]
				else:
					y = 0 
				table[i][j] = x+y
		return table[target][m-1]'''

def numberOfCombinations(S, n):
    m = len(S)
    table = [0 for k in range(n+1)]
    table[0] = 1
    for i in range(0,m):
        for j in range(S[i],n+1):
            table[j] += table[j-S[i]]
    return table

print(numberOfCombinations([1,2,4,5],28))