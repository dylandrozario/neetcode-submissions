class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        check = {}
        res = {}

        # frequency of s1
        for c in s1:
            check[c] = 1 + check.get(c, 0)

        l = 0
        for r in range(len(s2)):
            # add right char
            if s2[r] in check:
                res[s2[r]] = 1 + res.get(s2[r], 0)
            else:
                # reset window if char not in s1
                res.clear()
                l = r + 1
                continue

            # shrink window if too big
            if (r - l + 1) > len(s1):
                left_char = s2[l]
                res[left_char] -= 1
                if res[left_char] == 0:
                    del res[left_char]
                l += 1

            # check match
            if res == check:
                return True

        return False

            