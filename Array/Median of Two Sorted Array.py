def getMedian( ar1, ar2 , n):
    i = 0 
     
    j = 0 
     
    m1 = -1
    m2 = -1
     

    count = 0
    while count < n + 1:
        count += 1
         
      
        if i == n:
            m1 = m2
            m2 = ar2[0]
            break
   
        elif j == n:
            m1 = m2
            m2 = ar1[0]
            break

        if ar1[i] <= ar2[j]:
            m1 = m2
            m2 = ar1[i]
            i += 1
        else:
            m1 = m2
            m2 = ar2[j]
            j += 1
    return (m1 + m2)/2
 
ar1 = [1, 12, 15, 26, 38]
ar2 = [2, 13, 17, 30, 45]
n1 = len(ar1)
n2 = len(ar2)
if n1 == n2:
    print("Median is ", getMedian(ar1, ar2, n1))
else:
    print("Doesn't work for arrays of unequal size")
 
# ------------------------- log(n) ----------------------------------

def getMedian(arr1, arr2, n):
     

    if n == 0:
        return -1
         
    elif n == 1:
        return (arr1[0]+arr2[0])/2
         
    elif n == 2:

        return (max(arr1[0], arr2[0]) +
                min(arr1[1], arr2[1])) / 2
     
    else:
        m1 = median(arr1, n)
        m2 = median(arr2, n)
         
        if m1 > m2:
             
            if n % 2 == 0:
                return getMedian(arr1[:int(n / 2) + 1],
                        arr2[int(n / 2) - 1:], int(n / 2) + 1)
            else:
                return getMedian(arr1[:int(n / 2) + 1],
                        arr2[int(n / 2):], int(n / 2) + 1)
         
        else:
            if n % 2 == 0:
                return getMedian(arr1[int(n / 2 - 1):],
                        arr2[:int(n / 2 + 1)], int(n / 2) + 1)
            else:
                return getMedian(arr1[int(n / 2):],
                        arr2[0:int(n / 2) + 1], int(n / 2) + 1)
 
def median(arr, n):
    if n % 2 == 0:
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else:
        return arr[int(n/2)]
 
     
arr1 = [1, 2, 3, 6]
arr2 = [4, 6, 8, 10]
n = len(arr1)
print(int(getMedian(arr1,arr2,n)))


# --------------- O(nlogn) ---------------------------------

def getMedian(ar1, ar2, n):
    i, j = n - 1, 0
 
    while(ar1[i] > ar2[j] and i > -1 and j < n):
        ar1[i], ar2[j] = ar2[j], ar1[i]
        i -= 1
        j += 1
 
    ar1.sort()
    ar2.sort()
 
    return (ar1[-1] + ar2[0]) >> 1
 
 
if __name__ == '__main__':
    ar1 = [1, 12, 15, 26, 38]
    ar2 = [2, 13, 17, 30, 45]
 
    n1, n2 = len(ar1), len(ar2)
 
    if(n1 == n2):
        print('Median is', getMedian(ar1, ar2, n1))
    else:
        print("Doesn't work for arrays of unequal size")
