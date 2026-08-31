class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
        res = [1] * len(nums)

        # we want to first get an array 
        # of all numbers multipled to the left
        # of the current element
        # [1, 1, 2, 8]
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        # []
        for i in range(len(nums) - 1, -1 , -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res

