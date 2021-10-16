row = [1,0,-1,0]
col = [0,1,0,-1]

class Solution(object):
    def BFS(self,mat,queue,size):

        level = 0
        #print(queue)
        visited = [[False for _ in range(len(mat[0]))] for _ in range(len(mat))]


        while(queue):
            level += 1
            length = len(queue)

            while(length):
                #print(length)
                i,j = queue.pop(0)
                #print(i,j)
                visited[i][j] = True

                for k in range(len(row)):
                    temp_r = i + row[k]
                    temp_c = j + col[k]

                    if self.isValid(temp_r,temp_c,mat) and visited[temp_r][temp_c] == False:
                        visited[temp_r][temp_c] = True
                        size -= 1
                        queue.append((temp_r,temp_c))

                length -= 1

        if size == 0:
            return level 
        return -1

    def isValid(self,r,c,mat):
        return (r >= 0 and c >= 0 and r < len(mat) and c < len(mat[0]) and mat[r][c] == 1)

    def orangesRotting(self, mat):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        levelResult = -1

        q = []
        size = 0

        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if mat[i][j] == 2:
                    q.append((i,j))
                if mat[i][j] == 1:
                    size += 1
        if q or size:
            res = self.BFS(mat,q,size)
            return res-1 if res >= 0 else -1
        return 0

        
