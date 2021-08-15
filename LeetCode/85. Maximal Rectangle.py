class Solution(object):
    def maxHistogram(self,histogram):

        stack = []

        max_area = 0 

        index = 0
        while index < len(histogram):


            if (not stack) or (histogram[stack[-1]] <= histogram[index]):
                stack.append(index)
                index += 1

            else:
                top_of_stack = stack.pop()


                area = (histogram[top_of_stack] *
                       ((index - stack[-1] - 1)
                       if stack else index))

                max_area = max(max_area, area)

        while stack:

            top_of_stack = stack.pop()

            area = (histogram[top_of_stack] *
                  ((index - stack[-1] - 1)
                    if stack else index))

            max_area = max(max_area, area)


        return max_area



    def maximalRectangle(self, mat):
        
        if len(mat) == 0:
            return 0

        maxAns = 0

        hist = [0]*len(mat[0])  

        for i in range(0,len(mat)):

            for j in range(0,len(mat[0])):

                if mat[i][j] != "0":
                    hist[j] += int(mat[i][j])
                else:
                    hist[j] = 0

            maxAns = max(maxAns,self.maxHistogram(hist))

        return maxAns

        
