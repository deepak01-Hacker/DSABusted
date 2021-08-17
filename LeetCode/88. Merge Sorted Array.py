import heapq as hp

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        heap = []
        hp.heapify(heap)

        i = 0
        j = 0
        while(i < m and j < n):
            
            hp.heappush(heap,nums1[i])
            hp.heappush(heap,nums2[j])

            nums1[i] = hp.heappop(heap)
            i += 1
            j += 1

        while(heap or i < m or j < n):
            
            if i < m:
                hp.heappush(heap,nums1[i])
            if j < n:
                hp.heappush(heap,nums2[j])
                
            nums1[i] = hp.heappop(heap)
            i += 1
            j += 1





