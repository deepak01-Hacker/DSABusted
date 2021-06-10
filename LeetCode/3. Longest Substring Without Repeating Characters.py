

#leetcode ---- 

# o(n2) ----------------- Approach


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0

        for i in range(0,len(s)):
            
            checker = set()
            templength = 0
            
            for j in range(i,len(s)):
                
                if s[j] in checker:
                    
                    break
                templength += 1
                checker.add(s[j])
                result = max(result,templength)

        return result

# O(n) Approach ----------------------------------- Window sliding Aproach
                
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        result = 0
        
        start = 0
        map = {}

        for end in range(0,len(s)):
            
            if s[end] in map and start<= map[s[end]]:
                start = map[s[end]]+1
                
            map[s[end]] = end
            
            result = max(result,end-start)
        
        return result+1


                


if __name__ == "__main__":
    s = "pwwkew"
    
