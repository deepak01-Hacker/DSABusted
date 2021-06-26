class Solution(object):
    
    def create(self,left,right,t,res,ans):
    
        if right > left:
            return
        if left > t or right > t:
            return

        if left == right and left == t:
            ans.append(res)

        self.create(left+1,right,t,res+"(",ans)
        self.create(left,right+1,t,res+")",ans)
        
    def generateParenthesis(self, n):
        ans = []
        self.create(0,0,n,"",ans)
        return ans
        
        
