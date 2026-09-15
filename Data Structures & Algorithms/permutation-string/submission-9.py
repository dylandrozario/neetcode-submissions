class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #so we are given two strings
        #we want to return true if s1 exists as a premutation in s2 
        #so in my mind i want to use sliding window
        #the window will be the length of s1
        #once we hit the length we also record the chars we have in the window
        #and if they 

        if len(s1) > len(s2):
            return False

        h1 = [0] * 26
        h2 = [0] * 26

        for i in range(len(s1)):
            h1[ord(s1[i]) - ord("a")] += 1
            h2[ord(s2[i]) - ord("a")] += 1
        
        matches = 0
        for i in range(26):
            if h1[i] == h2[i]:
                matches += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord("a")
            h2[index] += 1
            if h1[index] == h2[index]:
                matches +=1
            elif h1[index] + 1 == h2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord("a")
            h2[index] -= 1
            if h1[index] == h2[index]:
                matches += 1
            elif h1[index] - 1 == h2[index]:
                matches -= 1
            l += 1
        return matches == 26
