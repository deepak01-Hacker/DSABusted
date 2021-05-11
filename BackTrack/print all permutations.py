#!bin/python3 

def util(string,l,r):
    if l == r:
        print(''.join(string))
    for i in range(l,r+1):
        string[l],string[i] = string[i],string[l]
        util(string,l+1,r)
        string[l],string[i] = string[i],string[l]


def printAllPermutation(string):
    util(string,0,len(string)-1)



if __name__ == "__main__":
    string = "ABC"
    printAllPermutation(list(string))
