class Solution(object):
    def setZeroes(self, matrix):
        row = set()
        col = set()

        rsize = len(matrix)
        csize = len(matrix[0])

        for r in range(rsize):
            for c in range(csize):
                if matrix[r][c] == 0:
                    row.add(r)
                    col.add(c)

        for c in col:
            for i in range(rsize):
                matrix[i][c] = 0    # Set each marked 0 column to 0
        for r in row:
            for j in range(csize):
                matrix[r][j] = 0    # Set each marked 0 row to 0

class Test:
    matrix1 = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
    ]

    matrix2 = [
    [0, 1, 2, 0],
    [3, 4, 5, 2],
    [1, 3, 1, 5]
    ]

    test = Solution()

    print("Example 1: ", test.setZeroes(matrix1))
    print("Example 2: ", test.setZeroes(matrix2))
