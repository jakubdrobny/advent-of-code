from functools import cmp_to_key
import sys
import math

sys.setrecursionlimit(10000)

vt = []
K = -1
for line in sys.stdin:
    a = list(map(int, line.strip("\n").split(",")))
    if len(a) == 1:
        K = int(a[0])
    else:
        vt.append(a)

edges = []
N = len(vt)
for i in range(N):
    for j in range(i + 1, N):
        edges.append([i, j])

cash = {}


def dist(edge):
    ef = frozenset(edge)
    if ef in cash:
        return cash[ef]
    cash[ef] = math.sqrt(sum((vt[edge[0]][i] - vt[edge[1]][i]) ** 2 for i in range(3)))
    return cash[ef]


EPS = 10**-9
edges = list(
    sorted(edges, key=cmp_to_key(lambda x, y: -1 if dist(x) - dist(y) < EPS else 1))
)

par = [i for i in range(N)]
size = [1 for _ in range(N)]


def find(x):
    if par[x] == x:
        return x
    par[x] = find(par[x])
    return par[x]


def unite(x, y):
    x, y = find(x), find(y)
    if x == y:
        return
    if size[x] < size[y]:
        x, y = y, x
    size[x] += size[y]
    par[y] = x


idx = 0
while idx < K:
    i, j = edges[idx]
    x, y = find(i), find(j)
    if x != y:
        unite(x, y)
    idx += 1

leaders = set()
for i in range(N):
    leaders.add(find(i))
sizes = []
for l in leaders:
    sizes.append(size[l])
sizes.sort()
res = 1
for s in sizes[::-1][:3]:
    res *= s
print(res)
