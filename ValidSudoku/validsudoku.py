class Solution(object):
    def isValidSudoku(self, board):
        seen = set()    # set improves performance as it's unchangeable and unindexed

        for r, row in enumerate(board):
            for c, val in enumerate(row):
                if val != ".":
                    if (val, r) in seen or (c, val) in seen or (r//3, c//3, val) in seen:
                        return False
                    else:
                        seen.add((val,r))
                        seen.add((c,val))
                        seen.add((r//3, c//3, val))

        return True

class Test:
    board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

    board2 = [
    ["8","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
    ]

    test = Solution()

    print("Example 1: ", test.isValidSudoku(board1))
    print("Example 2: ", test.isValidSudoku(board2))
