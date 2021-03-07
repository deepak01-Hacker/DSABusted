def isDifferAtOnePosition(word,string,endPoint):
    checker = 0
    for i in range(len(word)):
        if word[i] != string[i] and string[i] != endPoint[i]:
            checker += 1
        if checker > 1: 
            return False
    return True if checker == 1 else False



def transformation(beginWord,endWord,wordList):
    if endWord not in wordList:
        return 0
    ans = 5000**2
    queue = []
    queue.append(["hit",0])
    checker = set()
    while(queue):
        string = queue.pop(0)
        print(string)
        if string[0] == endWord:
            ans = min(ans,string[1])
            continue
        for word in wordList:
            if word not in checker and isDifferAtOnePosition(word,string[0],endWord):
                queue.append([word,string[1]+1])
                checker.add(word)
    return ans+1



if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    print(transformation(beginWord,endWord,wordList))
