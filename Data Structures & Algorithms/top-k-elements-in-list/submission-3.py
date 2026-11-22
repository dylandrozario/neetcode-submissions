class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = defaultdict(int)
        #well why dont we just create an array of len that same as len of list
        #assume that this array is 1-idx so each idx therefore are related to count of that num
        
        ordered = [[] for i in range(len(nums) + 1)]
        res = []
        for n in nums:
            check[n] += 1
        
        for key, value in check.items():
            ordered[value].append(key)
        
        for i in range(len(nums), 0, -1):
            res.extend(ordered[i])

            if len(res) >= k:
                return res[:k]