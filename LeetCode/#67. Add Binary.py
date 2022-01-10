class Solution(object):
    def addBinary(self, a, b):
        
        ans = ""
        
        i = len(a)-1
        j = len(b)-1
        
        carry = 0
        while(i >= 0 and j >= 0):
            sum = int(a[i])+int(b[j])+carry
            
            carry = sum//2
            
            ans += str(sum%2)
            
            i-= 1
            j -=1 # 1 1 0
        while(i >= 0):
            sum = int(a[i])+carry
            
            carry = sum//2
            
            ans += str(sum%2)
            i -= 1
            
        while(j >= 0):
            sum = int(b[j])+carry
            
            carry = sum//2
            
            ans += str(sum%2)
            j -= 1
        if carry:
            ans += str(carry)
        return ans[::-1]
            
