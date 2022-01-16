class Solution(object):
    def maxDistToClosest(self, seats):
        stack = []

        res = 0
        for i in range(len(seats)):

            if seats[i] == 1:
                stack.append(i)
                res = i
                break
        
        for i in range(i+1,len(seats)):

            if stack != [] and seats[i] == 1:
                distance = i-stack[-1]
                res = max(res,distance//2)
                stack.pop()
            
            if seats[i] == 1:
                stack.append(i)
    
        
        if stack[-1] != len(seats)-1:
            res = max(res,(len(seats)-stack[-1])-1)
        return res
        
        
