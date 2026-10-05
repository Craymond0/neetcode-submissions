class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        l = 0
        r = rows * cols - 1

        while l <= r:
            m = (l + r) // 2

            col = m % cols
            row = m // cols

            if matrix[row][col] > target:
                r = m - 1
            elif matrix[row][col] < target:
                l = m + 1
            else:
                return True

        return False
