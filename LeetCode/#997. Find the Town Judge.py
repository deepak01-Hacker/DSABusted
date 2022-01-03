class Solution(object):
    def findJudge(self, n, trust):
        if n == 1:
            return 1
        
        hashTable = [0]*(n+1)
        
        for ai,bi in trust:
            
            if hashTable[bi] <= 0:
                val = hashTable[bi]*-1
                hashTable[bi] = -1*(val+1)
            else:
                hashTable[bi] += 1
            
            
            if hashTable[ai] < 0:
                hashTable[ai] += (hashTable[ai]*-1)
            hashTable[ai] += 1
        print(hashTable)
        
        for i in range(1,n+1):
            if hashTable[i]<0 and -1*(hashTable[i]) == n-1:
                return i
        return -1 #1->2->3
        #1->3 , 2->3=1
