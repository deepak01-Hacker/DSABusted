def parenthesis_count(Str, i, j, isTrue, dp) :
     
    if (i > j) :
      return 0
     
    if (i == j) :
     
      if (isTrue == 1) :
       
        return 1 if Str[i] == 'T' else 0
       
      else :
       
        return 1 if Str[i] == 'F' else 0
     
    if (dp[i][j][isTrue] != -1) :
      return dp[i][j][isTrue]
     
    temp_ans = 0
     
    for k in range(i + 1, j, 2) :
     
      if (dp[i][k - 1][1] != -1) :
        leftTrue = dp[i][k - 1][1]
      else :
        # Count number of True in left Partition
        leftTrue = parenthesis_count(Str, i, k - 1, 1, dp)
         
      if (dp[i][k - 1][0] != -1) :
        leftFalse = dp[i][k - 1][0]
      else :
        # Count number of False in left Partition
        leftFalse = parenthesis_count(Str, i, k - 1, 0, dp)
      
      if (dp[k + 1][j][1] != -1) :
        rightTrue = dp[k + 1][j][1]
      else :
        # Count number of True in right Partition
        rightTrue = parenthesis_count(Str, k + 1, j, 1, dp)
       
      if (dp[k + 1][j][0] != -1) :
        rightFalse = dp[k + 1][j][0]
      else :
        # Count number of False in right Partition
        rightFalse = parenthesis_count(Str, k + 1, j, 0, dp)
     
      # Evaluate AND operation
      if (Str[k] == '&') :
        if (isTrue == 1) :
          temp_ans = temp_ans + leftTrue * rightTrue
        else :
          temp_ans = temp_ans + leftTrue * rightFalse + leftFalse * rightTrue + leftFalse * rightFalse
      # Evaluate OR operation
      elif (Str[k] == '|') :
        if (isTrue == 1) :
          temp_ans = temp_ans + leftTrue * rightTrue + leftTrue * rightFalse + leftFalse * rightTrue
        else :
          temp_ans = temp_ans + leftFalse * rightFalse
     
      # Evaluate XOR operation
      elif (Str[k] == '^') :
        if (isTrue == 1) :
          temp_ans = temp_ans + leftTrue * rightFalse + leftFalse * rightTrue
        else :
          temp_ans = temp_ans + leftTrue * rightTrue + leftFalse * rightFalse
      dp[i][j][isTrue] = temp_ans
 
    return temp_ans
     
def countWays(N, S) :
  
    dp = [[[-1 for k in range(2)] for i in range(N + 1)] for j in range(N + 1)]
    return parenthesis_count(S, 0, N - 1, 1, dp)
  
symbols = "TTFT"
operators = "|&^"
S = ""
j = 0
for i in range(len(symbols)) :
 
  S = S + symbols[i]
  if (j < len(operators)) :
    S = S + operators[j]
    j += 1
 
# We obtain the string  T|T&F^T
N = len(S)
 
# There are 4 ways
# ((T|T)&(F^T)), (T|(T&(F^T))), (((T|T)&F)^T) and
# (T|((T&F)^T))
print(countWays(N, S))
