class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #so we want to go in O(n) time to find the longest pattern where the elements increase by 1
        #the elements do not have to be consecutive in the og array
        #we want to return the length of what the longest pattern is 
        #how do we know if we are the start of a sequence or not
        #we have to check whether or not the current number - 1 exits or not
        
        numsSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in numsSet:
                length = 0
                while (n + length) in numsSet:
                        length += 1
                longest = max(longest, length)
        
        return longest
                    
            