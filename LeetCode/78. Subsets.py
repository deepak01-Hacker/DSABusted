class Solution(object):
    def util(self,arr,st,temp,ans):
        temps = tuple(temp)
        ans.append(temps)

        if arr == []:
            return 

        for i in range(st,len(arr)):
            temp.append(arr[i])
            self.util(arr,i+1,temp,ans)
            temp.pop()


    def subsets(self, arr):

        ans = []
        self.util(arr,0,[],ans)
        return ans
