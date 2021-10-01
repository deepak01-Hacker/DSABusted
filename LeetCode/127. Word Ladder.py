alpha = "abcdefghijklmnopqrstuvwxyz"

class Solution(object):
    def ladderLength(self, begin, end, wordList):

        depth = 0
        visited = {}

        checker = set(wordList)

        queue = []

        queue.append(begin)

        while(queue):

            length = len(queue)

            depth += 1

            while(length):
                qWord = queue.pop(0)

                if qWord == end:
                    return depth

                temp = list(qWord)

                for i in range(len(qWord)):

                    for alphabet in alpha:

                        if temp[i] == alphabet:
                            continue

                        temp[i] = alphabet

                        string = "".join(temp)
    

                        if string not in visited and string in checker:
            
                            visited[string] = True
                            queue.append(string)

                        temp[i] = qWord[i]

                length -= 1

        return 0
