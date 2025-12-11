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
        
vis = set()
def f(node, dac, fft):
    if node == "out":
        return dac and fft
    curr = 0
    for neighbour in path[node]:
        if neighbour == 'dac':
            curr += f(neighbour, True, fft)
        elif neighbour == 'fft':
            curr += f(neighbour, dac, True)
        else:
            curr += f(neighbour, dac, fft)
    return curr

ans = f('svr', False, False)
print(ans)