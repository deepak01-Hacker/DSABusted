class Solution(object):
    

    def say(self,res):
        ans = ""
        prev = [1,res[0]]

        for i in range(1,len(res)):
            if prev[-1] != res[i]:
                ans += str(prev[0])
                ans += prev[1]
                prev[0] = 0
            prev[0] += 1
            prev[1] = res[i]
        ans += str(prev[0])
        ans += prev[-1]
        return ans 

    def util(self,n,res):
        if n == 0:
            return res
        res = self.say(res)
        return self.util(n-1,res)


    def countAndSay(self, n):
        if n == 1:
            return "1"
        res = "1"
        return self.util(n-1,res)
        
