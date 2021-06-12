class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= 1:
            return s
        
        res = ["" for _ in range(numRows)]

        counter  = numRows
        check = 0

        for i in range(0,len(s)):


            if check % 2 != 0 and numRows-2 >0:
                index = (numRows-2-counter)+2
                res[-index] += s[i]
            else:
                #print(s[i],i)
                index = (numRows - counter)
                #print(index,counter)
                res[index] += s[i]

            counter -= 1

            if counter == 0:
                if check%2 == 0 and numRows-2 >0:
                    counter = numRows-2
                else:
                    counter = numRows
                check += 1



        for i in range(1,numRows):
            res[0] += res[i]
        return res[0]
