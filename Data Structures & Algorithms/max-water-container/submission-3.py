class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            width = r - l
            length = min(heights[r], heights[l])
            res = max(res, width * length)

            if length == heights[l]:
                l += 1
            else:
                r -= 1
            
        return res