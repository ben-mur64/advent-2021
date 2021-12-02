data = [x.split() for x in open('input.txt').readlines()]

# Part 1
x = 0
y = 0
for cell in data:
    d = cell[0]
    v = int(cell[1])

    if d == 'forward':
        x += v
    if d == 'back':
        x -= v
    if d == 'up':
        y -= v
    if d == 'down':
        y += v

print(x)
print(y)
print(x * y)

# Part 2
x = 0
y = 0
aim = 0
for cell in data:
    d = cell[0]
    v = int(cell[1])

    if d == 'forward':
        x += v
        y += aim * v
    if d == 'up':
        aim -= v
    if d == 'down':
        aim += v

print(x)
print(y)
print(x * y)
