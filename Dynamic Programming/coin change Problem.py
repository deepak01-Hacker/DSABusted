#User function Template for python3

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
