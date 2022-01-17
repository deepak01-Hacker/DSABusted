class Solution(object):
    def wordPattern(self, pattern, s):
        map = {}
        
        s = list(s.split(" "))
        
        for index in range(min(len(s),len(pattern))):
            char = pattern[index]
            
            if (s[index] in map and map[s[index]] != char) or (char in map.values() and s[index] not in map):
                return False
            map[s[index]] = char
        return True if len(s) == len(pattern) else False
