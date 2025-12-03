with open("input.txt") as f:
    lines = f.read().splitlines()
    
ans = 0
    
for line in lines:
    curr = ""
    i, n = 0, len(line)
    while i < n:
        maxInd, maxEle = -1, "0"
        maxChar = max(line[i: n - 11 + len(curr)])
        i = i + line[i: n - 11 + len(curr)].index(maxChar) + 1
        curr += maxChar
    ans += int(curr[:12])
    
print(ans)