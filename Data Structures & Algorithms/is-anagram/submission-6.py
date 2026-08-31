class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #so we just want to check if the char counts of each string are the same or not
        #so we create two hashmaps and compare the keys if they are any differences then return False
        #how do actually do the comparing that is the hard part
        # is there a method for this?
        # i think we can just do a simple equality test lets try
        s1 = defaultdict(int)
        s2 = defaultdict(int)

        for c in s:
            s1[c] += 1
        
        for c in t:
            s2[c] += 1
        
        if s1 == s2:
            return True
        
        return False