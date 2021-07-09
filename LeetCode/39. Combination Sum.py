class Solution(object):
    
    def util(self,arr,i,tar,ans,temp):

        if tar == 0:

            ans.add(temp)

        if i >= len(arr) or tar < 0 :
            return 0

        t = list(temp)
        t.append(arr[i])

        self.util(arr,i,tar-arr[i],ans,tuple(t))
        self.util(arr,i+1,tar,ans,temp)
        return 
    def combinationSum(self, candidates, target):
        ans = set()
        self.util(candidates,0,target,ans,())
        return list(ans)
        
