class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = 0.0
        
        length = len(nums1) + len(nums2)
        medianLen = (length//2)+1
        
        curr = 1
        prev = curr
        
        i = 0
        j = 0
        
        
        while(medianLen and (i < len(nums1) or j < len(nums2))):
            prev = curr
            
            first = 10**7
            last  = 10**7
            
            if i < len(nums1):
                first = nums1[i]
            if j < len(nums2):
                last = nums2[j]
            
            if first < last:
                i += 1
                curr = first
            else:
                j += 1
                curr = last
            
            medianLen -= 1
            
        return curr/1.0 if length%2 != 0 else (curr+prev)/2.0
        
        
