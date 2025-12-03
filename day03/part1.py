with open("input.txt") as f:
    lines = f.read().splitlines()
    
ans = 0
for line in lines:
    maxi = 0
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            maxi = max(maxi, int(line[i] + line[j]))
    ans += maxi
print(ans)