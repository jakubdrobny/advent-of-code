# coordinate compression and a little prefix sum trick :D
import sys

ranges = []
values = []
for line in sys.stdin:
    line = line.strip("\n")
    if not line:
        break
    x, y = map(int, line.split("-"))
    values.append(x)
    values.append(y)
    values.append(y + 1)
    ranges.append([x, y])

values.sort()
ids = {}
id = 0
inv = []
for v in values:
    if v not in ids:
        ids[v] = id
        inv.append(v)
        id += 1

N = id
marked = [0] * (N + 1)
for [x, y] in ranges:
    marked[ids[x]] += 1
    marked[ids[y] + 1] += -1

ans = 0
for i in range(N):
    if i:
        marked[i] += marked[i - 1]

    if not marked[i]:
        continue

    # now marked[i] = 1
    if not i or not marked[i - 1]:
        ans += 1

    if i and marked[i - 1]:
        ans += inv[i] - inv[i - 1]

print(ans)
