class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #so we want to find 2 unique elements that add up to the target
        # so i just realized that if we make a kv pair of the index of element being 
        # the key and the value being the second number needed to be added in order
        # to sum to the target, we can find this by doing target - element at that index
        #then after we complete that array how do we make sure that such pair exists
        # [0:4,1:3,2:2,3:1] [3,4,5,6]
        
        remains = defaultdict(int)

        for i in range(len(nums)):
            remains[i] = target - nums[i]
        
        for key in remains:
            if remains[key] in nums:
                if key == nums.index(remains[key]):
                    continue
                elif key > nums.index(remains[key]):
                    return [nums.index(remains[key]), key]
                elif key < nums.index(remains[key]):
                    return [key, nums.index(remains[key])]
        