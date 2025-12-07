# too easy dynamic programming
import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip("\n")))

n, m = len(grid), len(grid[0])
dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(1, n):
    for j in range(m):
        if grid[i - 1][j] == "S":
            dp[i][j] = 1
        if grid[i - 1][j] == ".":
            if grid[i][j] == ".":
                dp[i][j] += dp[i - 1][j]
            if grid[i][j] == "^":
                if j:
                    dp[i][j - 1] += dp[i - 1][j]
                if j + 1 < m:
                    dp[i][j + 1] += dp[i - 1][j]
print(sum(dp[-1]))
