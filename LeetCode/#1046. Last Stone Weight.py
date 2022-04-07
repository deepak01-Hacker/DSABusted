import heapq

class Solution(object):
    def lastStoneWeight(self, stones):
        
        for i in range(len(stones)):
            stones[i] = stones[i]*-1
            
        heapq.heapify(stones)
        
        
        while(len(stones)>1):
            x = heapq.heappop(stones)*-1
            y = heapq.heappop(stones)*-1
            
            if x != y:
                heapq.heappush(stones,abs(x-y)*-1)
                
        if len(stones) == 0:
            return 0
        return stones[0]*-1
        
