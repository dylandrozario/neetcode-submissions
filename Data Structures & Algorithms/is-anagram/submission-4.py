class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()

        if len(s) != len(t):
            return False
        

        for i in range(len(s)):
            if s[i] in s_map.keys():
                j = s_map[s[i]] + 1
                s_map[s[i]] = j
            
            else:
                s_map[s[i]] = 1
            

        for i in range(len(t)):
            if t[i] in t_map.keys():
                j = t_map[t[i]] + 1
                t_map[t[i]] = j
            
            else:
                t_map[t[i]] = 1
            
        
        if s_map == t_map:
            return True
        
        return False


        