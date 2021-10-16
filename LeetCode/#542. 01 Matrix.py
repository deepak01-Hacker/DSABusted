    
row = [1,0,-1,0]
col = [0,1,0,-1]

class Solution(object):
    def isValid(self,r,c,mat):
        return (r >= 0 and c >= 0 and r < len(mat) and c < len(mat[0]) and mat[r][c] == 1)


    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        dp = [[10**8 for _ in range(len(mat[0]))] for _ in range(len(mat))]

        stack = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    stack.append([i,j,0])

        while(stack):
            i,j,ans = stack.pop(0)

            if dp[i][j] > ans:


                dp[i][j] = ans

                for k in range(len(row)):
                    temp_r = row[k]+ i 
                    temp_c = col[k] + j


                    if self.isValid(temp_r,temp_c,mat):

                        stack.append([temp_r,temp_c,ans+1])

        return dp







