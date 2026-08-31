class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We want to find the longest consecutive sequence
        # Constraint is time complexity if O(n)
        # I am thinking of a default dict
        # where the value is a list of the consecutive sequence
        # the key will be the the first value of the sequence?
        # so we will loop through the sequence first to add to dicts
        # if value is not 1 greater than the value in the dict then it becomes a dict it self
        # However does this mean we need a nested for loop to check if the proceeding element
        # is one greater than last value
        # I think so
        # Second thought
        # what if we sort the array then search through it first then we can go throgh in one loop
        # however we still get the same issue of what if there is another squence
        # how do we deal with this
        # well then we can start making new lists in the dict and we dont have the check the previous
        # ones since they are not in the sequence cuz if they were it would've continued alr
        # after we get all the dicts we will run a separate loop in which we compare the value lengths and 
        # return the longest length

        longest = defaultdict(list)
        nums.sort()
        j = 0

        if len(nums) == 0:
            return 0

        # [0,1,1,2,3,4,5,6]
        # {[0, 1]}
        for i in range(len(nums)):
            if i == 0:
                longest[j].append(nums[i])
            elif nums[i] in longest[j]:
                continue
            elif nums[i] - 1 == longest[j][-1]:
                longest[j].append(nums[i])
            else:
                j = j + 1
                longest[j].append(nums[i])

        length = 0
        for val_list in longest.values():
            if(len(val_list) > length):
                length = len(val_list)
        
        return length
            