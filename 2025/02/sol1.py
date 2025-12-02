import sys


def check(x):
    s = str(x)
    return s[: len(s) // 2] == s[len(s) // 2 :]


for line in sys.stdin:
    x = line.split(",")
    ans = 0
    for y in x:
        a, b = map(int, y.split("-"))
        for num in range(a, b + 1):
            if check(num):
                ans += num
    print(ans)
