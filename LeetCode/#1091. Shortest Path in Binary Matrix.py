
row = [0,1,0,-1,1,-1,-1,1]
col = [1,0,-1,0,1,-1,1,-1]


class Solution(object):
    def isSafe(self,r,c,grid):
        return r >= 0 and c >= 0 and r < len(grid) and c < len(grid[0]) and grid[r][c] == 0
    
    def shortestPathBinaryMatrix(self, grid):
        if grid[0][0] != 0:
            return -1
        
        q = [[0,0,1]]
        
        fr = len(grid)-1
        fc = len(grid[0])-1
        
        while(q):
            i,j,k = q.pop(0)
            grid[i][j] = -1
            
            if i == fr and j == fc:
                return k
            
            for index in range(len(row)):
                newi = i+ row[index]
                newj = j+ col[index]
                
                if self.isSafe(newi,newj,grid):
                    grid[newi][newj] = -1
                    q.append([newi,newj,k+1])
        return -1
                
            
