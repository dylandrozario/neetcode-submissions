class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = defaultdict(int)
        tLetters = defaultdict(int)

        if(len(t) != len(s)):
            return False

        for i in range(len(s)):
            sLetters[s[i]] += 1
            tLetters[t[i]] += 1
    
        for letter in sLetters:
            if(sLetters[letter] != tLetters[letter]):
                return False
    
        return True

        