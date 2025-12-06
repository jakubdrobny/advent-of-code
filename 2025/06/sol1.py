import sys

nums = []
ops = []
for line in sys.stdin:
    s = line.strip("\n")
    if s.count("+") == 0:
        nums.append(list(map(int, s.split())))
    else:
        ops = s.split()

m = len(nums[0])
n = len(nums)
ans = 0
for j in range(m):
    op = ops[j]
    cur = 1 if op == "*" else 0
    for i in range(n):
        if op == "*":
            cur *= nums[i][j]
        else:
            cur += nums[i][j]
    ans += cur
print(ans)
