class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        seq = {"[": "]", "(": ")", "{": "}"}

        for char in s:
            if char in seq:              # it's an opening bracket
                stack.append(char)
            else:                        # it's a closing bracket
                if not stack or seq[stack[-1]] != char:
                    return False
                stack.pop()

        return stack == []
        
        

        
