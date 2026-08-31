class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "/", "*"]
        for token in tokens:
            if(token in operators):
                val = (stack.pop())
                val2 = (stack.pop())
                if token == "+":
                    val3 = val + val2
                elif token == "-":
                    val3 = val2 - val
                elif token == "/":
                    val3 = int(float(val2)/ val)
                elif token == "*":
                    val3 = val * val2
                stack.append(val3)
            else:
                stack.append(int(token))
        if stack[-1] not in operators: 
            return stack[-1]
