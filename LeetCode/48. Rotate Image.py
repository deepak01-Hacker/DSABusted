class Solution(object):
    def rotate(self, mat):
        n = len(mat)
        """
        1  2  3  4  5      
        6  7  8  9  10
        11 12 13 14 15
        16 17 18 19 20
        21 22 23 24 25      


        21 16 11 6  1
        22 17 12 7  2
        23 18 13 8  3
        24 19 14 9  4
        25 20 15 10 5
        """

        for i in range(n//2):
            for j in range(i,n-i-1,1):
                #print(mat[i][j])
                temp = mat[i][j]
                mat[i][j] = mat[n-j-1][i]
                mat[n-j-1][i] = mat[n-i-1][n-j-1]
                mat[n-i-1][n-j-1] = mat[j][n-i-1]
                mat[j][n-i-1] = temp
                
        return mat
