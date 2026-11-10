class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = defaultdict(int)

        for n in nums:
            check[n] += 1
        
        for val in check.values():
            if val > 1:
                return True
        return False