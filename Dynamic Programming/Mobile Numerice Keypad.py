#------------------------------ REcursion ----------------------------------------------------------------------------------

row = [0, 0, -1, 0, 1]
col = [0, -1, 0, 1, 0]
 

def getCountUtil(keypad, i, j, n):
    if (keypad == None or n <= 0):
        return 0
 
   
    if (n == 1):
        return 1
    k = 0
    move = 0
    ro = 0
    co = 0
    totalCount = 0
    
    for move in range(5):
        ro = i + row[move]
        co = j + col[move]
        if (ro >= 0 and ro <= 3 and co >= 0 and co <= 2 and
                keypad[ro][co] != '*' and keypad[ro][co] != '#'):
            totalCount += getCountUtil(keypad, ro, co, n - 1)
    return totalCount

def getCount(keypad, n):
     
    if (keypad == None or n <= 0):
        return 0
    if (n == 1):
        return 10
    i = 0
    j = 0
    totalCount = 0
    for i in range(4):  
        for j in range(3):  
             
            if (keypad[i][j] != '*' and keypad[i][j] != '#'):
                totalCount += getCountUtil(keypad, i, j, n)
    return totalCount
 
keypad = [['1', '2', '3'],
          ['4', '5', '6'],
          ['7', '8', '9'],
          ['*', '0', '#']]
print(getCount(keypad, 1))

