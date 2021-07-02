class Solution(object):
    def findSubstring(self, s, L):
        sizeWord = len(L[0])
        wordCount = len(L)
        sizeL = sizeWord*wordCount

        res = []

        if sizeL > len(s):
            return res

        hashmap = {}

        for i in range(wordCount):
            if L[i] in hashmap:
                hashmap[L[i]] += 1

            else:
                hashmap[L[i]] = 1

        for i in range(0,len(s)-sizeL+1,1):
            temphashmap = hashmap.copy()
            j = i
            count = wordCount

            while(j < i + sizeL):

                word = s[j:j+sizeWord]

                if word not in hashmap or temphashmap[word] == 0:
                    break

                else:
                    temphashmap[word] -= 1

                    count -= 1

                j += sizeWord

            if count == 0:
                res.append(i)

        return res
