class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        """
        length = 0
        prev = {}
        checker = {}

        for i in range(len(nums)):
            checker[nums[i]] = 1

        while(checker):
            eleTemp = 0
            for key in checker:
                eleTemp = key
                break 

            ele = eleTemp - 1

            while(ele in checker):
                checker[eleTemp] += checker[ele]
                del checker[ele]
                ele -= 1

            if ele in prev:
                checker[eleTemp] += prev[ele]

            length = max(length,checker[eleTemp])

            prev[eleTemp] = checker[eleTemp]
            del checker[eleTemp]

        return length


