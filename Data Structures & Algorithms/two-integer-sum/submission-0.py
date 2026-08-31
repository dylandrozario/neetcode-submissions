class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #I want to check a number with all following numbers
        #what is the best way to do this
        #make a hashmap and the key is the number and the 
        #I will brute force it first
        target_indices = []

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    target_indices.append(i)
                    target_indices.append(j)

        target_indices.sort()
        return target_indices
        
