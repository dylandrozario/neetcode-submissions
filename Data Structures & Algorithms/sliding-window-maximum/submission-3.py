class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        indices = deque()
        l,r = 0,0

        while r < len(nums):
            while indices and nums[r] > nums[indices[-1]]:
                indices.pop()
            indices.append(r)

            if l > indices[0]:
                indices.popleft()

            if(r + 1 >= k):
                res.append(nums[indices[0]])
                l += 1
            r += 1
        return res

