class Solution:
	def maxSubstring(self, S):
	    maxs = -1
	    res = 0
	    for i in range(len(S)):
	        t = -1 if S[i] == '1' else 1
	        res += t
	        if res < t:
	            res = t
	        maxs = max(res,maxs)
	    return maxs

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.maxSubstring(s)
		print(answer)

# } Driver Code Ends
