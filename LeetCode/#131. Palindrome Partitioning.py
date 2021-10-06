
#131. Palindrome Partitioning

"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

"""



class Solution(object):
    
    def isValid(self,s):
        return s == s[::-1]
    
    def util(self,s,temp,ans):
        if s == "":
            ans.append(tuple(temp))
            return True
        
        for i in range(1,len(s)+1):
            
            if self.isValid(s[:i]):
                
                temp.append(s[:i])
                
                self.util(s[i:],temp,ans)
                
                temp.pop()
    
    def partition(self, s):
        if s == "":
            return []
        ans = []
        
        self.util(s,[],ans)
        return ans
        
