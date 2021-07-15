class Solution(object):
        
    def util(self,arr,ans,currPermu):
        if arr == []:
            #print(currPermu)
            ans.append(currPermu[:])
            return

        for i in range(len(arr)):
            currPermu.append(arr[i])
            self.util(arr[:i]+arr[i+1:],ans,currPermu)
            currPermu.pop()
        return



    def permute(self,nums):
        ans = []
        self.util(nums,ans,[])
        return ans
