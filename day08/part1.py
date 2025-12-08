from collections import defaultdict
from heapq import heappop, heapify
class DSU:
    parent = {}
    sizes = defaultdict(lambda : 1)
    
    def __init__(self, n):
        for i in range(n):
            self.parent[i] = i
    
    def unite(self, p1, p2):
        ultp1 = self.findParent(p1)
        ultp2 = self.findParent(p2)
        
        if ultp1 == ultp2:
            return
        
        if self.sizes[ultp1] < self.sizes[ultp2]:
            self.parent[ultp1] = ultp2
            self.sizes[ultp2] += self.sizes[ultp1]
        else:
            self.parent[ultp2] = ultp1
            self.sizes[ultp1] += self.sizes[ultp2]
        
        
    def findParent(self, p):
        if p == self.parent[p]:
            return p
        self.parent[p] = self.findParent(self.parent[p])
        return self.parent[p]


with open("input.txt") as f:
    lines = f.read().splitlines()
    
points = []
def dist(p1, p2):
    return ((p2[0] - p1[0])**2 + (p2[1] - p1[1]) ** 2 + (p2[2] - p1[2])**2) ** 0.5

for line in lines:
    points.append(tuple(map(int, line.split(","))))

pairs = []
n = len(lines)
for i in range(n):
    for j in range(i+1, n):
        pairs.append((i, j))

pairs.sort(key = lambda p: dist(points[p[0]], points[p[1]]))
        
# limit = 10 # For example test case
limit = 1000
dsu = DSU(n)
for en, (i, j) in enumerate(pairs):
    if en == limit:
        break
    dsu.unite(i, j)
    
    
allParents = set(dsu.parent.values())
allSizes = [-dsu.sizes[p] for p in allParents]
ans = 1
heapify(allSizes)
for i in range(3):
    ans *= - heappop(allSizes)
print(ans)