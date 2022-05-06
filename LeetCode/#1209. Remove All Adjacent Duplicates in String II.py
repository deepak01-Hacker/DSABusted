class Solution(object):
    def removeDuplicates(self, s, k):
        stack = [["",0]]
        
        for i in range(len(s)):
            if stack[-1][0] != s[i]:
                stack.append([s[i],1])
            else:
                if stack[-1][1]+1 == k:
                    stack.pop()
                else:
                    stack[-1][1] += 1
        ans = ""
        for pair in stack:
            ans += pair[0]*pair[1]
        return ans
        
        
                
            
            
#deeedbbcccbdaa
# ddbbcccbdaa
                
            
        
