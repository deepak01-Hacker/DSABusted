class Solution(object):
    def isSubsequence(self, s, t):
        i = 0
        
        for j in range(len(t)):
            if i < len(s) and t[j] == s[i]:
                i += 1
        print(i)
        if i == len(s):
            return True
        return False
        
