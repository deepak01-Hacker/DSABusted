class Solution(object):
 
    def util(self,n,k,combo,ans):
        if k == 0:
            ans.append(combo[::-1])
            return
        for i in range(n,0,-1):
            combo.append(i)
            self.util(i-1,k-1,combo,ans)
            combo.pop()


    def combine(self, n, k):
        ans = []
        self.util(n,k,[],ans)
        return ans
