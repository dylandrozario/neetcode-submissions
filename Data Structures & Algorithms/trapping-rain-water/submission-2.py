class Solution:
    def trap(self, height: List[int]) -> int:
        #so we want to find the total amount of water trapped
        #this is defined by the empty space between two element and the area of that space set to a limit of the smaller element height
        #the equation to find the amount of water is min(l, r) - h[i] for the current element
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        res = 0

        if not height:
            return 0
            
        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(height[l], maxL)
                res += maxL - height[l]
            else:
                r -= 1
                maxR = max(height[r], maxR)
                res += maxR - height[r]
        
        return res
