class Solution:
        #what are unique ways a string can be identifed
        #the len of stirng
        #chars in a string
        #asicc of each char
        #
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = str(len(s)) + "#" + s
            res += l
        return res
        #apple, jack, monk -> 5#apple4#jack4#monk
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            n = j + 1
            res.append(s[n : length + n])
            i = length + n  
        return res