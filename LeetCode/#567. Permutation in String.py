class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        result = 0

        left = -1
        right = 0

        checker = {}
        for ele in s1:
            if ele in checker:
                checker[ele] += 1
            else:
                checker[ele] = 1

        #print(checker)

        map = {}

        size = 0

        left = -1

        for right in range(len(s2)):

            if s2[right] not in checker:
                map = {}
                left = -1
                size = 0
            else:
                try:
                    map[s2[right]] += 1
                except:
                    map[s2[right]] = 1

                size += 1

                if left == -1:
                    left = right

                while(map[s2[right]] > checker[s2[right]]):

                    #print(s2[right],left,right)
                    map[s2[left]] -= 1
                    size -= 1
                    left += 1

                if size == len(s1):
                    #print(left , right,map)
                    return True

        return False
