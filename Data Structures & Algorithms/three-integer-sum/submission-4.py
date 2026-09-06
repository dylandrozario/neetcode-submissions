class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #we want to find all 3 element combinations that are unique
        #i can return the output of triplets in any order
        #so i am thinking what if i sort first
        #then we use two pointers to figure out all the combinations
        #[-4, -1, -1, 0, 1, 2]
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            a = nums[i]

            if a > 0:
                break

            if i > 0 and nums[i - 1] == a:
                continue
            
            l, r = i + 1, len(nums) - 1
    
            while l < r:
                att = a + nums[l] + nums[r]
                if att > 0:
                    r -= 1
                elif att < 0:
                    l += 1
                else:
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return res