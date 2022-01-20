class Solution(object):
    def setK(self,k,piles):
        hours = 0

        for pile in piles:

            if pile < k:
                hours += 1
            else:
                hours += pile//k

                hours += 1 if pile%k > 0 else 0
                #print(pile,k)
        return hours


    def minEatingSpeed(self, piles, h):
        low = 1
        high = max(piles)
        res = 10**10

        while(low<=high):
            mid = (low+high)//2

            ans = self.setK(mid,piles)
            #print("hours: ",ans," , number : ",mid)
            if ans <= h:
                high = mid-1
                res = min(res,mid)
            elif ans > h:
                low = mid+1

        return res

