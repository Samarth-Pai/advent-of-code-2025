from functools import reduce
from operator import mul, add
with open("input.txt") as f:
    lines = f.read().splitlines()
    
nums = []
op = ""
ans = 0
for i in range(len(lines[0])):
    num = ""
    for j in range(len(lines)):
        if lines[j][i].isdigit():
            num += lines[j][i]
        else:
            if lines[j][i] in "*+":
                op = lines[j][i]
    if num == "":
        if op == "*":
            ans += reduce(mul, nums)
        else:
            ans += sum(nums)
        nums = []
    else:
        nums.append(int(num))
        
if op == "*":
    ans += reduce(mul, nums)
else:
    ans += sum(nums)
    
print(ans)