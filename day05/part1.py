with open("input.txt") as f:
    lines = f.read()
    
ranges, checks = lines.split("\n\n")
rangePairs = []
ranges = ranges.splitlines()
checks = checks.splitlines()
for line in ranges:
    start, end = map(int, line.split("-"))
    rangePairs.append((start, end))
    
ans = 0
for check in checks:
    check = int(check)
    for start, end in rangePairs:
        if start <= check <= end:
            ans += 1
            break
print(ans)
    