class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            count = 0
            isOver = False
            for j in range(i + 1, len(temperatures)):
                if(temperatures[i] < temperatures[j]):
                    count += 1
                    isOver = True
                    break
                count += 1
            if(isOver):
                result.append(count)
            else:
                result.append(0)
        return result