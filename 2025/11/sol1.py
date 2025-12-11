import sys
from collections import defaultdict, deque

g = defaultdict(list)

for line in sys.stdin:
    x, y = line.split(": ")
    ys = y.split()

    for y in ys:
        g[x].append(y)

q = deque(["you"])
dp = defaultdict(int)
dp["you"] = 1

vis = defaultdict(int)
vis["you"] = 1

while q:
    v = q.popleft()
    for u in g[v]:
        dp[u] += dp[v]
        if not vis[u]:
            q.append(u)
            vis[u] = 1

print(dp["out"])
