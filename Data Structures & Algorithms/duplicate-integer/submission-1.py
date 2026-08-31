class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsMap = defaultdict(int)

        for num in nums:
            numsMap[num] += 1
        
        for num in numsMap:
            if numsMap[num] > 1:
                return True
        
        return False