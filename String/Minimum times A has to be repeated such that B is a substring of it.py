def min_repetitions(a, b):
    len_a = len(a)
    len_b = len(b)
     
    for i in range(0, len_a):
         
        if a[i] == b[0]:
            k = i
            count = 1
            for j in range(0, len_b):
                 
                
                if k >= len_a:
                    k = 0
                    count = count + 1
                 
                if a[k] != b[j]:
                    break
                k = k + 1
                 
            else:
                return count
    return -1
 
A = 'abcd'
B = 'cdabcdab'
print(min_repetitions(A, B))
