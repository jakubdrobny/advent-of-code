import sys

grid = []
for line in sys.stdin:
    grid.append(list(line.strip("\n")))

n, m = len(grid), len(grid[0])
ans = 0
for i in range(1, n):
    for j in range(m):
        if grid[i - 1][j] == "S":
            grid[i][j] = "|"
        if grid[i - 1][j] == "|":
            if grid[i][j] == ".":
                grid[i][j] = "|"
            if grid[i][j] == "^":
                ans += 1
                if j:
                    grid[i][j - 1] = "|"
                if j + 1 < m:
                    grid[i][j + 1] = "|"
for line in grid:
    print("".join(line))
print(ans)
