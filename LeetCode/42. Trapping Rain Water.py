class Solution(object):
    def trap(self, height):
        stack = []
        result = 0

        for i in range(len(height)):

            while len(stack) != 0 and height[stack[-1]] < height[i]:

                popHeight = height[stack[-1]]
                stack.pop()

                if stack == []:
                    break

                distance = i-stack[-1]-1

                minimumHeight = min(height[stack[-1]],height[i])-popHeight

                result += minimumHeight*distance

            stack.append(i)
        return result

        
        
        
        
        
