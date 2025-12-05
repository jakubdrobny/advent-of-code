# import coordinate compression
import sys

ranges = True
r = []
q = []
for line in sys.stdin:
    s = line.strip("\n")
    if not s:
        ranges = False
        continue

    if ranges:
        r.append(list(map(int, s.split("-"))))
    else:
        q.append(int(s))

values = []
for [x, y] in r:
    values.append(x)
    values.append(y)
for qq in q:
    values.append(qq)
values.sort()
ids = {}
id = 0
for v in values:
    if v not in ids:
        ids[v] = id
        id += 1
for i in range(len(r)):
    r[i] = [ids[r[i][0]], ids[r[i][1]]]
for i in range(len(q)):
    q[i] = ids[q[i]]
N = id
marked = [0] * N
for [x, y] in r:
    for i in range(x, y + 1):
        marked[i] = True
ans = 0
for qq in q:
    if marked[qq]:
        ans += 1
print(ans)
