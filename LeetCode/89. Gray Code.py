class Solution(object):
    def grayCode(self, n):
        res = []

        st = "0"*n
        res.append(st)
        checker = set()
        checker.add(st)

        nth = 2**n
        for i in range(nth):
            st = list(res[-1])
            #print(st)

            for k in range(len(st)-1,-1,-1):
                temp = st[:]
                temp[k] = "0" if st[k] == "1" else "1"
                temp = "".join(temp)
                #print(temp,st)

                if temp not in checker:
                    res.append(temp)
                    checker.add(temp)
                    break

        for j in range(len(res)):
            res[j] = int(res[j],2)
        return res
        
