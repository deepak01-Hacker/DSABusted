class Solution(object):
    def groupAnagrams(self, strs):
        result = []

        hashmap = {}

        for string in strs:
            res = []
            for char in string:
                res.append(char)
            res.sort()
            res = tuple(res[:])
            if res in hashmap:
                hashmap[res].append(string)
            else:
                hashmap[res] = []
                hashmap[res].append(string)
        for key in hashmap.keys():
            result.append(hashmap[key])
        return result
        
