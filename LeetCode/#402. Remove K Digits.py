class Solution(object):
    def removeKdigits(self, num, k):

        stack = []

        for i in range(len(num)):
            while(stack and int(num[stack[-1]]) > int(num[i]) and k > 0):
                stack.pop()
                k -= 1

            stack.append(i)

        ans = ""
        while(stack != []):
            if k > 0:
                stack.pop()
                k -= 1
                continue

            ele = stack.pop(0)
            ans += num[ele]

        return str(int(ans)) if ans != "" else "0"
