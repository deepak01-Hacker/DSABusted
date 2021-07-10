class Solution(object):
    def combinationSum2(self,arr, sum):
        ans = []
        temp = []


        arr = sorted(list(arr))

        self.findNumbers(ans, arr, temp, sum, 0)
        return ans

    def findNumbers(self,ans, arr, temp, sum, index):
        if sum < 0:
            return

        if(sum == 0):

            ans.append(list(temp))
            return

        for i in range(index, len(arr)):
            if (index != i and arr[i] == arr[i - 1]):
                continue

            temp.append(arr[i])
            self.findNumbers(ans, arr, temp, sum-arr[i], i+1)

            temp.pop(-1)
