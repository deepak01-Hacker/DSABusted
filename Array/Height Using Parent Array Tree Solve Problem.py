#User function Template for python3

class Solution:
    def findHeight(self, N, arr):
        
        ans = 0
        for i in range(N):
            
            curr = arr[i]
            cnt = 1
            
            while(curr != -1):
                curr = arr[curr]
                cnt += 1
            ans = max(cnt,ans)
        
        return ans
