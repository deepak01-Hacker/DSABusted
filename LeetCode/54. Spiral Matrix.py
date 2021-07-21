class Solution(object):
    def spiralOrder(self, mat):
        res = []

        loopTime = len(mat)*len(mat[0])
        
        if loopTime == 1:
        
            return [mat[-1][-1]]
        

        rowUp = 0
        rowDown = len(mat)-1

        colUp = 0
        colDown = len(mat[0])-1

        while(1):
            if rowUp > rowDown or colUp > colDown:
                return res

            for i in range(colUp,colDown+1):
                res.append(mat[rowUp][i])
            rowUp += 1

            for i in range(rowUp,rowDown+1):
                res.append(mat[i][colDown])
            colDown -= 1

            if rowUp > rowDown or colUp > colDown:
                return res

            for i in range(colDown,colUp-1,-1):
                res.append(mat[rowDown][i])
            rowDown -= 1


            for i in range(rowDown,rowUp-1,-1):
                try:
                    res.append(mat[i][colUp])
                except:
                    print(i,colUp-1)
            colUp += 1

        return res

