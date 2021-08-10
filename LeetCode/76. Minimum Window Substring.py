class Solution(object):
    def hashSet(self,st):
        hashS = {}

        for val in st:
            try:
                hashS[val] += 1 
            except:
                hashS[val] = 1

        return hashS


    def minWindow(self, s, t):

        if len(s) < len(t):
            return ""
    

        hasht = self.hashSet(t)
        hashs = {}

        counter = 0
        ans = [0,len(s)]
        Ans = False

        i = 0
        j = 0
        while(j <= len(s)):

            #print(i,j,counter)


            if counter == len(hasht):
                Ans = True
                if (j - i) < (ans[1]-ans[0]):
                    ans = [i,j]

                if s[i] in t:
                    hashs[s[i]] -= 1
                    if hashs[s[i]] < hasht[s[i]]:
                        counter -= 1

                i += 1
            elif j >= len(s):
                break

            else:
                if s[j] in t:
                    try:
                        hashs[s[j]] += 1
                    except:
                        hashs[s[j]] = 1

                    if hashs[s[j]] == hasht[s[j]]:
                        counter += 1
                j += 1



        return s[ans[0]:ans[1]] if Ans else ""

