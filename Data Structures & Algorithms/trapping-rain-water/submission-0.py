class Solution:
    def trap(self, height: List[int]) -> int:
        # we are given an array of heights
        # each index is the x coordinate - 1
        # each element is the y coordinate
        # we want to find the max water possible between two bars
        # we must account for the space taken up by bars in between
        # for trapped water to be valid there has to be bars on both side
        # now taking from the previous problem rain water
        # we used a left pointer on start of array and right pointer at the end of array
        # then we move a pointer if one of them was smaller than the other
        # now how do we approach this problem
        # so we need to have a valid section
        # how do we do this
        # we check the neighbor if it is the same height as the pointer 
        # or greater height than pointer
        # if this happens directly then no water trapped
        # if we had space before 
        # mmm i am thinking about another way to view with the heights
        # i noticed that the 0 show water that can be used
        # and at times the parts of water that can fit looks palindronmic on the array
        # so can we just start counting a 'real' water potential when we meet pointers who have
        # the same height
        # then we do the neighbor checking like before
        # Now how do we solve the problem of getting the water area
        # the first thought in my mind is to just find the area ignoring the space first
        # then we substract the blocks inside from the area
        # since each block is 1 unit we can count each bar and add them
        # then subtract them from the available space 
        # now how do we move the pointers
        # we check if a pointer is next to a 0  and if 'free' for water, ie neighbor bar is not
        # greater or equal height as pointer
        # I realized my logic is not correct
        # because you can contain water with bars of dffering heights, there just must have space
        # between them, its area is just the height of the smaller bar
        # so let me think from the beginning
        # first we check if the first index or last index is 0, if yes then both the pointers 
        # for that is true by 1
        # now we do real checking
        # i think we assume if we have a potential area if we get two heights that are differing
        # we stop counting this area if the 0 is next to a bar greater in height than 
        # one of the pointers
        # i give up
        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
