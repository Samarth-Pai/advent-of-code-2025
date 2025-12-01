with open("input.txt") as f:
    lines = f.read().splitlines()
    
dial = 50
password = 0
for line in lines:
    dir = line[0]
    num = int(line[1:])
    if dir == 'R':
        if num + dial >= 100:
            password += (num + dial) // 100
        dial = (dial + num) % 100
    else:
        if dial - num <= 0:
            password +=  (-(dial - num) // 100) + (dial != 0)
        dial = (dial - num) % 100
print(password)