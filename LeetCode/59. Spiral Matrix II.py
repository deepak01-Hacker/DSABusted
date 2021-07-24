class Solution(object):
    def generateMatrix(self, n):
        mat = [[0 for _ in range(n)] for _ in range(n)]
        
        target = 1

        loopTime = n*n
        
        if loopTime == 1:
        
            return [[1]]
        

        rowUp = 0
        rowDown = n-1

        colUp = 0
        colDown = n-1

        while(1):
            if rowUp > rowDown or colUp > colDown:
                return mat

            for i in range(colUp,colDown+1):
                mat[rowUp][i] = target
                target += 1
            rowUp += 1

            for i in range(rowUp,rowDown+1):
                mat[i][colDown] = target
                target += 1
            colDown -= 1

            if rowUp > rowDown or colUp > colDown:
                return mat

            for i in range(colDown,colUp-1,-1):
                mat[rowDown][i] = target
                target += 1
            rowDown -= 1


            for i in range(rowDown,rowUp-1,-1):
                try:
                    mat[i][colUp] = target
                    target += 1
                except:
                    print(i,colUp-1)
            colUp += 1

        return mat
        
