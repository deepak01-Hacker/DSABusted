mod = 1e9+7
class Solution(object):
    
    def gcd(self,i,j):
        if j == 0:
            return i
        return self.gcd(j,i%j)
    
    def lcm(self,i,j):
        return (i*j)//self.gcd(i,j)
    
    def nthMagicalNumber(self, n, a, b):
        
        low = 1
        high = 1e17
        lcmab = self.lcm(a,b)
        print(self.gcd(a,b))
        
        while(low<high):
            
            mid = (low+high)//2
            target = (mid//a)+(mid//b)-(mid//lcmab)
            
            if target < n:
                low = mid+1
            else:
                high = mid
        return int(high%mod)
        
