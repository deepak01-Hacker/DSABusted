class Solution(object):
    def permuteUnique(self, nums):
        ans = set()
        self.util(nums,ans,[])
        return ans
        
    def util(self,arr,ans,currPermu):
        if arr == []:
            #print(currPermu)
            ans.add(tuple(currPermu[:]))
            return

        for i in range(len(arr)):
            currPermu.append(arr[i])
            self.util(arr[:i]+arr[i+1:],ans,currPermu)
            currPermu.pop()
        return

        
