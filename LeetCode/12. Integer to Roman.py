class Solution:
    def getMaxRoman(self,x,num):
        check = 0
        for i in range(len(num)):
            if num[i] > x:
                return check
            check = i
        return check
    
    def intToRoman(self, x: int) -> str:
        
        #set = {"I": 1 ,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"XC":90,"L":50,"C":100,"CD":400,"D":500,"CM":900,"M":1000}     
        num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        ans = ""

        while(x):
            getMax = self.getMaxRoman(x,num)
            x -= num[getMax]
            ans += roman[getMax]
            
        return ans
