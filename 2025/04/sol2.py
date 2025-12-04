import sys

grid = []
for line in sys.stdin:
    line = line.strip("\n")
    if line:
        grid.append(list(line))

n, m = len(grid), len(grid[0])
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

ans = 0
while True:
    cur_removed = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == ".":
                continue

            cur = 0
            for idx in range(len(dx)):
                ni, nj = i + dx[idx], j + dy[idx]
                if ni >= 0 and nj >= 0 and ni < n and nj < m and grid[ni][nj] == "@":
                    cur += 1
            if cur < 4:
                cur_removed.append((i, j))
    if not cur_removed:
        break
    ans += len(cur_removed)
    for i, j in cur_removed:
        grid[i][j] = "."
print(ans)
