#LEETCODE _______________________________________________________________

class Solution(object):
    def isSafe(self,board,row,col):
        return True if (row >= 0 and row <len(board) and col >= 0 and col < len(board[0]) and board[row][col] != "#") else False


    def util(self,row,col,tempSt,word,board):

                
        if tempSt > len(word):
            return False
        
        if not self.isSafe(board,row,col):
            return False
        
        
        if board[row][col] == word[tempSt]:

            temp = board[row][col]
            board[row][col] = "#"

            if tempSt == len(word)-1:
                return True

            elif self.util(row+1,col,tempSt+1,word,board)or  self.util(row-1,col,tempSt+1,word,board) or self.util(row,col-1,tempSt+1,word,board) or self.util(row,col+1,tempSt+1,word,board):
                return True
            
            board[row][col] = temp
            




    def exist(self, board, word):
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.util(i,j,0,word,board):
                    return True
        return False


#_____________________ OFFLINE __________________________







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
