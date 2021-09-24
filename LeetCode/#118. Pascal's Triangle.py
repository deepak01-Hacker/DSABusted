class Solution(object):
    def generate(self, numRows):
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        
        passTri = [[1],[1,1]]
        
        for i in range(2,numRows):
            passTri.append([])
            passTri[-1].append(1)
            
            for j in range(1,i):
                passTri[-1].append(passTri[-2][j]+passTri[-2][j-1])
            
            passTri[-1].append(1)
        
        return passTri
