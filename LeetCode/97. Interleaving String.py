#Memoization Code #Mine--------------------

map = {}
class Solution:
    def util(self,s1,s2,s3,len1,len2,len3,p1,p2,p3):
        
        if (p3 == len3):
            return True if (p1 == len1) and (p2 == len2) else False

        st_key = str(p1)+"*"+str(p2)+"*"+str(p3)

        if st_key in map:
            return map[st_key]
        
        if (p1 == len1):
            map[st_key] = False if (s2[p2] != s3[p3]) else self.util(s1,s2,s3,len1,len2,len3,p1,p2+1,p3+1)
            return map[st_key]

        elif (p2 == len2):
            map[st_key] = False if (s1[p1] != s3[p3]) else self.util(s1,s2,s3,len1,len2,len3,p1+1,p2,p3+1)
            return map[st_key]
        
        one ,two = False,False

        if (s1[p1] == s2[p2]):
            one = self.util(s1,s2,s3,len1,len2,len3,p1+1,p2,p3+1)
        if (s2[p2] == s3[p3]):
            two = self.util(s1,s2,s3,len1,len2,len3,p1,p2+1,p3+1)
        
        map[st_key] = one or two

        return map[st_key]
        
    
        

    def isInterleaving(self,s1,s2,s3):
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if (len1+len2) != len3:
            return False

        return self.util(s1,s2,s3,len1,len2,len3,0,0,0)


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    obj = Solution()

    print(obj.isInterleaving(s1,s2,s3))
    
    
  #----------- GFG ==== fukin Code-----------
  
class Solution(object):

    
    def isInterleave(self, A, B, C):
        M = len(A)
        N = len(B)

        # Let us create a 2D table to store solutions of
        # subproblems. C[i][j] will be true if C[0..i + j-1]
        # is an interleaving of A[0..i-1] and B[0..j-1].
        # Initialize all values as false.
        IL = [[False] * (N + 1) for i in range(M + 1)]

        # C can be an interleaving of A and B only of sum
        # of lengths of A & B is equal to length of C.
        if ((M + N) != len(C)):
            return False

        # Process all characters of A and B
        for i in range(0, M + 1):
            for j in range(0, N + 1):

                # two empty strings have an empty string
                # as interleaving
                if (i == 0 and j == 0):
                    IL[i][j] = True

                # A is empty
                elif (i == 0):
                    if (B[j - 1] == C[j - 1]):
                        IL[i][j] = IL[i][j - 1]

                # B is empty
                elif (j == 0):
                    if (A[i - 1] == C[i - 1]):
                        IL[i][j] = IL[i - 1][j]

                # Current character of C matches with
                # current character of A, but doesn't match
                # with current character of B
                elif (A[i - 1] == C[i + j - 1] and
                      B[j - 1] != C[i + j - 1]):
                    IL[i][j] = IL[i - 1][j]

                # Current character of C matches with
                # current character of B, but doesn't match
                # with current character of A
                elif (A[i - 1] != C[i + j - 1] and
                      B[j - 1] == C[i + j - 1]):
                    IL[i][j] = IL[i][j - 1]

                # Current character of C matches with
                # that of both A and B
                elif (A[i - 1] == C[i + j - 1] and
                      B[j - 1] == C[i + j - 1]):
                    IL[i][j] = (IL[i - 1][j] or IL[i][j - 1])

        return IL[M][N]

  
