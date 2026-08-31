class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        
        l = 0
        check = {}
        res = {}

        for i in range(len(s1)):
            check[s1[i]] = 1 + check.get(s1[i], 0)

        for r in range(len(s2)):
            if(s2[r] in check):
                res[s2[r]] = 1 + res.get(s2[r], 0)
            else:
                res.clear()
                l = r + 1
                continue
            
            if((r - l + 1) > len(s1)):
                res[s2[l]] -= 1
                if(res[s2[l]] == 0):
                    del res[s2[l]]
                l += 1
            
            if(res == check):
                return True
        
        return False
            