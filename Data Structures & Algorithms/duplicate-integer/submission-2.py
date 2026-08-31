class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #we want to see there is a duplicate in an array
        #so we can use a hashmap here
        #first we want to make the key for the number in it
        #then cycle through first to make the hashmap adding to kv if there is a duplciate
        #then we finally cycle the values and see if any val is greater than 1
        #if there is then return true
        #else return false

        hmap = defaultdict(int)

        for num in nums:
            hmap[num] += 1
        
        for val in hmap.values():
            if val > 1:
                return True
        
        return False