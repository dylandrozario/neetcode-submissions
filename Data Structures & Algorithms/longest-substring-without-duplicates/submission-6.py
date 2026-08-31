class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        l = 0
        maxLen = 0
        
        for r in range(len(s)):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            maxLen = max(maxLen, (r - l) + 1)
        
        return maxLen
