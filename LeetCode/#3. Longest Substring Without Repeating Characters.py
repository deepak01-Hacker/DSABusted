class Solution:
    def lengthOfLongestSubstring(self, st: str) -> int:
        result = 0

        left = 0
        right = 0

        map = {}

        for right in range(0,len(st)):
            while(st[right] in map and map[st[right]] == 1):
                map[st[left]] -= 1

                left += 1

            map[st[right]] = 1
            #print(left,right) Substring

            result = max(right+1-left,result)
        #print("h")
        return result
            
        
