row = [1,0,0,-1]
col = [0,1,-1,0]


class Solution(object):    


    def isValid(self,temp_r,temp_c,setColor,image):
        return (temp_r >= 0 and temp_r < len(image) and temp_c >= 0 and temp_c < len(image[0]) and image[temp_r][temp_c] == setColor)

    def maxAreaOfIsland(self, image):
        """
        :type image: List[List[int]]
        :rtype: int
        """
        res = 0

        for sr in range(len(image)):
            for sc in range(len(image[sr])):

                if image[sr][sc] == 1:

                    length = 1

                    queue = []

                    setColor = 1

                    queue.append((sr,sc))

                    while(queue):

                        r,c = queue.pop(0)
                        image[r][c] = -1
                        #print(r,c ,"visited")

                        for i in range(4):
                            temp_r = r + row[i]
                            temp_c = c + col[i] 

                            if self.isValid(temp_r,temp_c,1,image):

                                queue.append((temp_r,temp_c))
                                image[temp_r][temp_c] = -1
                                #print(length,temp_r,temp_c,image[temp_r][temp_c])

                                length += 1

                    res = max(length,res)
        #print(image)

        return res

