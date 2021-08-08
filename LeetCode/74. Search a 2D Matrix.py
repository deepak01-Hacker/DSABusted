class Solution(object):
    def searchMatrix(self, mat, target):
        
        left = 0
        right = len(mat)-1

        exist = False

        row = 0

        while(right>=left):
            row = (left+right)//2

            
            #print(mat[row])

            if mat[row][0] <= target and mat[row][-1] >= target:
                exist = True
                break

            elif mat[row][-1] > target:
                right = row-1
            else:
                left = row+1


        if not exist and len(mat) > 1:
            return False

        #print(row)

        left, right = 0,len(mat[row])-1

        while(right>=left):

            col = (left+right)//2

            if mat[row][col] == target:
                return True

            elif mat[row][col] > target:
                right = col-1
            else:
                left = col+1
        return False



