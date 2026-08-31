class Solution:
    def minWindow(self, s: str, t: str) -> str:
            if(len(t) > len(s) or t == ""):
                return ""
            
            res = [-1, -1]
            resLen = float("infinity")
            check = {}
            temp = {}

            for i in range(len(t)):
                check[t[i]] = 1 + check.get(t[i], 0)
            
            have = 0
            need = len(check)
            l = 0

            for r in range(len(s)):
                temp[s[r]] = 1 + temp.get(s[r], 0)

                if(s[r] in check and temp[s[r]] == check[s[r]]):
                    have += 1
                
                while(have == need):
                    if((r - l + 1) < resLen):
                        res = [l, r]
                        resLen = r - l + 1
                
                    temp[s[l]] -= 1
                    if(s[l] in check and temp[s[l]] < check[s[l]]):
                        have -= 1
                    l += 1
            l = res[0]
            r = res[1]
            return s[l: r + 1] if resLen != float("infinity") else ""