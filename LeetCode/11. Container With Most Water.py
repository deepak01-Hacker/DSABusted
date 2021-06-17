class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        ans = 0

        while(l<r):
            differnce = r-l
            #print(r,l)
            minHeight = min(height[l],height[r])
            ans = max(ans,minHeight*differnce)

            if height[l] < height[r]:
                l += 1
            else:
                r-=1
        return ans
        
