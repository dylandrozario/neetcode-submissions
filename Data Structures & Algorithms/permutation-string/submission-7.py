class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #okay so we need to use a sliding window tech here
        #we need to count the amount of chars in the first string add it to a hashmap
        #then move the window till it reaches said len then check if hashmap of s2
        #is the same as hashmap as s1 if not decrement the hashmap and increment l pointer

        hash1 = {}
        hash2 = {}
        l = 0
        maxLen = len(s1)

        for i in range(len(s1)):
            hash1[s1[i]] = 1 + hash1.get(s1[i], 0)
        
        for r in range(len(s2)):
            if (r - l + 1) > maxLen:
                if hash1 == hash2:
                    return True
                hash2[s2[l]] -= 1
                if hash2[s2[l]] == 0:
                    del hash2[s2[l]]
                l += 1
            hash2[s2[r]] = 1 + hash2.get(s2[r], 0)
        
        if hash1 == hash2:
                    return True
        return False
            
            