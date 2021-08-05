class Solution(object):
    def mySqrt(self, x):
        if x >-1 and x < 2:
            return x
        left = 0
        right = x

        while(left<=right):
            mid = (left+right)//2

            if mid*mid > x:
                right = mid-1
            elif mid*mid < x:
                left = mid+1
            else:
                return mid

        return right
      
    def mySqrtN(self, x):
        """
        :type x: int
        :rtype: int
        """

        # Newton's method 

        result = x
        while not result * result - x < 1:
            result = (result + x / result) / 2

        return int(result)
