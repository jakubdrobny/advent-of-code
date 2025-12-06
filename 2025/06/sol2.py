# absolute pain (:
import sys

nums = []
ops = []
for line in sys.stdin:
    s = line.strip("\n")
    if s.count("+") == 0:
        l = 0
        cur_nums = []
        while l < len(s):
            if s[l] != " ":
                r = l
                while r < len(s) and s[r] != " ":
                    r += 1
                cur_nums.append([s[l:r], l, r - 1])
                l = r
            l += 1
        nums.append(cur_nums)
    else:
        ops = s.split()

m = len(nums[0])
n = len(nums)
ans = 0
for j in range(m):
    op = ops[j]
    cur = 1 if op == "*" else 0
    nnums = [""] * max(nums[i][j][2] - nums[i][j][1] + 1 for i in range(n))
    mn = min(nums[i][j][1] for i in range(n))
    mx = max(nums[i][j][2] for i in range(n))
    for i in range(n):
        for d in range(mn, mx + 1):
            if d >= nums[i][j][1] and d <= nums[i][j][2]:
                nnums[d - mn] += str(nums[i][j][0])[d - nums[i][j][1]]
    for num in nnums:
        if op == "+":
            cur += int(num)
        else:
            cur *= int(num)
    ans += cur
print(ans)
