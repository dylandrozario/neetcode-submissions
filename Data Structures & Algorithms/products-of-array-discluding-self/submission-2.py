class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #we want to find all the products of each position exluding the current
        #position element we are on
        #the first thing that pops in mind is two pointers
        #Actually we are going to use a hashmap
        #so what if we had two hashmaps
        #the first one we make the key the index and the value is that element
        #the second one is a list we store with all 1's then we mutiply the list by cylcing through each element and if the eindixesdontmatch multiply
        #so the neetcode solution is that we first take the products of everything before the current element you are on store that in the res array
        #the second cycle we store the product of everything after the current element
        #to remedy the fact the first and last element may not have either an element before or after it we start by multiply each cycle by 1

        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        
        return res
