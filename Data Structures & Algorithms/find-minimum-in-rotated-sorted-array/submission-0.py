class Solution:
    def findMin(self, nums: List[int]) -> int:
        #so my inital thought is splitting the array if we find something out of order
        #so we always know that it can be rotated 1 - n times 


        l = 0
        r = len(nums) - 1
        low = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                low = min(low, nums[l])
                break
            m = (l + r) // 2
            low = min(low, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return low
