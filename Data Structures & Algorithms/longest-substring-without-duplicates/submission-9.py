class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #we want to find the longest substring of unique chars
        #the first approach that comes to mind is sliding window
        #where we will find a window of a valid substring and if not
        #then we shift the left pointer till it is not on a duplicate again
        #to track this substring we will use a set since it does not take
        #dupes

        l = 0
        check = set()
        res = 0
        for r in range(len(s)):
            while s[r] in check:
                check.remove(s[l])
                l += 1
            
            check.add(s[r])
            
            res = max(res, r - l + 1)
        return res