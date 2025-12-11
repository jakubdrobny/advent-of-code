import sys

points = []
for line in sys.stdin:
    line = line.strip("\n")
    x, y = map(int, line.split(","))
    points.append([x, y])

xc, yc = [], []
for [x, y] in points:
    xc.append(x)
    yc.append(y)
xc.sort()
yc.sort()

idx = {}
id = 0
for x in xc:
    if x not in idx:
        idx[x] = id
        id += 1
id = 0
idy = {}
for y in yc:
    if y not in idy:
        idy[y] = id
        id += 1

p = [[idy[y], idx[x]] for [x, y] in points]
rows = len(idy)
cols = len(idx)
g = [["." for j in range(cols)] for i in range(rows)]
g[p[0][0]][p[0][1]] = "#"
for i in range(len(p)):
    pp, cp = p[(i - 1 + len(p)) % len(p)], p[i]
    g[cp[0]][cp[1]] = "#"

    if pp[0] == cp[0]:
        for x in range(pp[1] + 1, cp[1]):
            g[cp[0]][x] = "X"
    else:
        for x in range(pp[0] + 1, cp[0]):
            g[x][cp[1]] = "X"

for i in range(rows):
    print("".join(g[i]))
