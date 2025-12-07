with open("input.txt") as f:
    lines = f.read().splitlines()
    
sind = lines[0].index("S")
dp = [[-1 for j in range(len(lines[0]))] for i in range(len(lines))]
def f(i, j, lines, dp):
    if i == len(lines):
        return 1
    if dp[i][j] != -1:
        return dp[i][j]
    if lines[i][j] == "^":
        dp[i][j] = f(i+1, j-1, lines, dp) + f(i+1, j+1, lines, dp)
        return dp[i][j]
    else:
        dp[i][j] = f(i+1, j, lines, dp)
        return dp[i][j]
    
ans = f(1, sind, lines, dp)
print(ans)
    