class Solution(object):
    
    def reverseString(self, s,left,right,res):
        
        for i in range(right,left-1,-1):
            res[0] += s[i]
            
    
            
    def reverseWords(self, s):
        
        res = [""]
        
        left = 0
        
        for i in range(len(s)):
            if s[i] == " ":
                self.reverseString(s,left,i-1,res)
                left = i+1 #
                res[0] += " "
                
            elif i == len(s)-1:
                self.reverseString(s,left,i,res)

                
        return res[0]
        
            
