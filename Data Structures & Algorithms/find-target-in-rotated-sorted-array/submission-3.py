class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif nums[m] >= nums[l] and target < nums[l] and target < nums[m]:
                l = m + 1
            elif nums[m] >= nums[l] and target > nums[l] and target > nums[m]:
                l = m  + 1
            elif nums[m] < nums[l] and target > nums [m] and target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        return -1