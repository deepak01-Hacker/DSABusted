"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

                [1]
               [1, 1]
             [1, 3, 3, 1]
            [1, 4, 6, 4, 1]
           [1, 5, 10, 10, 5, 1]
         [1, 6, 15, 20, 15, 6, 1]
       [1, 7, 21, 35, 35, 21, 7, 1]
      [1, 8, 28, 56, 70, 56, 28, 8, 1]


"""



class Solution(object):
    def getRow(self, rowIndex):
    
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1,1]

        pas = [0]*(rowIndex+1)
        pas[0] = 1
        pas[1] = 1

        for i in range(2,rowIndex+1):

            prev = 1
            for j in range(1,i):
                currStore = pas[j]
                pas[j] = pas[j]+prev
                prev = currStore

            pas[i] = 1

        return pas
