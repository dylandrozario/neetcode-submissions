class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # so we want to find max area between two points 
        # each point is in form of (x,y) -> (index + 1, value)
        # to compute area we must do x_2 - x_1 (times) (which either height is smaller)
        # so we want to find the maximum
        # how do we do this
        # so we have a left pointer on start of array and right pointer on last index
        # then we find the area 
        # if either of the pointers neigherbor is greater than its self then move the pointer 
        # compute the area
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return res

            