class Solution(object):
    def snakesAndLadders(self, board):
        mat = []
        n = len(board)
        for i in range(n):
            if i%2 == 0:
                for j in range(n):
                    mat.append(board[i][j])
            else:
                pos = len(mat)-1
                for j in range(n):
                    mat.insert(pos,board[i][j])
        board = []
        queue = []
        minMoves = n*n
        queue.append([0,0])
        visited = [False for _ in range(n*n)]
        while(queue):
            posAt = queue.pop(0)
            j = posAt[0]+1
            if j == n*n:
                minMoves = min(minMoves,posAt[1])
            while(j<=posAt[0]+n and j < n*n):
                if visited[j] == False:
                    queue.append([j if mat[j] == -1 else mat[j],posAt[1]+1])
                    visited[j] = True
                j+=1
        return minMoves
                
