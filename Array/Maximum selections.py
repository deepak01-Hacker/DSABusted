

class Solution:
        
    def max_non_overlapping(self,ranges):
        ranges.sort(key=lambda x:x[1])
        
        bound = [-1,-1]
        ans = 0
        
        for i in range(len(ranges)):
            x = ranges[i][0]
            y = ranges[i][1]
            
            if bound[-1] < x:
                bound[-1] = y
                bound[0] = x
                ans += 1
        return ans
