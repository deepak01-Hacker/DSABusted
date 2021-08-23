class Solution(object):
    def util(self,arr,st,temp,ans):

        ans.add(tuple(temp[:]))

        for i in range(st,len(arr)):
            temp.append(arr[i])
            self.util(arr,i+1,temp,ans)
            temp.pop()


    def subsetsWithDup(self, arr):
        ans = set()
        arr.sort()
        self.util(arr,0,[],ans)
        return list(ans)
        
