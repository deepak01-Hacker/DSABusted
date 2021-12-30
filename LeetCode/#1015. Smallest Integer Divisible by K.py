class Solution(object):
    def smallestRepunitDivByK(self, k):
        if k == 2 or k == 5:
            return -1
        
        prev_rem = 0
        
        for i in range(1,k+1):
            prev_rem = (prev_rem*10+1) % k
            
            if prev_rem == 0:
                return i
        return -1
        
