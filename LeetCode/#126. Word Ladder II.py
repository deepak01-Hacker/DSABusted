alpha = "abcdefghijklmnopqrstuvwxyz"

class Solution(object):
    

    def util(self,word,end,adjMap,ans,temp):
        temp.append(word)
        if word == end:
            ans.append(tuple(temp))
            temp.pop()
            return True

        if word in adjMap:
            for wordAt in adjMap[word]:
                self.util(wordAt,end,adjMap,ans,temp)
        temp.pop()
        return


    def findLadders(self, begin, end, wordList):
        adj = {}
        checker = set(wordList)

        queue = []
        queue.append(begin)

        visited = {}
        visited[begin] = 0

        while(queue):

            curr = queue.pop(0)
            temp = list(curr[:])

            for i in range(len(curr)):

                for aplphabet in alpha:

                    if temp[i] == aplphabet:
                        continue

                    temp[i] = aplphabet

                    string = "".join(temp)

                    if string in checker:

                        if string not in visited:
                            visited[string] = visited[curr]+1
                            queue.append(string)
                            try:
                                adj[curr].append(string)
                            except:
                                adj[curr] = [string]

                        elif visited[string] == visited[curr]+1:
                            try:
                                adj[curr].append(string)
                            except:
                                adj[curr] = [string]

                temp[i] = curr[i]

        ans = []

        self.util(begin,end,adj,ans,[])

        return ans
