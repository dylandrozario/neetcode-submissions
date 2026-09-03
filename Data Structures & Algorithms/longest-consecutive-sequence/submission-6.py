class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # we want to find the length of the longest consecutive sequence
        # based on an array of integers
        # in order to be consecutive the next element has to be 1 greater than the element before
        # how do we know we are at the start of a new sequence
        # we have to check if current element - 1 exists
        # if it does exist then the current elemene needs to be added
        #how can do this in O(n), we have to use a hashset since each element is unique and we want O(1) look up
        # since we have a hashset for lookups then we can begin by looking if an element one greater exists or not
        # and we can do this for each element that is the start and compare the lengths till we have find one
        
        numbers = set(nums)

        res = 0
        for n in nums:
            length = 1
            if n - 1 not in numbers:
                while n + length in numbers:
                    length += 1
                res = max(res, length)
        
        return res