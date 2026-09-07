class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #so we want to find 3 unique elements that sum to 0
        #the approach I am thinking of is doing two pointers
        #how do i want to do this is by going through each element one by one
        #then findint the next two elements by a standard two pointers search
        #I also want to avoid adding duplicates solutions so i will check if the
        #current element is the same as the previous
        #but also in my left pointer once I do find a solution if the next pointer is 
        #again same as left one since that would add a duplicate
        #we need to sort since trad two pointers appr needs to work

        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if a > 0:
                break

            if i > 0 and nums[i - 1] == a:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                if(a + nums[r] + nums[l] > 0):
                    r -= 1
                elif(a + nums[r] + nums[l] < 0):
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
        return res