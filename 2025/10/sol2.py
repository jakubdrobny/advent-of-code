# use linear programming :D
import sys
import numpy as np
from scipy import optimize

ans = 0
for line in sys.stdin:
    line = line.strip("\n").split()

    voltages = np.array([int(x) for x in line[-1][1:-1].split(",")])
    buttons = []
    for x in line[1:-1]:
        y = list(map(int, x[1:-1].split(",")))
        buttons.append([1 if i in y else 0 for i in range(len(voltages))])
    buttons = np.array(buttons).T

    voltages = np.reshape(voltages, (len(voltages), 1))
    c = np.ones(len(line) - 2)
    res = optimize.linprog(c, A_eq=buttons, b_eq=voltages, integrality=1)

    ans += int(round(sum(res.x)))

print(ans)
