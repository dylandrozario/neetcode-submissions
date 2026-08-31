class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        while(l < r):
            if(self.isValid(s[l]) == False):
                l += 1
                continue;
            if(self.isValid(s[r]) == False):
                r -= 1
                continue;
            if(s[l].lower() == s[r].lower()):
                l += 1
                r -= 1
            elif(s[l].lower() != s[r].lower()):
                return False
        return True

    def isValid(self, ch: strs) -> bool:
        if((ord("A") <= ord(ch) <= ord("Z")) or 
          (ord("a") <= ord(ch) <= ord("z")) or
          (ord("0") <= ord(ch) <= ord("9"))):
            return True
        else:
            return False