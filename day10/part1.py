with open("input.txt") as f:
    lines = f.read().splitlines()
    
def check(ind: int, curr: list[str], op: int, target: list[str], buttons: list[tuple[int]]):
    # print(ind, curr)
    if curr == target:
        return op
    if ind == len(buttons):
        return float("inf")

    noPick = check(ind+1, curr, op, target, buttons)
    currCopy = curr.copy()
    for b in buttons[ind]:
        currCopy[b] = ".#"[currCopy[b] == "."]
    pick = check(ind+1, currCopy, op+1, target, buttons)
    return min(noPick, pick)
    
    
def shortestWay(target: list[str], buttons: list[tuple[int]]):
    curr = ['.' for i in range(len(target))]
    return check(0, curr, 0, target, buttons)

ans = 0
    
for line in lines:
    splits = line.split()
    target = []
    buttons = []
    for sp in splits:
        if sp[0] == '[':
            target = list(sp[1:-1])
        elif sp[0] == '(':
            buttons.append(tuple(map(int, sp[1:-1].split(","))))

    ans += shortestWay(target, buttons)
    
print(ans)