class Solution(object):
    def util(self,s,index,ans,temp):
        if index >= len(s):
            ans.append(temp)
            return
        if (s[index] >= "a" and s[index] <= "z") or (s[index] >= "A" and s[index] <= "Z"):
            self.util(s,index+1,ans,temp+s[index].lower())
            self.util(s,index+1,ans,temp+s[index].upper())
        else:
            self.util(s,index+1,ans,temp+s[index])


    def letterCasePermutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.util(s,0,ans,"")
    
        return ans

        
