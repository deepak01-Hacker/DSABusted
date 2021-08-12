def isSafe(visited,row,col):
    return True if (row >= 0 and row<len(visited) and col >= 0 and col < len(visited[0]) and visited[row][col] != True) else False


def util(row,col,visited,tempSt):

    if tempSt == word:
        return True
    if len(tempSt) > len(word):
        return False
      
    if tempSt == word:
        return True

    tempSt += board[row][col]
    visited[row][col] = True

    if (isSafe(visited,row+1,col) and util(row+1,col,visited,tempSt)) or (isSafe(visited,row-1,col) and util(row-1,col,visited,tempSt)) or (isSafe(visited,row,col-1) and util(row,col-1,visited,tempSt)) or (isSafe(visited,row,col+1) and util(row,col+1,visited,tempSt)):
        return True
    tempSt = tempSt[:-1]
    visited[row][col] = False


    

def findWord(board,word):
    
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

    for i in range(len(visited)):
        for j in range(len(visited[0])):
            if util(i,j,visited,""):
                return True
    return False


if __name__ == "__main__":
    board = [["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"],["A","A","A","A","A","A"]]
    word = "AAAAAAAAAAAAAAB"
    print(findWord(board,word))
