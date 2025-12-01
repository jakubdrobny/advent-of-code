import sys

pos = 50
N = 100
ans = 0

for line in sys.stdin:
    x = int(line[1:])

    dt = 1 if line[0] == "R" else -1
    for _ in range(x):
        pos += dt
        if pos >= N:
            pos -= N
        if pos < 0:
            pos += N
        if pos == 0:
            ans += 1

print(ans)
