class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        check = defaultdict(int)

        for n in nums:
            check[n] += 1
        
        for key, val in check.items():
            if val > len(nums) / 2:
                return key
        