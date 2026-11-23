class Solution:
    #we want to encode a list of strings and return a new string in the process
    #how do i want to do this is the question
    #the first thing in my mind is that when I add strings together to one string
    #the computer must know when to stop to know that semblence of characters are
    # well a string can be comprised of any of the 256 valid ASCII characters
    # so firs thing i feel like is that we need an identifer to know when to stop
    # so we need a # percahnce and then the length of the string maybe?

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            templ = len(s)
            temp = str(templ) + "#" + s
            res += temp
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i : j])
            res.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return res
