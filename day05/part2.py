with open("input.txt") as f:
    lines = f.read()
    
ranges, checks = lines.split("\n\n")
rangePairs = []
ranges = ranges.splitlines()

for line in ranges:
    start, end = map(int, line.split("-"))
    rangePairs.append([start, end])
rangePairs.sort()

newRangePairs = []
for start, end in rangePairs:
    if not newRangePairs or start > newRangePairs[-1][1]:
        newRangePairs.append([start, end])
    else:
        newRangePairs[-1][1] = max(newRangePairs[-1][1], end)
ans = 0
for start, end in newRangePairs:
    ans += end - start + 1
print(ans)