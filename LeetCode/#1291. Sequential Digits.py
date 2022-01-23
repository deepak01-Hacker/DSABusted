class Solution(object):
    def sequentialDigits(self, low, high):
        ans = []
        
        max_ = len(str(high))
        
        for n in range(len(str(low)),max_+1):
        
            num = ['1']

            while(len(num) != n):
                num.append(str(int(num[-1])+1))

            number = int(''.join(num))

            while(number <= high):

                if number >= low and number <= high:
                    ans.append(number)

                num.pop(0)
                num.append(str(int(num[-1])+1))
                
                if num[-1] == '10' or len(num) > n:
                    break

                number = int(''.join(num))
            
        return ans
