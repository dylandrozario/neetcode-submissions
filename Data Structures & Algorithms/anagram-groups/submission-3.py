class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #

        h = defaultdict(list)
        for s in strs:
            key = [0] * 26
            for c in s:
                idc = ord(c) - ord("a")
                key[idc] += 1
            h[tuple(key)].append(s)
        
        return list(h.values())
   