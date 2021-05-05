
#Practice  : https://practice.geeksforgeeks.org/problems/word-break1352/1


#REcursion -----------------------

def wordbreak(i,j):
    if i <= -1 or j <= -1:
        return False
    
    if i < j:
        if A[i:j] in dictionary and i == 0:
            return True
        elif A[i:j] in dictionary:
            return wordbreak(i-1,i)
        else:
            return wordbreak(i-1,j)
    return False



#---------------------DP ====================

def wordBreak(line, dictionary):
    dp = [False for _ in range(len(line)+1)]
    
    for i in range(len(line)):
        for j in range(i+1,len(line)+1):
            if line[i:j] in dictionary :
                if i == 0:
                    dp[j] = True
                else:
                    dp[j] = dp[i]
    return dp[-1]

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		res = wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends
