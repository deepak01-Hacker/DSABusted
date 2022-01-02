class Solution(object):
    def numPairsDivisibleBy60(self, time):
        hashTable = {}
        ans = 0
        
        for i in range(len(time)):
            r = time[i]%60
            
            key = 60-r if r>0 else 0
            print(key)
            if key in hashTable :
                ans += hashTable[key]
            
            if r in hashTable:
                hashTable[r] += 1
            else:
                hashTable[r] = 1
        return ans
        
