class Solution:
    def climbStairs(self, n: int) -> int:
        # D[i] = number of distinct ways to reach i steps
        # base cases: D[0] = 1, D[1] = 1, D[2] = 2
        # D[i] = D[i - 1] + D[i - 2]

        one = 1
        two = 1

        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one
