class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        i = 0
        # 4#abcd2#ef
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_length = int(s[i:j])
            i = j + 1
            j = i + word_length
            strings.append(s[i:j])
            i = j
        return strings

