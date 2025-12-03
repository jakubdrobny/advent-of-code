import sys

K = 12

ans = 0
for line in sys.stdin:
    cur_ans = ""
    i = 0
    s = line.strip("\n")
    n = len(s)
    while i < n and len(cur_ans) < K:
        j = i + 1
        cur = i
        while j < n - K + 1 + len(cur_ans):
            if s[j] > s[cur]:
                cur = j
            j += 1
        cur_ans += s[cur]
        i = cur + 1
    ans += int(cur_ans)
print(ans)
