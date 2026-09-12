class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #so we want to find length of longest substring w/o duplicates
        #so we have to look at each char and see if they already exist
        #we can do this with a set
        #if we encounter a duplicate we move the left pointer until there is
        #no duplicate it lands on then remove it from the set
        
        chars = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in chars:
                chars.remove(s[l])
                l += 1
            chars.add(s[r])
            res = max(res, r - l + 1)
        return res
