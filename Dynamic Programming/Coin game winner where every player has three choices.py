#!bin/python3 

def util(n,x,y,st):
    if n < 0:
        return False
    newSt = "A" if st == "B" else "B"
    if newSt == "A" and n == 0:
        return True
    return util(n-1,x,y,newSt) or util(n-x,x,y,newSt) or util(n-y,x,y,newSt)


def isAwinOrnot(n,x,y):
    return True if util(n,x,y,"A") else False


if __name__ == "__main__":
    n = 2
    x = 3
    y = 4
    print(isAwinOrnot(n,x,y))
