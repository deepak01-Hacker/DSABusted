#User function Template for python3
import heapq
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,arr,n,k):
        ans = []
    
        srtArr = []
        heapq.heapify(srtArr)
    
        for i in range(len(arr)):
            heapq.heappush(srtArr,arr[i])
    
            if len(srtArr) > k:
                ele = heapq.heappop(srtArr)
                ans.append(ele)
        
        while(len(srtArr) > 0):
            ele = heapq.heappop(srtArr)
            ans.append(ele)
    
        return ans
    


#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(*ob.nearlySorted(a,n,k))

# } Driver Code Ends
