import sys

testcases = []
for line in sys.stdin:
    line = line.strip("\n").split()

    voltages = [int(x) for x in line[-1][1:-1].split(",")]
    buttons = []
    for x in line[1:-1]:
        buttons.append(list(map(int, x[1:-1].split(","))))

    testcases.append([buttons, voltages])

ans = 0

min_cnt = 0


def backtrack(cur, btns, tg, i, cnt):
    global min_cnt

    if cur == tg:
        min_cnt = min(min_cnt, cnt)
        return

    if i >= len(btns):
        return

    while True:
        ok = True
        for p in btns[i]:
            if cur[p] == tg[p]:
                ok = False
                break
            else:
                cur[p] += 1
        if not ok:
            break
        backtrack(list(cur), btns, tg, i + 1, cnt + 1)
        cnt += 1


for i, [buttons, voltages] in enumerate(testcases):
    n = len(voltages)
    m = len(buttons)
    cur = [0] * n
    min_cnt = max(voltages) + 1
    backtrack(cur, buttons, voltages, 0, 0)
    ans += min_cnt
    print(f"testcase {i + 1} done.")

print(ans)
