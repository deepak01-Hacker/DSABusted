#let's begin with python3 and end this life .................. with terror ;)
#Pythonist
# 

checker = [[1,1],[0,1],[-1,1],[1,0],[-1,0],[0,-1],[-1,-1],[1,-1]]
                     
class Solution:

    def isValid(self,r,c,grid,visited):
        if r>=0 and c>= 0 and r<len(grid) and c<len(grid[0]) and visited[r][c] == False and grid[r][c] == 1: 
            return True
        return False
    
    def itsconnected(self,grid,land,visited):
        queue = []
        queue.append(land)
        while(queue):
            connect = queue.pop(0)
            visited[connect[0]][connect[1]] = True
            for con in checker:
                r = connect[0] + con[0]
                c = connect[1] + con[1]
                if self.isValid(r,c,grid,visited):
                    queue.append([r,c])
 
    def numIslands(self,grid,):
        R = len(grid)
        C = len(grid[0])
        visited = [[ False for _ in range(C)] for _ in range(R)]
        queue = []
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    queue.append([i,j])
        island = 0
        while(queue):
            land = queue.pop(0)
            if visited[land[0]][land[1]] == False:
                island += 1
                self.itsconnected(grid,land,visited)
        return island


if __name__ == "__main__":
    grid = [[0,1,1,1,0,0,0],[0,0,1,1,0,1,0]]
    s1 = Solution()
    print(s1.numIslands(grid))
