class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # we have a string of uppercase letters
        # we have an integer k which is our constraint
        # we want to create the longest substring of one char and can replace 
        # an chars in the string at most k times to create that substring
        # so the first approach that i am thinking about is finding the start and end positions
        # of each char and see what can be the longest substring for that 
        # we can do this by taking the legnth of what is known vs unknown
        # then doing known + (unknown - k), this will give the longest substring
        # actually this does not work out
        

        l = 0
        res = 0
        count = defaultdict(int)
        maxf = 0
        for r in range(len(s)):
            count[s[r]] += 1
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res