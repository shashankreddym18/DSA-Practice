class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        x = len(grid)
        y = len(grid[0])
        ans = [[0] * y for _ in range(x)]
        onesRow = [row.count(1) for row in grid]
        onesCol = [col.count(1) for col in zip(*grid)]

        for i in range(x):
          for j in range(y):
            ans[i][j] = onesRow[i] + onesCol[j] - \
                (y - onesRow[i]) - (x - onesCol[j])

        return ans