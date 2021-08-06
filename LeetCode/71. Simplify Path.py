class Solution(object):
    def simplifyPath(self, path):
        i = 0;

        stack = []

        while(i<len(path)):

            if path[i] == "/":

                if stack != [] and stack[-1] == "/":
                    stack.pop()

                stack.append(path[i])
            elif path[i] == "." and i+2 < len(path) and path[i+1] == "." and path[i+2] == "." :
                stack.append("...")
                i += 2

            elif (path[i] == "." and i+1 < len(path) and path[i+1] == "." and stack[-1] == "/") and (i+2 >= len(path) or path[i+2] == "/"):
                
                if len(stack) > 1:
                    
                    stack.pop()
                    if len(stack) > 1:
                        stack.pop()
                i += 1
                
            elif path[i] == "." and stack[-1] == "/"  and ((i+1 < len(path) and path[i+1] == "/") or i+1 >= len(path)):
                i += 1
                continue

            else:
                if stack != [] and stack[-1] != "/":
                    stack[-1] += path[i]
                else:
                    stack.append(path[i])
            i += 1
            
        if len(stack) > 1 and stack[-1] == "/":
            stack.pop()
            
        ans = ""
        
        for pathOb in stack:
            ans += pathOb
            
        return ans
