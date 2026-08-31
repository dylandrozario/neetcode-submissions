class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #we have a list of numbers
        #we want to find the k most fequenet elements in that list
        #we return k numbers in a list in any order
        #how do we find this max
        #well cant we find hashmap based on val:freq
        #then how do we find k most
        #well we can make a list of k spaces
        #fill them

        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
