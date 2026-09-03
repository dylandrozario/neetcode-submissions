class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # so we want to find the pair of indices that will add up to target
        # there will always be a pair
        # the pair cannot be the same element twice
        # the first index has to be less than second index
        # so in my mind we use two pointers here
        # since the array is sorted and we have pointers on either side
        # we can adjust if the sum is too little we increase l or too big 
        # we can decrease r until we hit the sum and return the pair
        
        l = 0
        r = len(numbers) - 1
        while l < r:
            pot = numbers[l] + numbers[r]
            if pot > target:
                r -= 1
                continue
            elif pot < target:
                l += 1
                continue
            return [l + 1, r + 1]