class Solution(object):
    def floodutil(self,image,sr,sc,prevc,newColor):
        if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != prevc or image[sr][sc] == newColor:
            return 
        image[sr][sc] = newColor
        self.floodutil(image,sr-1,sc,prevc,newColor)
        self.floodutil(image,sr,sc-1,prevc,newColor)
        self.floodutil(image,sr+1,sc,prevc,newColor)
        self.floodutil(image,sr,sc+1,prevc,newColor)

        
    def floodFill(self, image, sr, sc, newColor):
        prevc = image[sr][sc]
        self.floodutil(image,sr,sc,prevc,newColor)
        return image
        
        

if __name__ == "__main__":
    arr = [[1,1,1],
           [1,1,0],
           [1,0,1]]
    x = 1
    y = 1
    col = 2
    s1 = Solution()
    s1.floodFill(arr,x,y,col)
    print(arr)
