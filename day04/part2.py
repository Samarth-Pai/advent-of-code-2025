from copy import deepcopy
import time
with open("input.txt") as f:
    lines = f.read().splitlines()
    
lines = [list(line) for line in lines]
    
# m x n
m = len(lines)
n = len(lines[0])
ans = 0
currLines = deepcopy(lines)
while True:
    rowPapers = 0
    for i in range(m):
        for j in range(n):
            if lines[i][j] == ".":
                continue
            cnt = 0
            # Check upper row
            if i > 0:
                cnt += lines[i-1][max(0, j - 1): j + 2].count("@")
            
            # Check lower row
            if i < m-1:
                cnt += lines[i+1][max(0, j - 1): j + 2].count("@")
            
            if j > 0 and lines[i][j-1] == "@":
                cnt += 1
            if j < n-1 and lines[i][j+1] == "@":
                cnt += 1
            
            if cnt < 4:
                currLines[i][j] = "."
                rowPapers += 1
    lines = deepcopy(currLines)
    if rowPapers == 0:
        break
    
    ans += rowPapers
print(ans)