with open("input.txt") as f:
    lines = f.read().splitlines()
    
# m x n
m = len(lines)
n = len(lines[0])
ans = 0
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
            ans += 1
print(ans)