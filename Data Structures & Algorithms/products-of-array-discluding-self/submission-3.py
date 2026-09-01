class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       #We want to return an array of the elements in the og array
       #st that each element is the product of every element except itself
       #how can we accomplish this in O(n) time comp
       #i firs thinking of seperating how we multiply each element into 2 stages
       #multiply all the numbers before the current element and multiply all the      #elements after the current element
       #for the first and last element we would assume that the numbers in that spot is 1
       # [1,2,4,6]
       # before [1, 1, 2, 8]
       # after [48,24, 6, 1]
       # total [48, 24, 12, 8]
       # how can we do this in a single pass
       # so first we have pre

       
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] *= prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
