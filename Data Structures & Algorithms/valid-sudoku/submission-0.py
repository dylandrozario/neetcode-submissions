class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we have a 9x9 board
        # There are 9 sub-grids inside the grid
        # we have to check if each sub-grid if they are valid
        # if all sub-grids are valid then we return true
        # How can we solve this
        # A sub-grid is valid if each row and column in the sub-grid do not have duplicates, 
        # we ignore "." and don't count them
        # How can we achieve this
        # Every 3 elements will be a different sub-grid, so we need to create a hashmap of 9 
        # key-value pairs, the key will be the number of the sub-grid and the value will be an
        # list of the values
        # how can we do this, we make a for loop and have a counter if it increases each time 
        # if we exceed the 3 elements in the sub-grid, so it moves to the next sub-grid, the counter
        # value will act as the key for the hashmap, we will end the loop at the length of the board
        # I realized we need another loop to check for other rows so minimum time comp will be O(n^2)
        # My methos does not work bc actually the entire row and entire column must not contain
        # duplicates as well
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True