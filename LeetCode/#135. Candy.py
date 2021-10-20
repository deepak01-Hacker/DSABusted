class Solution(object):
    def candy(self, rating):
        left = [1]*len(rating)
        right = [1]*len(rating)
        candy = 0
        
        
        for i in range(1,len(rating)):
            if rating[i-1] < rating[i]:
                left[i] += left[i-1]
        
        for i in range(len(rating)-2,-1,-1):
            if rating[i+1] < rating[i]:
                right[i] += right[i+1]
            
        for k in range(len(rating)):
            candy += max(left[k],right[k])
        
        return candy

