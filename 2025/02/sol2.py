import sys


def check(x):
    s = str(x)
    for k in range(1, len(s) // 2 + 1):
        p = s[:k]
        ok = True
        for i in range(k, len(s), k):
            if s[i : i + k] != p:
                ok = False
        if ok:
            return True
    return False


for line in sys.stdin:
    x = line.split(",")
    ans = 0
    for y in x:
        a, b = map(int, y.split("-"))
        for num in range(a, b + 1):
            if check(num):
                ans += num
    print(ans)
