import sys

points = []
for line in sys.stdin:
    line = line.strip("\n")
    x, y = map(int, line.split(","))
    points.append([x, y])

points.sort()

n = len(points)
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        cur = (abs(points[i][0] - points[j][0]) + 1) * (
            abs(points[i][1] - points[j][1]) + 1
        )
        print(cur)
        ans = max(ans, cur)
print(ans)
