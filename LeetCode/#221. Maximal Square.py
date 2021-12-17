class Solution(object):
    def maximalSquare(self, mat):
        matrix = [[0 for _ in range(len(mat[i]))] for i in range(len(mat))] #its only for integer you can use mat 
        res = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if mat[i][j] == "0":
                    matrix[i][j] = 0
                else:
                    matrix[i][j] = 1

                    res = 1

        for i in range(1,len(matrix)):
            for j in range(1,len(matrix[i])):

                if matrix[i][j] > 0 and matrix[i-1][j] > 0 and matrix[i][j-1] and matrix[i-1][j-1] > 0:
                    matrix[i][j] = min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1

                res = max(res,matrix[i][j])
        if res == 1:
            return 1
        return res*res
