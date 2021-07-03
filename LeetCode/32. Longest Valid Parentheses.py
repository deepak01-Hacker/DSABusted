class Solution(object):
    def longestValidParentheses(self, S):
        result = 0
        
        stack = []
        
        stack.append(-1)
        
        for i in range(len(S)):
            
            if S[i] == '(':
                stack.append(i)
            
            else:
                
                if len(stack)!= 0:
                    stack.pop()

                if len(stack) != 0:
                    result = max(result,i-stack[-1])
                else:
                    stack.append(i)
        return result
