class Solution(object):
    def snakesAndLadders(self, board):
        n = len(board)
        lastDestination = n*n
        mat = [-1]*(lastDestination+1)
        leftToRight = True
        k = 1
        for i in range(n-1,-1,-1):
            if leftToRight:
                for j in range(0,n):
                    mat[k] = board[i][j]
                    k += 1
                leftToRight = False
            else:
                for j in range(n-1,-1,-1):
                    mat[k] = board[i][j]
                    k += 1
                leftToRight = True
        queue = []
        visited = [False]*(lastDestination+1)
        visited[1] = True
        queue.append(1)
        result = 0
        while(queue):
            size = len(queue)
            result += 1
            for _ in range(size):
                curr = queue.pop(0)
                for nei in range(curr+1,curr+7):
                    if mat[nei] != -1:
                        nei = mat[nei]
                    if visited[nei]:
                        continue
                    if nei == lastDestination:
                        return result
                    visited[nei] = True
                    queue.append(nei)
        return -1
