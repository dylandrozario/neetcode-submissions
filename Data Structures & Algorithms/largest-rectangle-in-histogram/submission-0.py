class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # in my mind we need to have a max count of sorts and update if we find
        # a bigger rectangle
        # also a smallest counter to see when to stop counting that rec?
        # nevermind i was thinking now of starting from the last element of given
        # array
        # then we put in the largest element in the stack
        # we then calculate the largest and have a current
        # we cycle through and then add the next element 
        
        maxA = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxA = max(maxA, height * (i - index))
                start = index
            stack.append((start,h))
        
        for i, h in stack:
            maxA = max(maxA, h * (len(heights) - i))
        
        return maxA
        
       
            