class Solution(object):
    def notInRow(self,arr, row):

        st = set()

        for i in range(0, 9):

     
            if arr[row][i] in st:
                return False

            if arr[row][i] != '.':
                st.add(arr[row][i])

        return True

 
    def notInCol(self,arr, col):

        st = set()

        for i in range(0, 9):

            if arr[i][col] in st:
                return False

            if arr[i][col] != '.':
                st.add(arr[i][col])

        return True

    def notInBox(self,arr, startRow, startCol):

        st = set()

        for row in range(0, 3):
            for col in range(0, 3):
                curr = arr[row + startRow][col + startCol]

               
                if curr in st:
                    return False

              
                if curr != '.':
                    st.add(curr)

        return True


    def isValid(self,arr, row, col):

        return (self.notInRow(arr, row) and self.notInCol(arr, col) and
                self.notInBox(arr, row - row % 3, col - col % 3))

    def isValidSudoku(self, arr):
        n = 9
        
        for i in range(0, n):
            for j in range(0, n):

                
                if not self.isValid(arr, i, j):
                    return False

        return True

        
