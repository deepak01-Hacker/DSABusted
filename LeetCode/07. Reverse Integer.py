class Solution:
    def reverse(self, x: int) -> int:
                
        ans = 0

        posVal = True
        
        if x<0:
            posVal = False
            x = x*-1

        while(x):

            #print(ans)
            ans = ans*10

            ans += x%10

            x = x//10


        if not posVal:
            ans *= -1
        if ans <= (-2**31) or ans >= (2**31)-1:
            return 0
        return ans
        
