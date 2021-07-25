

def util(number,prem,res,checker):
    if number == "" :
        if res[0] == res[1] and prem not in checker:
            res[2] = prem
            res[0] += 1
            checker.add(prem)
        elif prem not in checker:
            res[0]+=1
            checker.add(prem)

        return
    
    for i in range(len(number)):
        util(number[:i]+number[i+1:],prem+number[i],res,checker)
    return

def nthPermutation(n,k):
    number = ""
    for i in range(1,n+1):
        number += str(i)
    
    res = [1,k,"-1"]
    checker = set()

    util(number,"",res,checker)

    return res[2]
  
  
 # ------------------- Optimize Approach With MAths

class Solution(object):
   
    def getPermutation(self, n, k):
        fact = [1,1,2,6,24,120,720,5040,40320,362880]
        ans = ""
        digits = [i for i in range(1,n+1)]

        while(n):
            index_ = k//(fact[n-1])
            if k%(fact[n-1]) == 0:
                index_ -= 1
            ans += str(digits[index_])
            removeIn = digits.index(digits[index_])
            digits.pop(removeIn)

            k = k - (index_*fact[n-1])
            n -= 1
        return ans


        
        



if __name__ == "__main__":
    n = 3
    k = 3
    print(nthPermutation(n,k))
