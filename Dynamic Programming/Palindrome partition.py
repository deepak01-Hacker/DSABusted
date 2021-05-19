#palindrome Partitioning


#------------------------- Recursive ---------------------------------

def isPalindrome(x):
    return x == x[::-1]
 
 
def minPalPartion(string, i, j):
    if i >= j or isPalindrome(string[i:j + 1]):
        return 0
    ans = float('inf')
    for k in range(i, j):
        count = (
            1 + minPalPartion(string, i, k)
            + minPalPartion(string, k + 1, j)
        )
        ans = min(ans, count)
    return ans
 
 

def partition(st):
    return minPalPartion(st,0,len(st)-1)
    

        
                
#----------------------------------- O(n2)
def minCut(a):
 
    cut = [0 for i in range(len(a))]
    palindrome = [[False for i in range(len(a))] for j in range(len(a))]
    for i in range(len(a)):
        minCut = i;
        for j in range(i + 1):
            if (a[i] == a[j] and (i - j < 2 or palindrome[j + 1][i - 1])):      
                palindrome[j][i] = True;
                minCut = min(minCut,0 if  j == 0 else (cut[j - 1] + 1));
        cut[i] = minCut;  
    return cut[len(a) - 1];
 

if __name__=='__main__':
 
    print(minCut("aab"))
    print(minCut("aabababaxx"))

#-------------------------------- simple Dp variation of Matrix Chain Multiplicatioin--------------------

def minPalPartion(str):
     
    
    n = len(str)
     
    C = [[0 for i in range(n)]
            for i in range(n)]
    P = [[False for i in range(n)]
                for i in range(n)]
 
    j = 0
    k = 0
    L = 0
     

    for i in range(n):
        P[i][i] = True;
        C[i][i] = 0;
         
    for L in range(2, n + 1):
         
        for i in range(n - L + 1):
            j = i + L - 1 
            if L == 2:
                P[i][j] = (str[i] == str[j])
            else:
                P[i][j] = ((str[i] == str[j]) and
                             P[i + 1][j - 1])

            if P[i][j] == True:
                C[i][j] = 0
            else:

                C[i][j] = 100000000
                for k in range(i, j):
                    C[i][j] = min (C[i][j], C[i][k] +
                                   C[k + 1][j] + 1)

    return C[0][n - 1]
 
str = "ababbbabbababa"
print ('Min cuts needed for Palindrome Partitioning is',
                                     minPalPartion(str))
