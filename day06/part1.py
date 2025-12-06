from functools import reduce
from operator import mul, add
with open("input.txt") as f:
    lines = f.read().splitlines()
    
nums = []
for line in lines[:-1]:
    nums.append(list(map(int, line.split())))
ans = 0
print(len(lines))
for en, op in enumerate(lines[-1].split()):
    col = [nums[i][en] for i in range(len(lines)-1)]
    if op == "*":
        ans += reduce(mul, col)
    else:
        ans += sum(col)
        
print(ans)