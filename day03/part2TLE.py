# DP Solution. Will take forever to run
from collections import defaultdict
with open("input.txt") as f:
    lines = f.read().splitlines()
    
ans = 0

def f(ind, num, line, dp):
    if(len(num) >= 12 or ind == len(line)):
        return int(num) if num else 0
    if(dp[ind][num] != -1):
        return dp[ind][num]
    pick = f(ind+1, num + line[ind], line, dp)
    noPick = f(ind+1, num, line, dp)
    return max(pick, noPick)
    
    
for line in lines:
    dp = [defaultdict(lambda: -1) for _ in range(len(line))]

    maxi = f(0, "", line, dp)
    ans += maxi
    
print(ans)