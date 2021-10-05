
#130. Surrounded Regions

"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.
"""

class Solution(object):
    def isValid(self,board,row,col):
        return True if (row < len(board) and row >= 0) and (col < len(board[row]) and col >= 0 ) else False


    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        stack = []

        for i in range(len(board)):
            if board[i][0] == "O" :
                stack.append([i,0])

            if board[i][-1] == "O":
                stack.append([i,len(board[i])-1])

        for j in range(len(board[0])):

            if board[0][j] == "O":
                stack.append([0,j])

            if board[-1][j] == "O":
                stack.append([len(board)-1,j])

        while(stack):
            row,col = stack.pop(0)

            if board[row][col] == "O":

                board[row][col] = "T"

                if self.isValid(board,row+1,col) and board[row+1][col] == "O":
                    stack.append([row+1,col])

                if self.isValid(board,row-1,col) and board[row-1][col] == "O":
                    stack.append([row-1,col])

                if self.isValid(board,row,col+1) and board[row][col+1] == "O":
                    stack.append([row,col+1])

                if self.isValid(board,row,col-1) and board[row][col-1] == "O":
                    stack.append([row,col-1])



        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "T":
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"
