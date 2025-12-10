import sys

testcases = []
for line in sys.stdin:
    line = line.strip("\n").split()

    want = 0
    lights = line[0][1:-1]
    for i in range(len(lights)):
        if lights[i] == "#":
            want += 1 << i

    buttons = []
    for x in line[1:-1]:
        b = list(map(int, x[1:-1].split(",")))
        button = 0
        for i in range(len(lights)):
            if i in b:
                button += 1 << i
        buttons.append(button)

    voltages = [int(x) for x in line[-1][1:-1].split(",")]

    testcases.append([want, buttons, voltages])

ans = 0

for [want, buttons, voltages] in testcases:
    n = len(voltages)
    m = len(buttons)
    min_cnt = len(buttons) + 1
    for mask in range(1 << m):
        have = 0
        cnt = 0
        for i in range(m):
            if (mask >> i) & 1:
                have = have ^ buttons[i]
                cnt += 1
        if have == want:
            min_cnt = min(min_cnt, cnt)
    ans += min_cnt

print(ans)
