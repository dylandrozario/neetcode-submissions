class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s)-1

        while l < r:
            if not self.isAlphaNum(s[l]):
                l += 1
                continue
            elif not self.isAlphaNum(s[r]):
                r -= 1
                continue

            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True
    
    def isAlphaNum(self, s: str) -> bool:
        if (ord("Z") >= ord(s) >= ord("A") or 
            ord("z") >= ord(s) >= ord("A") or
            ord("9") >= ord(s) >= ord("0")):
            return True
        return False
