class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                tempt, tempi = stack.pop()
                res[tempi] = i - tempi
            stack.append([t, i])
        return res