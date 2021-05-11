#!bin/python3 

# ------------------ Recursion ----------------------------------------------

def util(n,x,y,st):
    if n < 0:
        return False
    newSt = "A" if st == "B" else "B"
    if newSt == "A" and n == 0:
        return True
    return util(n-1,x,y,newSt) or util(n-x,x,y,newSt) or util(n-y,x,y,newSt)


def isAwinOrnot(n,x,y):
    return True if util(n,x,y,"A") else False


#----------------------DP---------------------------------------------------
#Memoization

#!bin/python3 

dp = [-1 for _ in range(100)]

def util(n,x,y,st):
    if n < 0:
        return 0
    if dp[n] != -1:
        return dp[n]
    newSt = "A" if st == "B" else "B"
    if newSt == "A" and n == 0:
        return 1
    dp[n] = util(n-1,x,y,newSt) or util(n-x,x,y,newSt) or util(n-y,x,y,newSt)
    return dp[n]

def isAwinOrnot(n,x,y):
    return True if util(n,x,y,"A") else False
#---------------------------- use Functions by your need they all algo function have same name 000---------------------------

if __name__ == "__main__":
    n = 2
    x = 3
    y = 4
    print(isAwinOrnot(n,x,y))
