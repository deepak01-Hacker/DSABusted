class Solution(object):
    def plusOne(self, digits):
        carry = 1
        
        for i in range(len(digits)-1,-1,-1):
            val = carry+digits[i]
            digits[i] = val%10
            carry = val//10
            
            if carry == 0:
                break
            
        if carry:
            digits.insert(0,carry)
        return digits
        
         
