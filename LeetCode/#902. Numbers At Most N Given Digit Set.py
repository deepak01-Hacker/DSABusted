class Solution(object):
    def atMostNGivenDigitSet(self, digits, n):
        n_str = str(n)
        count = 0
        
        for i in range(1,len(n_str)):
            count += len(digits)**i
            
        i = 0
        while(i<len(n_str)):
            j = 0
            
            while(j < len(digits) and digits[j][0] < n_str[i]):
                count += len(digits)**(len(n_str)-1-i)
                j += 1
            
            if j == len(digits) or digits[j][0] > n_str[i]:
                break
            i += 1
            
        if i == len(n_str):
            count += 1
        return count
