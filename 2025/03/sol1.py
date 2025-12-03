import sys

ans = 0
for line in sys.stdin:
    cur = 0
    s = line
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            x = int(s[i] + s[j])
            cur = max(cur, x)
    ans += cur
print(ans)
