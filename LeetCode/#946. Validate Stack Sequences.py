class Solution(object):
    def validateStackSequences(self, pushed, popped):
        if len(pushed) != len(popped):
            return False

        stack = []
        i = 0
        j = 0

        while(i < len(pushed)):
            stack.append(pushed[i])
            i += 1

            while(stack and stack[-1] == popped[j]):
                stack.pop()
                j += 1
        if stack:
            return False
        return True

        
