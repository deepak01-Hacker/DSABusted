import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        if n < 0:
            return False
        val = math.log2(n)
        
        return math.ceil(val) == math.floor(val)
        
        
