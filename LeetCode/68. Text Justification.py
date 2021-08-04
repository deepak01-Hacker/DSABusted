class Solution(object):
    def perform(self,words,start,end,total_len,maxWidth):
        line = ""

        space = maxWidth-total_len
        if end-start == 1:
            perWordSpac = maxWidth-total_len
            space = perWordSpac
        else:
            perWordSpac = int((space/(end-1-start))+0.5)


        for i in range(start,end):
            line += words[i]

            if space >= perWordSpac:
                line += " "*perWordSpac

                space -= perWordSpac
            else:
                line += " "*space
                space = 0

        line += " "*space

        return line

    def fullJustify(self, words, maxWidth):
        ans = []
        start = 0
        end = 0
        total_len = 0

        for i in range(len(words)):
            space = end-start
            if total_len+space+len(words[i]) > maxWidth :

                st = self.perform(words,start,end,total_len,maxWidth)
                ans.append(st)
                start = i
                total_len = 0

            end = i+1
            total_len += len(words[i])

        if end-start > 0:
            st = self.perform(words,start,end,total_len,maxWidth)
            ans.append(st)

        return ans
