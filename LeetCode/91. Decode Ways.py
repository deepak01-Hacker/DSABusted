
class Solution(object):

    def numDecodings(self, arr): 
        if arr == "":
            return 0

        dp = [0]*(len(arr)+1)
        dp[-1] = 1
        dp[-2] = 0 if arr[-1] == "0" else 1

        for i in range(len(arr)-2,-1,-1):
            if arr[i] == "0":
                dp[i] = 0
            else:

                tmp = int(arr[i]+arr[i+1])
                #print(tmp)
                if tmp > 26:
                    dp[i] = dp[i+1]
                else:
                    dp[i] = dp[i+1]+dp[i+2]

        return dp[0]

