def count(S, m, n):

    table = [[0 for x in range(m)] for x in range(n+1)]
 
    for i in range(m):
        table[0][i] = 1
 
    for i in range(1, n+1):
        for j in range(m):
 
            x = table[i - S[j]][j] if i-S[j] >= 0 else 0
 
            y = table[i][j-1] if j >= 1 else 0
 
            table[i][j] = x + y
 
    return table[n][m-1]
 
arr = [1, 2, 3]
m = len(arr)
n = 4
print(count(arr, m, n))

#========================================================================

# Dynamic Programming Python implementation of Coin

def count(S, m, n):
	table = [0 for k in range(n+1)]

	table[0] = 1

	for i in range(0,m):
		for j in range(S[i],n+1):
			table[j] += table[j-S[i]]

	return table[n]


arr = [1, 2, 3]
m = len(arr)
n = 4
x = count(arr, m, n)
print (x)


#------------------------------------------------------------------
class Solution:
    def __init__(self):
        self.dp = {}
        
    def dputils(self,chains,money,i):# Here i is the pointer that point to chains element or rupee
        if money == 0:
            return 1
        elif money < 0 or i >= len(chains):
            return 0
        try:
            return self.dp[(money,i)]
        except:
            self.dp[(money,i)] = self.dputils(chains,money,i+1) + self.dputils(chains,money-chains[i],i)
            return self.dp[(money,i)]
            
    def count(self, chains, money, n): 
        return self.dputils(chains,n,0)


#{ 
#  Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n,m = list(map(int, input().strip().split()))
        S = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.count(S,m,n))
# } Driver Code Ends
