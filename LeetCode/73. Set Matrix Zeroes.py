class Solution(object):
    def setZeroes(self, mat):
        setRow = set()
        setCol = set()

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == 0:
                    setRow.add(i)
                    setCol.add(j)

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if i in setRow:
                    mat[i][j] = 0
                elif j in setCol:
                    mat[i][j] = 0
        return mat
        
        
