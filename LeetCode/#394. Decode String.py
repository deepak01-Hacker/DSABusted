class Solution(object):
    def decodeString(self, s):
        stack = [[-1,""]]

        res = ""
        digi = ""

        for i in range(len(s)):
            if s[i] >= "0" and s[i] <= "9":
                digi += s[i]
            elif s[i] == "[":
                stack.append([int(digi),""])
                digi = ""
            elif s[i] == "]":
                res = stack.pop()
                stack[-1][1] += res[1]*res[0]
            elif digi == "":
                stack[-1][1] += s[i]

        return stack[-1][1]
