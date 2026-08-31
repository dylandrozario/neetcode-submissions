class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lowOut = 0
        highOut = len(matrix) - 1

        while lowOut <= highOut:
            middleOut = (lowOut + highOut) // 2
            if target < matrix[middleOut][0]:
                highOut = middleOut -1 
            elif target > matrix[middleOut][-1]:
                lowOut = middleOut + 1
            else:
                break
        
        if not lowOut <= highOut:
            return False
        
        middleOut = (lowOut + highOut) // 2
        lowIn = 0
        highIn = len(matrix[middleOut]) - 1

        while lowIn <= highIn:
            middleIn = (lowIn + highIn) // 2
            if target < matrix[middleOut][middleIn]:
                highIn = middleIn - 1
            elif target > matrix[middleOut][middleIn]:
                lowIn = middleIn + 1
            else:
                return True
            
        return False