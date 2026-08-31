class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        integers = []

        if len(tokens) == 0:
            return 0
        
        for i in range(len(tokens)):
            elm = tokens[i]
            if elm == "+":
               integers.append(integers.pop() + integers.pop())
            elif elm == "-":
                b = integers.pop()
                a = integers.pop()
                integers.append(a - b)
            elif elm == "*":
                integers.append(integers.pop() * integers.pop())
            elif elm == "/":
                b = integers.pop()
                a = integers.pop()
                integers.append(int(float(a) / b))
            else:
                integers.append(int(elm))
        
        return integers[0]