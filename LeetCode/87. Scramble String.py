map = {}

class Solution(object):
    def util(self,s1,s2):

        if len(s1) != len(s2):
            return False

        if s1 == s2 or len(s1) == 0:
            return True
        if (s1+' '+s2) in map:
            return map[s1+' '+s2]

        for i in range(1,len(s1)):

            if (self.util(s1[:i],s2[:i]) and self.util(s1[i:],s2[i:])) or (self.util(s1[-i:],s2[:i]) and self.util(s1[:-i],s2[i:])):
                map[s1+' '+s2] = True

                return True
        map[s1+' '+s2] = False


        return False



    def isScramble(self, s1, s2):
        if s1 == s2:
            return True

        return self.util(s1,s2)
        
