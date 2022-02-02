class Solution(object):
    def findAnagrams(self, s, p):
        ans = []
        hash = {}
        hash_sum = 0
        
        for val in p:
            if val in hash:
                hash[val] += 1
            else:
                hash[val] = 1
            hash_sum += 1
        
        i = 0
        j = 0
        temp = {}
        countStr = 0
        
        while(j < len(s) and i <= j):
            if s[j] not in temp:
                temp[s[j]] = 0
            
            if s[j] in hash:
                temp[s[j]] += 1
                countStr += 1
            
                while(temp[s[j]] > hash[s[j]]):
                    temp[s[i]] -= 1
                    i += 1
                    countStr -= 1
                
                if countStr == hash_sum:
                    ans.append(i)
            else:
                countStr = 0
                temp = {}
                i = j+1
            
            j += 1

        return ans

        
