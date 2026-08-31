class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #so we want to group each anagram in their respective group
        #how do we know if an anagram is an anagram
        # 1. if both strings are same length
        # 2. if both strings have the same chars 
        # so then how do we group them
  
      
        sol = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord("a")] += 1
            sol[tuple(count)].append(s)
        
        return list(sol.values())