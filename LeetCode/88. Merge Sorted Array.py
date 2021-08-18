#----------------o(n)- -----------------

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = m-1
        right = n-1

        i = (m+n)-1

        while(left >= 0 and right >= 0):
            if nums1[left] > nums2[right]:
                nums1[i] = nums1[left]
                left -= 1
            else:
                nums1[i] = nums2[right]
                right -= 1
            i -= 1

        while(left >= 0):
            nums1[i] = nums1[left]
            left -= 1
            i -= 1

        while(right >= 0):
            nums1[i] = nums2[right]
            right -= 1
            i -= 1




#------------- n(logn) ------------------

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





