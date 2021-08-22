class Solution(object):
    def grayCode(self, n):
        res = []

        st = "0"*n
        res.append(st)
        checker = set()
        checker.add(st)

        nth = 2**n
        for i in range(nth):
            st = list(res[-1])
            #print(st)

            for k in range(len(st)-1,-1,-1):
                temp = st[:]
                temp[k] = "0" if st[k] == "1" else "1"
                temp = "".join(temp)
                #print(temp,st)

                if temp not in checker:
                    res.append(temp)
                    checker.add(temp)
                    break

        for j in range(len(res)):
            res[j] = int(res[j],2)
        return res
    
    #____________________________GFG ___________________ SAME APPROACH BUT EFFICIENT CODE ________________________
    
    # Python3 program to generate
# n-bit Gray codes
 
# This function generates all n
# bit Gray codes and prints the
# generated codes
def generateGray(n):
     
    # Base case
    if (n <= 0):
        return ["0"]
    if (n == 1):
        return [ "0", "1" ]
 
    # Recursive case
    recAns = generateGray(n - 1)
 
    mainAns = []
     
    # Append 0 to the first half
    for i in range(len(recAns)):
        s = recAns[i]
        mainAns.append("0" + s)
 
    # Append 1 to the second half
    for i in range(len(recAns) - 1, -1, -1):
        s = recAns[i]
        mainAns.append("1" + s)
 
    return mainAns
 
# Function to generate the
# Gray code of N bits
def generateGrayarr(n):
     
    arr = generateGray(n)
 
    # Print contents of arr
    print(*arr, sep = "\n")
 
# Driver Code
generateGrayarr(3)
 
        
