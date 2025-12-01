import sys

pos = 50
N = 100
ans = 0

for line in sys.stdin:
    x = int(line[1:])
    if line[0] == "L":
        x = N - x
    pos = (pos + x) % N
    if pos == 0:
        ans += 1

print(ans)
