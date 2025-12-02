with open("input.txt") as f:
    lines = f.read().split(",")
    
ans = 0
def is_invalid(n):
    s  = str(n)
    ln = len(s)
    for k in range(1, ln//2+1):
        if ln % k != 0:
            continue
        for i in range(ln):
            if s[i] != s[i%k]:
                break
        else:
            return True
    return False

for ids in lines:
    start, end = map(int, ids.split("-"))
    for i in range(start, end+1):
        if is_invalid(i):
            ans += i
    
print(ans)