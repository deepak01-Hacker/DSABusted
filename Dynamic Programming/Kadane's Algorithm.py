
class Solution:
    def maxSubArraySum(self,a,size):
        resultSum = 0
        sum = 0
        for value in a:
            sum += value
            if sum < value:
                sum = value
            resultSum = max(resultSum,sum)
        return resultSum

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
