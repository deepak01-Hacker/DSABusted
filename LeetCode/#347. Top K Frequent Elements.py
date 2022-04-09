import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        ans = []
        
        map = {}
        for i in range(len(nums)):
            try:
                map[nums[i]] += 1
            except:
                map[nums[i]] = 1
        
        heapq.heapify(ans)
        
        for key in map.keys():
            heapq.heappush(ans,(map[key],key))
            
            if len(ans) > k:
                heapq.heappop(ans)
        result = []
        
        for i in range(len(ans)):
            st,end = heapq.heappop(ans)
            
            result.append(end)
        return result[::-1]
            
            
            
            
