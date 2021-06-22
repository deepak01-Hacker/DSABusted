keypad = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]  

class Solution(object):
    
    def util(self,c_digit,res,combo):
        if c_digit == "":
            res.append(combo)
            return
        for i in keypad[int(c_digit[0])]:
            self.util(c_digit[1:],res,combo+i)
        return 
    
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        
        if digits == "":
            return res
        self.util(digits,res,"")
        return res
        
