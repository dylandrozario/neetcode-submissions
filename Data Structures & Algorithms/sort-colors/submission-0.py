class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        #so we want to sort an array from 0 idx to end with elements group by their 
        #likeness so 0 then 1 then 2
        # well we can do this since they are in numeric order
        # the first thing in my mind is shifting based on numeric valuee
        # but now how do we actually do the shifting
        # I think if we find something we just shift the places of them
        # but can we do this in O(n) time?
        #[2,1,0,2,1]
        #[1,2,0,2,1]
        #[1,0,2,2,1]

        l = 0
        r = len(nums) - 1
        i = 0

        def swap(i, p):
            temp = nums[p]
            nums[p] = nums[i]
            nums[i] = temp
        
        while i <= r:
            if nums[i] == 0:
                swap(i, l)
                l += 1
            elif nums[i] == 2:
                swap(i, r)
                r -= 1
                i -= 1
            i += 1
                
            

        