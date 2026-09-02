class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        grids = defaultdict(set)

        for row in range(9):
            for col in range(9):
                el = board[row][col]
                if el == ".":
                    continue
                if(el in rows[row] or el in columns[col] or el in grids[(row//3, col//3)]):
                    return False
                rows[row].add(el)
                columns[col].add(el)
                grids[(row//3, col//3)].add(el)
        
        return True