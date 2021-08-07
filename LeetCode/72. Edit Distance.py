class Solution(object):
    def minDistance(self, word1, word2):
        dp = [[0 for _ in range(len(word1)+1)] for _  in range(len(word2)+1)]

        for i in range(1,len(word2)+1):
            dp[i][0] = i

        for j in range(1,len(word1)+1):
            dp[0][j] = j

        for i in range(1,len(word2)+1):
            for j in range(1,len(word1)+1):
                if word2[i-1] != word1[j-1]:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1

                else:
                    dp[i][j] = dp[i-1][j-1]



        #print(dp)
        return dp[-1][-1]

#Edit Distance With Recursion

def util(word1,word2,ans):
    if word1 == "" :
        return len(word2)

    if word2 == "":
        return len(word1)

    if word1[-1] == word2[-1]:
        return util(word1[:-1],word2[:-1],ans)
    else:
        return min(util(word1[:-1],word2,ans),util(word1,word2[:-1],ans),util(word1[:-1],word2[:-1],ans))+1




def editDistance(word1,word2):
    ans = [0]
    return util(word1,word2,ans) // ans if for debugging So don't care about this . ;)


if __name__ == "__main__":
    word1 = "intention"
    word2 = "execution"   
    print(editDistance(word1,word2))
