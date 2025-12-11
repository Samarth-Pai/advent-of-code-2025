from collections import defaultdict
with open("input.txt") as f:
    lines = f.read().splitlines()

path = defaultdict(list)
for line in lines:
    split = line.split()
    source = split[0][:-1]
    targets = split[1:]
    for t in targets:
        path[source].append(t)
        
def f(node):
    if node == "out":
        return 1
    curr = 0
    for neighbour in path[node]:
        curr += f(neighbour)
    return curr

ans = f('you')
print(ans)