class Solution(object):
    def isValid(self, st):
        stack = []

        for i in range(len(st)):
            # print(stack)
            if stack != [] and (st[i] != "(" and st[i] !="[" and st[i] != "{"):
                if stack[-1] == "(" and st[i] == ")":
                    stack.pop()
                elif stack[-1] == "{" and st[i] == "}":
                    stack.pop()
                elif stack[-1] == "[" and st[i] == "]":
                    stack.pop()
                else:
                    #print(stack)
                    return False
            else:
                stack.append(st[i])
        #print(stack)
        return True if stack == [] else False
