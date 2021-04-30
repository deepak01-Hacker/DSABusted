 this Code from GFG
 
 #------------------ o(n2)
 
 MAX = 100
dp = [[0 for i in range(MAX)]
         for i in range(MAX)]
for i in range(0, MAX) :
    for j in range(0, MAX) :
        dp[i][j] = -1

def countRemovals(a, i, j, k) :
 
    global dp
  
    if (i >= j) :
        return 0
 

    elif ((a[j] - a[i]) <= k) :
        return 0

    elif (dp[i][j] != -1) :
        return dp[i][j]
 
    elif ((a[j] - a[i]) > k) :
 
        dp[i][j] = 1 + min(countRemovals(a, i + 1,
                                         j, k),
                           countRemovals(a, i,
                                         j - 1, k))
    return dp[i][j]

def removals(a, n, k) :

    a.sort()

    if (n == 1) :
        return 0
    else :
        return countRemovals(a, 0,
                             n - 1, k)

a = [1, 3, 4, 9, 10,
     11, 12, 17, 20]
n = len(a)
k = 4
print (removals(a, n, k))








#@-------------------------- o(nlogn)

def findInd(key, i, n,
            k, arr):
   
     ind = -1
     

     start = i + 1
   
     end = n - 1;
     
    
     while (start < end):
          mid = int(start +
                   (end - start) / 2)
         
   
          if (arr[mid] - key <= k):
             
               
               ind = mid
                 
               start = mid + 1
          else:
               end = mid
                 
     return ind
     

def removals(arr, n, k):
   
     ans = n - 1
     
     
     arr.sort()
     
     for i in range(0, n):
       
          j = findInd(arr[i], i,
                      n, k, arr)
           
         
          if (j != -1):

               ans = min(ans, n -
                        (j - i + 1))
               
     return ans

a = [1, 3, 4, 9,
     10,11, 12, 17, 20]
n = len(a)
k = 4
print(removals(a, n, k))

#-------------------o(n)


def removals(arr, n, k):
     
  arr.sort()
  dp = [0 for i in range(n)]
 
  
  for i in range(n):
    dp[i] = -1
 

  ans = n - 1
  dp[0] = 0
   
  for i in range(1, n):
    dp[i] = i
    j = dp[i - 1]
     
    while (j != i and arr[i] - arr[j] > k):
      j += 1
       
    dp[i] = min(dp[i], j)
    ans = min(ans, (n - (i - j + 1)))
     
  return ans
 
a = [ 1, 3, 4, 9, 10, 11, 12, 17, 20 ]
n = len(a)
k = 4
 
print(removals(a, n, k))











