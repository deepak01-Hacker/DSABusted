class Solution(object):
    def largestRectangleArea(self, arr):
        ans = 0
        stack = []

        for i in range(len(arr)):

            while(stack != [] and arr[stack[-1]] > arr[i]):

                hist = stack.pop()

                if stack :

                    index = (i-stack[-1]-1)

                else:
                    index = i

                area = index*arr[hist]

                #print(index,area,stack,arr[hist])

                ans = max(ans,area,arr[i])

            stack.append(i)

        if stack == []:
            return 

        #print(stack)

        maxs = stack[-1]
        while(stack):

            t = stack.pop()

            h = arr[t]

            if stack == []:

                index = (maxs-t) + (t+1)

                #print(maxs,t,i+1)

            else:
                index = (maxs-t) + (t-stack[-1])

                #print(index)


            ans = max(ans,h*index)

        return ans
