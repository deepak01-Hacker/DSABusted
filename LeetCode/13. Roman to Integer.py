class Solution:
    def romanToInt(self, x: str) -> int:
        num = {"I": 1 ,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"XC":90,"L":50,"C":100,"CD":400,"D":500,"CM":900,"M":1000}     

        #num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        #roman = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        ans = 0


        index = 0
        while(index < len(x)):
            if index+1 < len(x) and x[index:index+2] in num:
                ans += num[x[index:index+2]]
                index += 2

            else:
                ans += num[x[index:index+1]]
                index += 1
        return ans
        
        
