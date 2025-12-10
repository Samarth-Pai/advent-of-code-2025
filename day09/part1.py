with open("input.txt") as f:
    lines = f.read().splitlines()
    
coords = []
for line in lines:
    coords.append(tuple(map(int, line.split(",")))[::-1])
    
n = len(coords)
maxi = 0
for i in range(n):
    for j in range(i+1, n):
        x1 = coords[i][0]
        y1 = coords[i][1]
        x2 = coords[j][0]
        y2 = coords[j][1]
        
        area = (abs(x1 - x2) + 1)* (abs(y1 - y2) + 1)
        maxi = max(maxi, area)
print(maxi)