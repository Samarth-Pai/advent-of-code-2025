with open("input.txt") as f:
    lines = f.read().split(",")
    
ans = 0
def is_invalid(n):
    s  = str(n)
    ln = len(s)
    return ln %2 == 0 and s[:ln//2] == s[ln//2:]

for ids in lines:
    start, end = map(int, ids.split("-"))
    for i in range(start, end+1):
        if is_invalid(i):
            ans += i
    
print(ans)
