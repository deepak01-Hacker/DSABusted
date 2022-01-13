class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key=lambda x:x[1])
        print(points)
        
        i = 1
        stack = []
        stack.append([points[0][-1],points[0][0],points[0][-1]])
        
        while(i < len(points)):
            start,end = points[i]
            
            if stack != [] and stack[-1][-1] >= start and stack[-1][0] >= start:
                snend,sstart,send = stack.pop()
                
                stack.append([snend,start,end])
            else:
                stack.append([end,start,end])
            
            i += 1
            
                
        return len(stack)
         
        #
            
        
