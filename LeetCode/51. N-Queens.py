class Solution(object):
    def solveNQueens(self, n):
        res = []
        
        maze = [["." for _ in range(n)] for _ in range(n)]

        self.utilQueen(res,maze,n,0) 
        

        return res
    
    def checker(self,maze,row,colum,n):

        for i in range(0,colum):
            if maze[row][i] == "Q":
                return False

        r = row-1
        c = colum-1

        while(r >= 0 and  c >= 0):
            if maze[r][c] == "Q":
                return False
            r -= 1
            c -= 1

        r = row+1
        c = colum-1

        while(r < n and  c >= 0):
            if maze[r][c] == "Q":
                return False
            r += 1
            c -= 1


        return True







    def utilQueen(self,res,maze,n,col):
        if col == n:
            temp = []
            
            for i in range(n-1,-1,-1):
                st = ""
                for j in range(n):
                    st += maze[i][j]
                temp.append(st)
            res.append(temp)
            
            return True

        for i in range(0,n):
            maze[i][col] = "Q"

            if self.checker(maze,i,col,n) :
                self.utilQueen(res,maze,n,col+1)

            maze[i][col] = "."

        return False






