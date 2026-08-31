class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if(len(nums) == 0):
            return []
        
        l = 0
        res = []

        for r in range(k, len(nums) + 1):
            maxElement = float("-inf")
            for i in range(l,r):
                maxElement = max(maxElement, nums[i])
            res.append(maxElement)
            l += 1
        return res
