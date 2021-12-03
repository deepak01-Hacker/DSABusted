class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        product = -11
        
        minus = 1
        tempProduct = 1
        for num in nums:
            
            tempProduct *= num
            minus *= num

            #print(minus,tempProduct)
            
            if minus > num:

                temp = minus
                minus = min(tempProduct,num)
                tempProduct = max(num,temp,tempProduct)
            
            if tempProduct < num:
                temp = tempProduct
                tempProduct = max(num,minus)
                minus = min(temp,minus,tempProduct)
            
                
            product = max(tempProduct,product)
        return product
        
