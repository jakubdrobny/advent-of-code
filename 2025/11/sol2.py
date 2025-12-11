import sys
from collections import defaultdict, deque

g = defaultdict(list)

for line in sys.stdin:
    x, y = line.split(": ")
    ys = y.split()
    for y in ys:
        g[x].append(y)

root = "svr"
FFT = 1
DAC = 2
vs = set()


def dfs(v):
    vs.add(v)
    for u in g[v]:
        if u not in vs:
            dfs(u)


dfs(root)

for v in set(g.keys()) - vs:
    del g[v]

indeg = defaultdict(int)
invg = defaultdict(list)
for v in g:
    for u in g[v]:
        indeg[u] += 1
        invg[u].append(v)

a = []
for v in g:
    if not indeg[v]:
        a.append(v)

q = deque(a)
if len(a) != 1:
    print("what?")
    exit(1)

root = a[0]
dp = defaultdict(list)
dp[root] = [1, 0, 0, 0]

bad = ["fft", "dac"]

while q:
    u = q.popleft()
    if u not in dp:
        dp[u] = [0] * 4
    for v in invg[u]:
        if u not in bad:
            dp[u][0] += dp[v][0]
        dp[u][1] += (dp[v][0] if u == "fft" else 0) + dp[v][1]
        dp[u][2] += (dp[v][0] if u == "dac" else 0) + dp[v][2]
        dp[u][3] += (
            (dp[v][1] if u == "dac" else 0) + dp[v][3] + (dp[v][2] if u == "fft" else 0)
        )
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)

print(dp["out"][DAC + FFT])
