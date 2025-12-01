import sys

pos = 50
N = 100
ans = 0

for line in sys.stdin:
    x = int(line[1:])

    if line[0] == "L":
        ans += x // N + (pos > 0 and x % N >= pos)
        pos = ((pos - x) % N + N) % N
    else:
        ans += x // N + (pos + x % N >= N)
        pos = (pos + x) % N

print(ans)
