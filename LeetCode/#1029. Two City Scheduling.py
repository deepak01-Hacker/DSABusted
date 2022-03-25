class Solution(object):
    def twoCitySchedCost(self, arr):
        arr.sort(key=lambda x : abs(x[1]-x[0]),reverse = True)

        #print(arr)


        cost = 0

        l=0
        r = 0

        i = 0

        while(i<len(arr)):
            a,b = arr[i]

            if l == len(arr)//2 or r == len(arr)//2:
                break

            if a < b:
                cost += a
                l += 1
            else:
                cost += b
                r += 1

            i += 1

        while(l < len(arr)//2):
            a,b = arr[i]
            cost += a
            l += 1
            i += 1

        while(r < len(arr)//2):
            a,b = arr[i]
            cost += b
            r += 1
            i += 1

        return cost



