class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(list)

        for i in range(len(nums)):
            dic[nums[i]] = i
        
        for i in range(len(nums)):
            aim = target - nums[i]
            if aim in dic and dic[aim] != i:
                return [i, dic[aim]]
        return []

        
       

