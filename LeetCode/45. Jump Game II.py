class Solution(object):
    def jump(self, nums):
        if nums == [] or len(nums) == 1:
            return 0

        path = 1
        curr = nums[0]

        maxs = curr

        for i in range(1,len(nums)):
            if i > curr:
                if curr == maxs:
                    return 0
                curr = maxs
                path += 1

            if i <= curr:
                maxs = max(i+nums[i],maxs)

        return path
