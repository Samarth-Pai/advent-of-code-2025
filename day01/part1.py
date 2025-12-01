with open("input.txt") as f:
    lines = f.read().splitlines()
    
dial = 50
password = 0
for line in lines:
    dir = line[0]
    num = int(line[1:])
    if dir == 'R':
        dial = (dial + num) % 100
    else:
        dial = (dial - num) % 100
    if dial == 0:
        password += 1
print(password)