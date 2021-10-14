row = [1,0,0,-1]
col = [0,1,-1,0]


class Solution(object):
   
    def isValid(self,temp_r,temp_c,setColor,image):
        return (temp_r >= 0 and temp_r < len(image) and temp_c >= 0 and temp_c < len(image[0]) and image[temp_r][temp_c] == setColor)


        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        queue = []

        setColor = image[sr][sc]

        queue.append((sr,sc))

        while(queue):

            r,c = queue.pop(0)
            image[r][c] = -1

            for i in range(4):
                temp_r = r + row[i]
                temp_c = c + col[i] 

                if self.isValid(temp_r,temp_c,setColor,image):
                    queue.append((temp_r,temp_c))
        
        for i in range(len(image)):
            for j in range(len(image[i])):
                if image[i][j] == -1:
                    image[i][j] = newColor


        return image

        
