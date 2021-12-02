data = [x.split() for x in open('input.txt').readlines()]

# Part 1
x = 0
y = 0
for cell in data:
    if cell[0] == 'forward':
        x += int(cell[1])
    if cell[0] == 'back':
        x -= int(cell[1])
    if cell[0] == 'up':
        y -= int(cell[1])
    if cell[0] == 'down':
        y += int(cell[1])

print(x)
print(y)
print(x * y)

# Part 2
x = 0
y = 0
aim = 0
for cell in data:
    if cell[0] == 'forward':
        x += int(cell[1])
        y += aim * int(cell[1])
    if cell[0] == 'up':
        aim -= int(cell[1])
    if cell[0] == 'down':
        aim += int(cell[1])

print(x)
print(y)
print(x * y)
