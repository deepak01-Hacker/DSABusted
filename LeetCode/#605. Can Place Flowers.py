class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left = True if i-1 < 0 or flowerbed[i-1] !=1 else False
                right = True if i+1 >= len(flowerbed) or flowerbed[i+1] !=1 else False
                
                if left and right :
                    flowerbed[i] = 1
                    n -= 1
        #print(flowerbed)
        return True if n <= 0 else False
